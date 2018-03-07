'''
Reference code to showcase MXNet model prediction on AWS Lambda.

This function uses the geolocation model and predicts the lat/long for a given image and then
using the geopy module, we reserve map that to a location - country/city

@author: Sunil Mallya
'''

import base64
import os
import boto3
import json
import tempfile
import urllib2 
from urllib import urlretrieve

# Check if Lambda Function
if os.environ.get('LAMBDA_TASK_ROOT') is None:
    print "just exit, we are not in a lambda function",
    import sys; sys.exit(0)

import geopy
geolocator = geopy.geocoders.GoogleV3()
    
# del all files in tmp directory - just in case
import os
for f in os.listdir("/tmp"):
    f_path = "/tmp/" + f
    os.unlink(f_path)

import mxnet as mx
import numpy as np

from PIL import Image
from io import BytesIO
from collections import namedtuple
Batch = namedtuple('Batch', ['data'])

# Gloabls
grids, ground_truth = [], {}

f_params = 'geo/RN101-5k500-0012.params'
f_symbol = 'geo/RN101-5k500-symbol.json'
    
bucket = 'smallya-test'
s3 = boto3.resource('s3')
s3_client = boto3.client('s3')

# load labels
with open('grids.txt', 'r') as f:
    for line in f:
        line = line.strip().split('\t')
        lat = float(line[1])
        lng = float(line[2])
        grids.append((lat, lng))

# Load model
def load_model(s_fname, p_fname):
    """
    Load model checkpoint from file.
    :return: (arg_params, aux_params)
    arg_params : dict of str to NDArray
        Model parameter, dict of name to NDArray of net's weights.
    aux_params : dict of str to NDArray
        Model parameter, dict of name to NDArray of net's auxiliary states.
    """
    symbol = mx.symbol.load(s_fname)
    save_dict = mx.nd.load(p_fname)
    arg_params = {}
    aux_params = {}
    for k, v in save_dict.items():
        tp, name = k.split(':', 1)
        if tp == 'arg':
            arg_params[name] = v
        if tp == 'aux':
            aux_params[name] = v
    return symbol, arg_params, aux_params

# load labels
with open('grids.txt', 'r') as f:
    for line in f:
        line = line.strip().split('\t')
        lat = float(line[1])
        lng = float(line[2])
        grids.append((lat, lng))
   
mod = None

#params
f_params_file = tempfile.NamedTemporaryFile(delete=True)
urlretrieve("https://s3.amazonaws.com/smallya-test/geo/RN101-5k500-0012.params", f_params_file.name)
f_params_file.flush()

#symbol
f_symbol_file = tempfile.NamedTemporaryFile(delete=True)
urlretrieve("https://s3.amazonaws.com/smallya-test/geo/RN101-5k500-symbol.json", f_symbol_file.name)
f_symbol_file.flush()

sym, arg_params, aux_params = load_model(f_symbol_file.name, f_params_file.name)
mod = mx.mod.Module(symbol=sym, label_names=None)
mod.bind(for_training=False, data_shapes=[('data', (1,3,224,224))], label_shapes=mod._label_shapes)
mod.set_params(arg_params, aux_params, allow_missing=True)

f_params_file.close()
f_symbol_file.close()

### Helpers
def distance(p1, p2):
        R = 6371 # Earth radius in km
        lat1, lng1, lat2, lng2 = map(radians, (p1[0], p1[1], p2[0], p2[1]))
        dlat = lat2 - lat1
        dlng = lng2 - lng1
        a = sin(dlat * 0.5) ** 2 + cos(lat1) * cos(lat2) * (sin(dlng * 0.5) ** 2)
        return 2 * R * asin(sqrt(a))

# mean image for preprocessing
mean_rgb = np.array([123.68, 116.779, 103.939])
mean_rgb = mean_rgb.reshape((3, 1, 1))

def predict(url, dataurl):
    '''
    predict labels for a given image
    '''

    print "downloading the image"
    img_file = tempfile.NamedTemporaryFile(delete=True)
    if url:
        req = urllib2.urlopen(url)
        img_file.write(req.read())
        img_file.flush()
        img = Image.open(img_file.name)
    elif dataurl:
        #convert to image
        img_data = dataurl.split(",")[1]
        if img_data[-2] != "=":
            img_data += "=" # pad it 
        img = Image.open(BytesIO(base64.b64decode(img_data))) 
        img = img.convert('RGB')

    img_file.close()
    
    # center crop and no resize
    # ** width, height must be greater than new_width, new_height 
    #new_width, new_height = 224, 224
    #width, height = img.size   # Get dimensions
    #left = (width - new_width)/2
    #top = (height - new_height)/2
    #right = (width + new_width)/2
    #bottom = (height + new_height)/2
    #img = img.crop((left, top, right, bottom))

    # preprocess by cropping to shorter side and then resize
    short_side = min(img.size)
    left = int((img.size[0] - short_side) / 2)
    right = left + short_side
    top = int((img.size[1] - short_side) / 2)
    bottom = top + short_side
    img = img.crop((left, top, right, bottom))
    img = img.resize((224, 224), Image.ANTIALIAS)

    # convert to numpy.ndarray
    sample = np.asarray(img)  
    # swap axes to make image from (224, 224, 3) to (3, 224, 224)
    sample = np.swapaxes(sample, 0, 2)
    sample = np.swapaxes(sample, 1, 2)
    sample = sample[np.newaxis, :] 
    print sample.shape

    # sub mean? 
    normed_img = sample - mean_rgb
    normed_img = normed_img.reshape((1, 3, 224, 224))

    mod.forward(Batch([mx.nd.array(normed_img)]), is_train=False)
    prob = mod.get_outputs()[0] 
    #prob = prob.asnumpy()[0]
    #pred = np.argsort(prob)[::-1]
    # .asnumpy() seems to fail of large arrays.
    pred = mx.ndarray.argsort(prob[0])
    pred = pred.asnumpy()[::-1]
    #print "PRED", pred
    idx = pred[0]
    idx = int(idx)
    lat, lng = grids[idx] #top result
    # lat, lng
    return lat, lng

def lambda_handler(event, context):

    #url = 'http://www.japantimes.co.jp/wp-content/uploads/2016/03/n-tower-e-20160302.jpg'
    url = None 
    data_url = None

    try:
        # API Gateway GET method
        print "Request Method:", event['httpMethod']
        if event['httpMethod'] == 'GET':
            url = event['queryStringParameters']['url']
        #API Gateway POST method
        elif event['httpMethod'] == 'POST':
            data = json.loads(event['body'])
            if data.has_key('dataurl'):
                data_url = data['dataurl']
            else:
                url = data['url']
            
    except KeyError:
        # direct invocation
        url = event['url']

    print "URL:" , url
    lat, lng = predict(url, data_url)
    latlng = "%s, %s" % (lat,lng)
    loc = geolocator.reverse(latlng)
    print "LOC:" , loc 
    
    out = {
            "headers": {
                "content-type": "application/json",
                "Access-Control-Allow-Origin": "*"
                },
            "body": '{"address": "%s", "latlng": "%s"}' % (loc[0], loc[1]),  
            "statusCode": 200
          }
    return out

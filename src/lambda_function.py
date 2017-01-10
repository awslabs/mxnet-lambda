'''
Reference code to showcase MXNet model prediction on AWS Lambda 
'''

import os
import boto3
import json
import tempfile
import urllib2 

import mxnet as mx
import numpy as np
import cv2
from collections import namedtuple
Batch = namedtuple('Batch', ['data'])

f_params = 'resnet-18-0000.params'
f_symbol = 'resnet-18-symbol.json'
    
bucket = 'smallya-test'
s3 = boto3.resource('s3')
s3_client = boto3.client('s3')

#params
f_params_file = tempfile.NamedTemporaryFile()
s3_client.download_file(bucket, f_params, f_params_file.name)
f_params_file.flush()

#symbol
f_symbol_file = tempfile.NamedTemporaryFile()
s3_client.download_file(bucket, f_symbol, f_symbol_file.name)
f_symbol_file.flush()

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

def predict(url, mod, synsets):
    '''
    predict labels for a given image
    '''

    req = urllib2.urlopen(url)
    arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
    cv2_img = cv2.imdecode(arr, -1)
    img = cv2.cvtColor(cv2_img, cv2.COLOR_BGR2RGB)
    if img is None:
        return None
    img = cv2.resize(img, (224, 224))
    img = np.swapaxes(img, 0, 2)
    img = np.swapaxes(img, 1, 2) 
    img = img[np.newaxis, :] 
    
    mod.forward(Batch([mx.nd.array(img)]))
    prob = mod.get_outputs()[0].asnumpy()
    prob = np.squeeze(prob)

    a = np.argsort(prob)[::-1]
    out = '' 
    for i in a[0:5]:
        out += 'probability=%f, class=%s' %(prob[i], synsets[i])
    out += "\n"
    return out

with open('synset.txt', 'r') as f:
    synsets = [l.rstrip() for l in f]

def lambda_handler(event, context):

    url = ''

    # API Gateway GET method
    if event['httpMethod'] == 'GET':
        url = event['queryStringParameters']['url']
    # API Gateway POST method
    elif event['httpMethod'] == 'POST':
        data = json.loads(event['body'])
        url = data['url']
    # Direct Lambda invocations
    else:
        url = event['url']
    
    sym, arg_params, aux_params = load_model(f_symbol_file.name, f_params_file.name)
    mod = mx.mod.Module(symbol=sym)
    mod.bind(for_training=False, data_shapes=[('data', (1,3,224,224))])
    mod.set_params(arg_params, aux_params)
    labels = predict(url, mod, synsets)
    
    #TODO: Handle error cases on failure

    out = {
            "headers": {
                "content-type": "application/json",
                "Access-Control-Allow-Origin": "*"
                },
            "body": labels,  
            "statusCode": 200
          }
    return out

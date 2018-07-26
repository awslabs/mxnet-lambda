import mxnet as mx
import tempfile
import urllib2
import numpy as np
from PIL import Image

from model_loader import sym, arg_params, aux_params, labels

from collections import namedtuple
from StringIO import StringIO


ctx = mx.cpu()


def preprocess(event):
    """
    Preprocess Lambda event into input data format for mx mod.
    :return: input data NDArray
    event : dict
        Lambda event
    """
    img = None
    try:
        # GET method
        if event.get('httpMethod') == 'GET':
            url = event['queryStringParameters']['url']
            # download image from url
            img_file = tempfile.NamedTemporaryFile(delete=True)
            if url:
                req = urllib2.urlopen(url)
                img_file.write(req.read())
                img_file.flush()
            img = Image.open(img_file.name)
            img_file.close()
        # POST method
        else:
            multipart_string = event['body'].decode('base64')
            img = Image.open(StringIO(multipart_string))
    except KeyError:
        # direct invocation
        url = event['url']
        # download image from url
        img_file = tempfile.NamedTemporaryFile(delete=True)
        if url:
            req = urllib2.urlopen(url)
            img_file.write(req.read())
            img_file.flush()
        img = Image.open(img_file.name)
        img_file.close()
    # prepare data
    img = img.resize((224, 224))
    img = mx.nd.array(img)
    img = img.transpose((2, 0, 1))
    img = img.expand_dims(axis=0)
    return img


def inference(data):
    """
    Run inference on data.
    :return: output NDArray
    data : NDArray
        data for mx mod
    """
    # define a simple data batch
    Batch = namedtuple('Batch', ['data'])
    # load required models
    mod = mx.mod.Module(symbol=sym, context=ctx, label_names=None)
    mod.bind(for_training=False, data_shapes=[('data', data.shape)], 
             label_shapes=mod._label_shapes)
    mod.set_params(arg_params, aux_params, allow_missing=True)
    # run inference and get the output
    mod.forward(Batch([data]))
    prob = mod.get_outputs()[0].asnumpy()
    prob = np.squeeze(prob)
    return np.argsort(prob)[::-1][0]


def postprocess(output):
    """
    Postprocess model output into response body.
    :return: response body string
    output : NDArray
        output from mx mod
    """
    # index label from synset
    return '{"category": "%s"}' % (labels[output])

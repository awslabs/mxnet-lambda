import mxnet as mx
from model_loader import sym, arg_params, aux_params

import tempfile
import urllib2

import numpy as np
from PIL import Image
from StringIO import StringIO


ctx = mx.cpu()


def preprocess(event):
    """
    Preprocess Lambda event into input format for mx mod.
    :return: input NDArray
    event : dict
        Lambda event
    """
    img = None
    try:
        # GET method
        if event.has_key('httpMethod') and event['httpMethod'] == 'GET':
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
    # prepare input
    img = img.resize((224, 224))
    img = mx.nd.array(img)
    img = img.transpose((2, 0, 1))
    img = img.expand_dims(axis=0)
    return img


def inference(input):
    """
    Run inference on input.
    :return: output NDArray
    input : NDArray
        input for mx mod
    """
    # define a simple data batch
    from collections import namedtuple
    Batch = namedtuple('Batch', ['data'])
    # load required models
    mod = mx.mod.Module(symbol=sym, context=ctx, label_names=None)
    mod.bind(for_training=False, data_shapes=[('data', input.shape)], 
             label_shapes=mod._label_shapes)
    mod.set_params(arg_params, aux_params, allow_missing=True)
    # run inference and get the output
    mod.forward(Batch([input]))
    prob = mod.get_outputs()[0].asnumpy()
    prob = np.squeeze(prob)
    a = np.argsort(prob)[::-1]
    return a[0]


def postprocess(output):
    """
    Postprocess model output into response body.
    :return: response body string
    output : NDArray
        output from mx mod
    """
    # load labels from synset
    with open('synset.txt', 'r') as f:
        labels = [l.rstrip() for l in f]
    # index label from synset
    return '{"category": "%s"}' % (labels[output])

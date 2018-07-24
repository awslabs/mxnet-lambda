from __future__ import print_function

import urllib
import sys
import os
import json
import subprocess

import yaml

class Context(object):
    pass

class BaseResponse(object):

    def __init__(self, response_body=""):
        self.headers = []
        self.status_code = 200
        self.body = response_body

    def get_dict(self):
        return {"headers":dict(self.headers), "body":self.body, "statusCode":self.status_code}

    def add_response_property(self, key, value):
        self.headers.append((key, value))

    def set_response_status(self, code, reason_string=None):
        self.status_code = code

    def set_response_body(self, response_body):
        self.body = response_body


def lambda_handler(event, context):
    config = yaml.load(open('config.yaml'))
    model_url = config["url_mar"]
    urllib.urlretrieve(model_url, "/tmp/mar.zip")
    subprocess.call("unzip /tmp/mar.zip -d /tmp", shell=True)
    sys.path.insert(0, os.getcwd())
    os.chdir("/tmp")
    with open('MANIFEST.json') as f:
        manifest = json.load(f)
    sys.path.insert(0, os.getcwd())
    module_name, function_name = manifest["model"]["handler"].split(":")
    handler = __import__(module_name)
    inference = getattr(handler, function_name)

    response = BaseResponse()
    ctx = Context
    ctx.log = print
    ctx.add_metrics = print
    ctx.get_request_property = lambda x : context.get("headers").get(x)
    ctx.get_system_info = lambda : context
    ctx.add_response_property = response.add_response_property
    ctx.set_response_status = response.set_response_status
    
    data = [[{"key": "data", "value": event}]]

    output = inference(data, ctx)
    
    response.set_response_body(output)

    return response.get_dict()

from __future__ import print_function

import urllib
import sys
import os
import json
import subprocess

class Context(object):
    def __init__(self, logger, metrics_writter, request, response, system_info):
        self.logger = logger
        self.metrics_writter = metrics_writter
        self.request = request
        self.response = response
        self.system_info = system_info


class BaseResponse(object):
    """BaseResponse if the object providing standard response attributes and operations"""
    def __init__(self, response_body=""):
        """Constructor, construct a response

        Parameters
        ----------
        response_body: Optionally give the response a non-empty body
        """
        self.headers = []
        self.status_code = 200
        self.body = response_body

    def get_dict(self):
        """Get the response in dict form"""
        return {"headers":dict(self.headers), "body":self.body, "statusCode":self.status_code}

    def add_response_property(self, key, value):
        """Add a pair of property to response

        Parameters
        ----------
        key: string
            Key of the property
        value: string
            Value of the property
        """
        self.headers.append((key, value))

    def set_response_status(self, code, reason_string=None):
        """Set the response status

        Parameters
        ----------
        code: int
            Status code of the response
        reason_string: string
            Optional non-default response reason string
        """
        self.status_code = code

    def set_response_body(self, response_body):
        """Set the response body

        Parameters
        ----------
        response_body: object
            The body of response
        """
        self.body = response_body


def lambda_handler(event, context):
    """Calculate the outputs specified by the bound symbol.

    Parameters
    ----------
    event: dict, list, str, int, float, or NoneType 
        AWS Lambda uses this parameter to pass in event data to the handler. 
    context: LambdaContext
        AWS Lambda uses this parameter to provide runtime information to your handler. 

    Returns
    -------
    response_dict: Returns the response of lambda_handler in dict.
        In the HTTP response to the invocation request, serialized into JSON.
    """
    # load config
    with open('config.json', 'r') as file:
        config = json.load(file)
    model_url = config["url_model_archive"]
    # download and unzip MAR
    urllib.urlretrieve(model_url, "/tmp/mar.zip")
    subprocess.call("unzip /tmp/mar.zip -d /tmp", shell=True)
    # change wd and make sure dir containing this file and MAR are both in PYTHONPATH
    trigger_dir = os.getcwd()
    sys.path.insert(0, trigger_dir)
    os.chdir("/tmp")
    sys.path.insert(0, os.getcwd())
    # read MANIFEST to get MAR handler
    with open('MANIFEST.json') as f:
        manifest = json.load(f)
    module_name, function_name = manifest["model"]["handler"].split(":")
    handler = __import__(module_name)
    inference = getattr(handler, function_name)

    # prepare context object for MAR handler
    response = BaseResponse()
    
    ctx = Context(lambda : print, lambda : print, lambda : event.get("headers"), response, context)
    ctx.log = print
    ctx.add_metrics = print
    ctx.get_request_property = lambda x : context.get("headers").get(x)
    ctx.get_system_info = lambda : context
    ctx.add_response_property = response.add_response_property
    ctx.set_response_status = response.set_response_status
    # prepare data object for MAR handler
    data = [[{"key": "data", "value": event.get("body")}]]

    # trigger MAR handler and get response body
    output = inference(data, ctx)
    response.set_response_body(output)
    
    # reverse working dir to avoid config file not found
    os.chdir(trigger_dir)

    return response.get_dict()

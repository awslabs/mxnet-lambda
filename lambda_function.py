from __future__ import print_function


handler = __import__(module_name)
inference = getattr(handler, function_name)


class BaseResponse:

    def __init__(self, response_body):
        self.headers = ["content-type": "application/json", "Access-Control-Allow-Origin": "*"]
        self.statusCode = 200
        self.body = response_body

    def get_dict(self):
        return {"headers":dict(self.headers), "body":self.body, "statusCode":self.statusCode}

    def set_headers(self, headers):
        self.headers = list(headers)

    def set_status_code(self, status_code):
        self.status_code = status_code

    def set_response_body(self, response_body):
        self.body = response_body


def lambda_handler(event, context):

    response = BaseResponse()
    ctx.set_headers = response.set_headers
    ctx.log = print
    ctx.metrix = print
    for key, value in context:
        ctx
    output = inference(data, ctx)
    
    response.set_response_body(output)

    return response

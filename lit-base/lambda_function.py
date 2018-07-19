from model_service import preprocess, inference, postprocess


class BaseResponse:

    def __init__(self, response_body):
        self.headers = {"content-type": "application/json", "Access-Control-Allow-Origin": "*"}
        self.statusCode = 200
        self.body = response_body

    def get_dict(self):
        return {"headers":self.headers, "body":self.body, "statusCode":self.statusCode}


def lambda_handler(event, context):

    # serving 
    data    = preprocess(event)
    output   = inference(data)
    response_body = postprocess(output)
    
    response = BaseResponse(response_body).get_dict()

    return response

from model_service import preprocess, inference, postprocess


class BaseResponse:
    """BaseResponse if the object providing standard response attributes and operations"""
    def __init__(self, response_body):
        """Constructor, construct a response
        Parameters
        ----------
        response_body: Optionally give the response a non-empty body
        """
        self.headers = {"content-type": "application/json", "Access-Control-Allow-Origin": "*"}
        self.statusCode = 200
        self.body = response_body

    def get_dict(self):
        """Get the dictionary representation of the response
        Return
        ----------
        dict: the dictionary representation of the response
        """
        return {"headers":self.headers, "body":self.body, "statusCode":self.statusCode}


def lambda_handler(event, context):
    # serving 
    data    = preprocess(event)
    output   = inference(data)
    response_body = postprocess(output)
    
    response = BaseResponse(response_body).get_dict()

    return response

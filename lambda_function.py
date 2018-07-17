from model_service import preprocess, inference, postprocess


def lambda_handler(event, context):

    # serving 
    input    = preprocess(event)
    output   = inference(input)
    response = postprocess(output)
    
    out = {
            "headers": {
                "content-type": "application/json",
                "Access-Control-Allow-Origin": "*"
                },
            "body": response,
            "statusCode": 200
          }
    return out

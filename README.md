# MXNet package for AWS Lambda

This is a reference application that predict labels for an image, using a pre-built model on MXNet deployed on [AWS Lambda](https://aws.amazon.com/lambda). You can leverage the precompiled libraries to build your prediction pipeline on Lambda.

## Components

- MXNet
- OpenCV
- Numpy

## Instructions

- Create a Lambda function from the CLI by running the following commands: 

```
cd mxnet-lambda
zip -9r lambda_function.zip  * 
aws lambda update-function-code --function-name mxnet-lambda --zip-file fileb://lambda_function.zip

```

- Test the Lambda function: 
```
aws lambda invoke --invocation-type RequestResponse --function-name mxnet-lambda --region us-east-1 --log-type Tail --payload '{"url": "https://images-na.ssl-images-amazon.com/images/G/01/img15/pet-products/small-tiles/23695_pets_vertical_store_dogs_small_tile_8._CB312176604_.jpg"}' output_file
```

## Notes

All the necessary libraries needed for MXNet have been copied to the src/lib folder. In addition, OpenCV for Python is also available for your use.  

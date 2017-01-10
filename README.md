# MXNet package for AWS Lambda

This is a reference application that uses a pre-built model using MXNet deployed on AWS Lambda to predict labels for an image. You can leverage the pre-compiled libraries to build your prediction pipeline on AWS Lambda.

## Components

- MXNet
- OpenCV
- Numpy

## Instructions

- Create a lambda function from the CLI by running the following commands 

```
cd mxnet-lambda
zip -9r lambda_function.zip  * 
aws lambda update-function-code --function-name mxnet-lambda --zip-file fileb://lambda_function.zip

```

- Test the lambda function 
```
aws lambda invoke --invocation-type RequestResponse --function-name mxnet-lambda --region us-east-1 --log-type Tail --payload '{"url": "https://images-na.ssl-images-amazon.com/images/G/01/img15/pet-products/small-tiles/23695_pets_vertical_store_dogs_small_tile_8._CB312176604_.jpg"}' output_file
```

## Notes

All the necessary libraries needed for MXNet have been copied over to src/lib folder. In addition OpenCV for python is also made available for use.  

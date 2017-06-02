# MXNet package for AWS Lambda

This is a reference application that predict labels for an image, using a pre-built model on MXNet deployed on [AWS Lambda](https://aws.amazon.com/lambda). You can leverage the precompiled libraries to build your prediction pipeline on Lambda.

## Components

- MXNet 0.10.1
- Numpy
- PIL

* boto3 is included in the Lambda environment, if you want to try it locally please pip install boto3 in your virtualenv 

## Instructions

- Create a Lambda function from the CLI by running the following commands: 

```
cd mxnet-lambda/src
zip -9r lambda_function.zip  * 
aws lambda create-function --function-name mxnet-lambda-v2 --zip-file fileb://lambda_function.zip --runtime python2.7 --region us-east-1 --role MY_ROLE_ARN --handler lambda_function.lambda_handler --memory-size 1536 --timeout 60

```
- Update the Lambda function code
 
```
aws lambda update-function-code --function-name mxnet-lambda-v2 --zip-file fileb://lambda_function.zip
```
- Test the Lambda function: 
```
aws lambda invoke --invocation-type RequestResponse --function-name mxnet-lambda-v2 --region us-east-1 --log-type Tail --payload '{"url": "https://images-na.ssl-images-amazon.com/images/G/01/img15/pet-products/small-tiles/23695_pets_vertical_store_dogs_small_tile_8._CB312176604_.jpg"}' output_file
```

## Build MXNet package from source for AWS Lambda

- compile MXNet on Amazon Linux (AMI name: amzn-ami-hvm-2016.03.3.x86_64-gp2)

```
$ git clone --recursive https://github.com/dmlc/mxnet mxnet
$ cd mxnet 
$ make -j $(nproc) USE_OPENCV=0 USE_CUDNN=0 USE_CUDA=0 USE_BLAS=openblas 
```

- build python bindings

```
$ cd python
$ python setup.py install
```

- copy python bindings 

```
$ mkdir mxnet-lambda-pkg
$ cd mxnet-lambda-pkg 
$ cp -r /usr/local/lib/python2.7/site-packages/mxnet-0.10.1-py2.7.egg . 
$ mv mxnet-0.10.1-py2.7.egg/mxnet . 
```

- copy all the support libraries to lib folder

```
$ mkdir lib

Copy all the following libraries from /usr/local/lib or /usr/lib/ to lib/ directory  

libatlas.a       libcblas.so.3.0    libf77blas.so.3.0  libopenblas.so.0   libptf77blas.so.3
libatlas.so.3    libclapack.so.3    libgfortran.so.3   libptcblas.a       libptf77blas.so.3.0
libatlas.so.3.0  libclapack.so.3.0  liblapack.a        libptcblas.so.3    libquadmath.so.0
libcblas.a       libf77blas.a       liblapack.so.3     libptcblas.so.3.0
libcblas.so.3    libf77blas.so.3    liblapack.so.3.0   libptf77blas.a

```


## Notes

All the necessary libraries needed for MXNet have been copied to the src/lib folder. In addition, PIL for Python is also available for your use. OpenCV was available in the previous release, but has been taken out to reduce the size of the code package. Refer to opencv branch for the code 

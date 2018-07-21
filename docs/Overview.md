## Introduction

Lambda Inference Toolkit provides a toolkit for testing, deploying and serving machine learning models in a serverless manner.

It is built on MXNet and AWS Lambda, but could also deploy models developed with other frameworks that support ONNX (PyTorch, CNTK, Caffe2, etc.). It provides a charge-by-query solution for AWS customers who host/use AI applications, with reasonable performance and effortless and limitless scalability. 

## Components
```
lambda-inference-toolkit/
       LICENSE
       README.md
       /lit-cli/          # LIT Client
             client.py
             setup.py
       /lit-base/         # LIT Base Package
             /mxnet/*
             /mxnet-0.12.0-py2.7.egg/*
             /lib/*
             lambda_function.py
             model_service.py
             model_loader.py
             model_url.py
             setup.cfg
             [other_dependencies]
       /sam/              # SAM Support
             template.yaml
             swagger.yaml
       /opencv/           # OpenCV Support
             /cv2/*
             /lib/*
```

## System Design

**Serverless Model Serving**

First models are trained and exported into model zoo, ONNX or saved as checkpoint (CKPT). Then we use Lambda Inference Toolkit to pack the model into a package that's Inference + Lambda enabled (*details on this part explained in the next graph*). Then the deployed package will be served on AWS Lambda with charge by query, reasonable response time, and effortless and limitless scalability. The serverless model serving could be triggered by AWS Services (S3, API Gateway, Kinesis, Dynamo, Kinesis, etc.), API Callbacks, HTTP, Mobile, etc., and the serving itself is also supported by AWS services (together with Java, Python, etc.).

**Lambda Inference Toolkit**

The Lambda Inference Toolkit has three major functions and three major components. Three major functions are **Inference Package Construction, Inference Package Maintenance and Easy Package Deployment.** These three major functions are supported by three major components: LIT Client, LIT Base Package, and LIT Model Bucket. 

LIT Base Package is a base package with decent modularization that runs a sample Lambda enabled inference task. LIT Model Bucket is an online S3 resource that host models for Lambda enabled inference. With pre-packed LIT Base Package (with MxNet pre-configured), users only need to customize local inference logics to create their own deployable Lambda enabled inference package. LIT Base Package also communicate LIT Model Bucket when being served on AWS Lambda. LIT Client is a command line tool based on AWS CLI to significantly simplify the process of construct, maintain, deploy, and update a Lambda enabled inference package. 

## References

[MXNet](https://mxnet.incubator.apache.org)

[Model Server for MXNet](https://github.com/awslabs/mxnet-model-server)

[AWS Lambda](https://aws.amazon.com/lambda/)

[Train Your Machine Learning Model with SageMaker](https://aws.amazon.com/sagemaker/)

[Test Your Lambda Package Locally with SAM CLI](https://github.com/awslabs/aws-sam-cli)
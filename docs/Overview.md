## Introduction

MXNet Lambda provides a toolkit for testing, deploying and serving deep learning models with Apache MXNet (incubating) in a serverless manner.

It is built on MXNet and AWS Lambda, but could also deploy models developed with other frameworks that support ONNX (PyTorch, CNTK, Caffe2, etc.). It provides a charge-by-query solution for AWS customers who host/use AI applications, with reasonable performance and effortless and limitless scalability. 

## Components
```
mxnet-lambda/
       LICENSE
       README.md
       /mar/          # Model Archive Support Framework
             config.json
             lambda_function.py
       /base/         # Base Code for Running Inference on AWS Lambda
             lambda_function.py
             model_service.py
             model_loader.py
             model_url.py
             requirements.txt
       /sam/          # SAM Templates Support
             template.yaml
             swagger.yaml
       /scripts/      # Utilities
             configure.py
       /docs/*        # Documentation
```

## System Design

**Serverless Model Serving**

First models are trained and exported into model zoo, ONNX or saved as checkpoint (CKPT). Then we use Lambda Inference Toolkit to pack the model into a package that's Inference + Lambda enabled (*details on this part explained in the next graph*). Then the deployed package will be served on AWS Lambda with charge by query, reasonable response time, and effortless and limitless scalability. The serverless model serving could be triggered by AWS Services (S3, API Gateway, Kinesis, Dynamo, Kinesis, etc.), API Callbacks, HTTP, Mobile, etc., and the serving itself is also supported by AWS services (together with Java, Python, etc.).

**MXNet Lambda**

MXNet Lambda has two major functions and four major components. Three major functions are **Consuming Model Archive on AWS Lambda and  Running Inference with Apache MXNet (incubating) on AWS Lambda.** These two major functions are supported by four major components: Model Archive Support Framework, Base Code for Running Inference on AWS Lambda, SAM Templates Support, and Utilities. 

Model Archive Support Framework is a framework that supports consuming Model Archive formatted machine learning models on AWS Lambda. Base Code for Running Inference on AWS Lambda is a base package with decent modularization that runs a sample Lambda enabled inference task. SAM Templates Support is AWS Serverless Application Model descriptive code to significantly simplify the process of construct, maintain, test, deploy, and update a Lambda enabled inference package. Utilities provides scripts that help process Model Archives. 

## References

[MXNet](https://mxnet.incubator.apache.org)

[Model Server for MXNet](https://github.com/awslabs/mxnet-model-server)

[AWS Lambda](https://aws.amazon.com/lambda/)

[Train Your Machine Learning Model with SageMaker](https://aws.amazon.com/sagemaker/)

[Test Your Lambda Package Locally with SAM CLI](https://github.com/awslabs/aws-sam-cli)

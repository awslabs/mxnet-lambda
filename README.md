# Lambda-Inference-Toolkit (LIT)

## Introduction

Lambda Inference Toolkit provides a toolkit for testing, deploying and serving machine learning models in a serverless manner.

It is built on MXNet and AWS Lambda, but could also deploy models developed with other frameworks that support ONNX (PyTorch, CNTK, Caffe2, etc.). It provides a charge-by-query solution for AWS customers who host/use AI applications, with reasonable performance and effortless and limitless scalability. 

## Documentation

[Lambda Inference Toolkit Wiki](docs/Home.md)

## Demo
```
curl -i -H "Content-Type: application/json" -X GET 'https://1hlvxxnt2e.execute-api.us-east-2.amazonaws.com/init/lit-demo?url=https://github.com/dmlc/web-data/blob/master/mxnet/doc/tutorials/python/predict_image/cat.jpg?raw=true'
```
If you don't have curl handy, you can either find it here https://curl.haxx.se, or just copy and paste the full link inside single quote into your browser.

![image to infer](https://raw.githubusercontent.com/dmlc/web-data/master/mxnet/doc/tutorials/python/predict_image/cat.jpg)
```
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: 35
{"category": "n02123159 tiger cat"}
```

## Quickstart

#### Prerequisites
AWS CLI (https://aws.amazon.com/cli/) configured

AWS IAM ARN (https://docs.aws.amazon.com/IAM/latest/UserGuide//id_roles.html) setup

Python 2.7 (https://www.python.org/download/releases/2.7/) with `pip`

[Optional] ONNX (https://github.com/onnx/onnx) if you want to import from ONNX

#### Installation
```
git clone https://github.com/anchen1011/lambda-inference-toolkit.git
cd lambda-inference-toolkit
pip install lit-cli/
```

#### Create and deploy package
```
lit-cli create lit-demo
cd lit-demo
lit-cli deploy --role ROLE_ARN
```
AWS has provide a role template for Lambda, and could be created following https://docs.aws.amazon.com/lambda/latest/dg/with-userapp-walkthrough-custom-events-create-iam-role.html

Make sure your `ROLE_ARN` is in the format of `arn:aws:iam::<number>:role/<role_name>` (https://github.com/motdotla/node-lambda-template/issues/1).

#### Invoke your package
```
aws lambda invoke \
--invocation-type RequestResponse \
--function-name lit-demo \
--region us-east-2 \
--log-type Tail \
--payload '{"url": "https://github.com/dmlc/web-data/blob/master/mxnet/doc/tutorials/python/predict_image/cat.jpg?raw=true"}' \
output.json
```

# MXNet Lambda

## Introduction

MXNet Lambda provides a toolkit for testing, deploying and serving deep learning models using MXNet using a serverless approach.

It is built on MXNet and AWS Lambda, but could also deploy models developed with other frameworks that support ONNX (PyTorch, CNTK, Caffe2, etc.). It provides a charge-by-query solution for AWS customers who host/use AI applications, with reasonable performance and effortless and limitless scalability. 

## Documentation

[MXNet Lambda Wiki](docs/Home.md)

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

#### Installation
```
git clone https://github.com/anchen1011/mxnet-lambda.git
cd mxnet-lambda
pip install lit-cli/
```

#### Create and deploy package
```
lit-cli create mxnet-lambda-demo
cd mxnet-lambda-demo
lit-cli install requirements.txt -r
lit-cli deploy --role ROLE_ARN
```
AWS provides managed role for Lambda, and could be created following https://docs.aws.amazon.com/lambda/latest/dg/with-userapp-walkthrough-custom-events-create-iam-role.html

Make sure your `ROLE_ARN` is in the format of `arn:aws:iam::<iam_account_number>:role/<role_name>`.

#### Invoke your package
```
aws lambda invoke \
--invocation-type RequestResponse \
--function-name mxnet-lambda-demo \
--region us-east-2 \
--log-type Tail \
--payload '{"url": "https://github.com/dmlc/web-data/blob/master/mxnet/doc/tutorials/python/predict_image/cat.jpg?raw=true"}' \
output.json
```

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

## Quickstart: SAM + MAR

#### Prerequisites
AWS CLI (https://aws.amazon.com/cli/) configured

AWS IAM ARN (https://docs.aws.amazon.com/IAM/latest/UserGuide//id_roles.html) setup

Python 2.7 (https://www.python.org/download/releases/2.7/) with `pip`

* In the AWS Region you plan to deploy, make sure you have an existing Amazon S3 bucket in which SAM can create the deployment artifacts.

Else create a new bucket using the following AWS CLI command:

```
aws s3 mb s3://<your-bucket-name> --region <your-bucket-region>
```

#### Installation
```
git clone https://github.com/anchen1011/mxnet-lambda.git
cd mxnet-lambda
pip install lit-cli/
```

#### Create package
```
cp -r lit-mar PACKAGE_NAME
cd PACKAGE_NAME
cp ../sam/* .
```

#### [Optional] Configure Model Archive (only on Amazon Linux)
If your model archive pack all requirements inside the MAR, modify `config.json` and then you are good.

Otherwise, make sure to configure it with
```
lit-cli use <MODEL_ARCHIVE> [--model-bucket <MODEL_BUCKET>]
```
e.g.
```
lit-cli use https://s3.us-east-2.amazonaws.com/baiachen-amazon-ai-work-data/img_classification_exp.mar
```

#### Deploy package
- Before deploying the project to SAM for the first time, you'll need to update some variables in `template.yaml`/`swagger.yaml`

```
# swagger.yaml
# <<region>> : AWS region set in Pre-Requisites, referenced twice in swagger.yaml (e.g. us-east-2)
# <<accountId>> : your global AWS account ID (found in MyAccount, e.g. 537123456789)
uri: arn:aws:apigateway:<<region>>:lambda:path/2015-03-31/functions/arn:aws:lambda:<<region>>:<<accountId>>:function:${stageVariables.LambdaFunctionName}/invocations

# template.yaml (you don't need to make change here if you follow every step in this page)
CodeUri: path/to/lambda_function.zip
DefinitionUri: path/to/swagger.yaml
```

- Pack Lambda Function
```
zip -r9 lambda_function.zip *
```

- Execute the AWS Cloudformation SAM commands to create the Serverless application

```
aws cloudformation package \
--template-file ./template.yaml \
--output-template-file ./template-out.yaml \
--s3-bucket <your-s3-bucket-name>

aws cloudformation deploy \
--template-file ./template-out.yaml \
--stack-name <STACK_NAME> \
--capabilities CAPABILITY_IAM
```
 

- Get the URL of the Serverless application that was created

```
aws cloudformation describe-stacks --stack-name <STACK_NAME> | python -c 'import json,sys;obj=json.load(sys.stdin);print obj["Stacks"][0]["Outputs"][0]["OutputValue"];'
```

#### Test with POST request

```
wget https://s3.us-east-2.amazonaws.com/baiachen-amazon-ai-work-data/cat.png
curl -H "Content-Type: image/png" -X POST https://MY_URL -T "cat.png"
```


## Quickstart: CLI 

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

#### Create and deploy package (only on Amazon Linux)
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

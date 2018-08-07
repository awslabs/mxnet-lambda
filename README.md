# MXNet Lambda

## Introduction

MXNet Lambda provides a toolkit for testing, deploying and serving deep learning models using Apache MXNet (incubating) using a serverless approach.

It is built on Apache MXNet (incubating) and AWS Lambda, but could also deploy models developed with other frameworks that support ONNX (PyTorch, CNTK, Caffe2, etc.). It provides a charge-by-query solution for AWS customers who host/use AI applications, with reasonable performance and effortless and limitless scalability. 

## Documentation

[MXNet Lambda Wiki](docs/Home.md)

## Demo
```
curl -i -H "Content-Type: application/json" -X GET 'https://1hlvxxnt2e.execute-api.us-east-2.amazonaws.com/init/lit-demo?url=https://s3.us-east-2.amazonaws.com/baiachen-amazon-ai-work-data/cat.png'
```
If you don't have curl handy, you can either find it here https://curl.haxx.se, or just copy and paste the full link inside single quote into your browser.

![image to infer](docs/cat.png)
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

In the AWS Region you plan to deploy, make sure you have an existing Amazon S3 bucket in which SAM can create the deployment artifacts.

* Else create a new bucket using the following AWS CLI command:

```
aws s3 mb s3://<your-bucket-name> --region <your-bucket-region>
```

#### Create package
```
cp -r mar mxnet-lambda-demo
cd mxnet-lambda-demo
cp ../sam/* .
```

#### [Optional] Configure Model Archive (only on Amazon Linux)
If your model archive pack all requirements inside the MAR, modify `config.json` and then you are good.

Otherwise, make sure to configure it with `scripts/configure.py`
```
python configure.py model_archive lambda_function_path [model_bucket]
```
e.g.
```
cd ../scripts
lit-cli configure.py  https://s3.us-east-2.amazonaws.com/baiachen-amazon-ai-work-data/img_classification_exp.mar ../mxnet-lambda-demo
cd -
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
curl -O https://s3.us-east-2.amazonaws.com/baiachen-amazon-ai-work-data/cat.png
curl -H "Content-Type: image/png" -X POST https://MY_URL -T "cat.png"
```

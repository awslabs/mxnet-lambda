* In the AWS Region you plan to deploy, make sure you have an existing Amazon S3 bucket in which SAM can create the deployment artifacts.

Else create a new bucket using the following AWS CLI command:

```
aws s3 mb s3://<your-bucket-name>
```
If you need a bucket but don't have one, you can 
create new bucket using the following AWS CLI command:

```
aws s3 mb s3://<your-bucket-name>
```

## Get Help
[SAM Documentation](https://github.com/awslabs/serverless-application-model/blob/master/HOWTO.md)

## Create Package
Copy the `base` template and `sam` template to get started.
```
cp -r `base` PACKAGE_NAME
cd PACKAGE_NAME
cp ../sam/* .
```

## Configure Package (some files are in `sam/` folder)
Update `model_service.py`, `model_url.py`, `template.yaml` )and/or `swagger.yaml`).

#### Model Service
```
# model_service.py
preprocess(event)   # preprocess the requested event into the model input
inference(input)    # load model to run inference logic on the input to produce output
postprocess(output) # postprocess the output to get the formatted response
```

#### Model URL
URL to the standard MXNet model description files (you may want to upload them to S3 if you don't have them online
```
# model_url.py
url_params = "https://PARAMS_URL"
url_symbol = "https://SYMBOL_URL"
```

#### SAM Template
Setup the S3 bucket for SAM
```
# template.yaml
CodeUri: CodeUri: path/to/lambda_function.zip
```

#### More Resources (e.g. API Gateway)
Setup more resources/services according to [SAM Doc](https://github.com/awslabs/serverless-application-model/blob/master/HOWTO.md) or [CloudFormation Doc](https://aws.amazon.com/documentation/cloudformation/)

For example, setup a POST file API Gateway with demo swagger file
```
# swagger.yaml
# <<region>> : AWS region set in Pre-Requisites, referenced twice in swagger.yaml
# <<accountId>> : your global AWS account ID (found in MyAccount)
uri: arn:aws:apigateway:<<region>>:lambda:path/2015-03-31/functions/arn:aws:lambda:<<region>>:<<accountId>>:function:${stageVariables.LambdaFunctionName}/invocations

# template.yaml
DefinitionUri: path/to/swagger.yaml
```

## Install Dependency
Install Python dependencies specified by `requirements.txt`
```
pip install -r requirements.txt -t .
```
or install Python dependencies specified by PACKAGE_NAME
```
pip install PACKAGE_NAME -t .
```

## Deploy Package
```
aws cloudformation package \
--template-file <path-to-file>/template.yaml \
--output-template-file <path-to-file>/template-out.yaml \
--s3-bucket <your-s3-bucket-name>

aws cloudformation deploy \
--template-file <path-to-file>/template-out.yaml \
--stack-name <STACK_NAME> \
--capabilities CAPABILITY_IAM
```

## Update Package
Same as deploy. [Versioning is supported by SAM](https://github.com/awslabs/serverless-application-model/releases/tag/1.3.0).

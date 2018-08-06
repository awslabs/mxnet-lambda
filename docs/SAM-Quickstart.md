* In the AWS Region you plan to deploy, make sure you have an existing Amazon S3 bucket in which SAM can create the deployment artifacts.

Else create a new bucket using the following AWS CLI command:

```
aws s3 mb s3://<your-bucket-name> --region <your-bucket-region>
```

- First copy the lit-base template and SAM templates to get started.
```
cp -r lit-base PACKAGE_NAME
cd PACKAGE_NAME
cp ../sam/* .
```

- Before deploying the project to SAM for the first time, you'll need to update some variables in `template.yaml`/`swagger.yaml` (found in `sam/` folder).

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
--template-file <path-to-file>/template.yaml \
--output-template-file <path-to-file>/template-out.yaml \
--s3-bucket <your-s3-bucket-name>

aws cloudformation deploy \
--template-file <path-to-file>/template-out.yaml \
--stack-name <STACK_NAME> \
--capabilities CAPABILITY_IAM
```
 

- Get the URL of the Serverless application that was created

```
aws cloudformation describe-stacks --stack-name <STACK_NAME> | python -c 'import json,sys;obj=json.load(sys.stdin);print obj["Stacks"][0]["Outputs"][0]["OutputValue"];'
```

- Test with POST request

```
wget https://s3.us-east-2.amazonaws.com/baiachen-amazon-ai-work-data/cat.png
curl -H "Content-Type: image/png" -X POST https://MY_URL -T "cat.png"
```
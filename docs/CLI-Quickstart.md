## Quickstart
### Create and deploy package
```
lit-cli create lit-demo
cd lit-demo
lit-cli deploy --role ROLE_ARN
```
AWS provides a managed IAM role and could be created following [this tutorial](https://docs.aws.amazon.com/lambda/latest/dg/with-userapp-walkthrough-custom-events-create-iam-role.html)

Make sure your `ROLE_ARN` is in the format of `arn:aws:iam::[aws_account_number]:role/[role_name]`.

### Invoke your package
```
aws lambda invoke \
--invocation-type RequestResponse \
--function-name lit-demo \
--region us-east-2 \
--log-type Tail \
--payload '{"url": "https://github.com/dmlc/web-data/blob/master/mxnet/doc/tutorials/python/predict_image/cat.jpg?raw=true"}' \
output.json
```
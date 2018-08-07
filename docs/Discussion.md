## Pros & Cons for Serverless Model Serving

There are a few pros and cons using Lambda compared to hosting a server/instance for machine learning model serving:

Pros:

1. It could significantly reduce the cost of serving a well-trained model for inference
2. It is charged by query
3. Effortless and limitless scalability. 

Cons:

1. GPU not yet available
2. 512 MB /tmp limit
3. Slow startup if not frequently used (we can alternatively [keep instance warm](https://github.com/anchen1011/lambda-inference-toolkit/wiki/Keep-it-Warm))
4. Potentially bottlenecked by speed of fetching and loading if the model file is large

Other Features:

1. Decent amortized runtime, but the first execution in a while is time consuming due to Lambda’s “probably start a new instance” feature

## Other Useful Services

[Amazon Sagemaker](https://aws.amazon.com/sagemaker/) is a fully-managed platform that enables developers and data scientists to quickly and easily build, train, and deploy machine learning models at any scale.. 

[AWS SAM-CLI](https://github.com/awslabs/aws-sam-cli) is the AWS CLI tool for managing Serverless applications written with AWS Serverless Application Model (SAM). SAM CLI can be used to test functions locally, start a local API Gateway from a SAM template, validate a SAM template, fetch logs, generate sample payloads for various event sources, and generate a SAM project in your favorite Lambda Runtime.

[Apache MXNet Model Server](https://github.com/awslabs/mxnet-model-server) (MMS) is a flexible and easy to use tool for serving deep learning models exported from [Apache MXNet](http://mxnet.apache.org/) or the Open Neural Network Exchange ([ONNX](http://onnx.ai/)).

All these tools are very amazing, and we are not trying to reinvent the wheel. MXNet-lambda supports packaging, deploying and serving machine learning models in a serverless manner. We don't support training, deploying with server or local Lambda testing. 

For training, please check out Sagemaker. For deploying / model serving, both Sagemaker and MMS are very good resources. For local Lambda testing, SAM-CLI it is highly recommended. 

We are actively providing support/extensions for these tools, but a stable, high performance implementation is prioritized for now.

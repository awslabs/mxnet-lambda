## Sagemaker, SAM and MMS

Sagemaker https://aws.amazon.com/cn/sagemaker/ is a stable AWS official tool to train and deploy (on server) machine learning models. 

SAM-CLI https://github.com/awslabs/aws-sam-cli is a stable AWS Labs official tool that supports local Lambda testing. 

MMS https://github.com/awslabs/mxnet-model-server is an AWS Labs official tool that supports server-based model serving. 

All these tools are very amazing, and we are not trying to reinvent the wheel. We support packing, deploying and serving machine learning models in a serverless manner. We don't support training, deploying with server or local Lambda testing. 

For training, please check out Sagemaker. For deploying / model serving, both Sagemaker and MMS are very good resources. For local Lambda testing, SAM-CLI it is highly recommended. 

We are actively providing support/extensions for these tools, but a stable, high performance implementation is prioritized for now.

## Pros & cons for serverless model serving

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

## Challenges and solutions

On the other hand, it is worth noticing that due to the current Lambda restriction, GPU enabled inference is not yet available. Also, the current implementation supports MxNet based deployment only, while support for other frameworks should also be valuable. 

Considering the tradeoff between implementability and deployability for frameworks, actually the best strategy may not be supporting another framework with another independent implementation. Instead, an ONNX extension to import other frameworks into Serverless Model Server pipeline is more feasible and valuable. 
We support Model Archive v1.0

## Create Lambda Function
```
mkdir PACKAGE_NAME
cd PACKAGE_NAME
cp ../lit-mar/* .
```

## Config Model Archive
### [Option 1] Use lit-cli
```
lit-cli config <model_archive>
```
Where <model_archive> could be either a local file path or url.

### [Option 2] Manual
#### Install Requirements
If `requirements.txt` is provided in MAR
```
pip install requirement.txt -t .
```
Install MXNet if not provided in either `requirement.txt` or MAR package
```
pip install mxnet -t .
```
#### Modify Configuration
Upload model archive if it's local, then change `url_mar` in `config.yaml` to model archive URL.

## Deploy
Deploy Lambda Function with [SAM](SAM-Usage.md)
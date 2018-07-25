If you need a bucket but don't have one, you can 
create new bucket using the following AWS CLI command:

```
aws s3 mb s3://<your-bucket-name> --region <your-bucket-region>
```

## Get Help Messages
`lit-cli --help`

## Get Help Messages of Commands
`lit-cli COMMAND --help`

## Create Package
Usage: `lit-cli create [OPTIONS] PACKAGE_NAME`

&nbsp;&nbsp;&nbsp;&nbsp;  Create base package specified by PACKAGE_NAME

&nbsp;&nbsp;&nbsp;&nbsp;  This command makes a copy of `lit-base` and create `.lit-info.npy`

&nbsp;&nbsp;&nbsp;&nbsp;  Should only run under lambda-inference-toolkit root

&nbsp;&nbsp;&nbsp;&nbsp;  All other commands should run under working dir of your created pkg.

&nbsp;&nbsp;&nbsp;&nbsp;  Working dir could be verified with `pwd` and get `/.../pkg_name`

Options:

&nbsp;&nbsp;&nbsp;&nbsp;  `--help`  Show this message and exit.

## Configure Package [pending for model archive support]
Usage: `lit-cli config [OPTIONS]`

&nbsp;&nbsp;&nbsp;&nbsp;  Service file will simply be copied and renamed into `package_root/model_service.py`

&nbsp;&nbsp;&nbsp;&nbsp;  Model could be configured with ONNX models, MXNet models, and MMS model archives.

&nbsp;&nbsp;&nbsp;&nbsp;  ONNX models could only be local file, and will be exported into MXNet models.

&nbsp;&nbsp;&nbsp;&nbsp;  Params and symbol could be configured in either local file name or online file link. 

&nbsp;&nbsp;&nbsp;&nbsp;  MMS model archives could be configured in either local file name or online file link. 

&nbsp;&nbsp;&nbsp;&nbsp;  If local file name is supplied, it will be uploaded to a S3 bucket

&nbsp;&nbsp;&nbsp;&nbsp;  and the link of the online copy will be used. When model-bucket is supplied, 

&nbsp;&nbsp;&nbsp;&nbsp;  this file will be uploaded to the specified S3 bucket.

Options:

&nbsp;&nbsp;&nbsp;&nbsp;  `--params TEXT`         Model params to load (local file path or url link)

&nbsp;&nbsp;&nbsp;&nbsp;  `--symbol TEXT`         Model symbol to load (local file path or url link)

&nbsp;&nbsp;&nbsp;&nbsp;  `--onnx TEXT`           ONNX model to load (local file path)

&nbsp;&nbsp;&nbsp;&nbsp;  `--model-service TEXT`  Model service that defines inference handler (local file path)

&nbsp;&nbsp;&nbsp;&nbsp;  `--model-bucket TEXT`   S3 bucket for model storage

&nbsp;&nbsp;&nbsp;&nbsp;  `--help`                Show this message and exit.

## Deploy Package
Usage: `lit-cli deploy [OPTIONS]`

&nbsp;&nbsp;&nbsp;&nbsp;  Deploy package to AWS Lambda

Options:

&nbsp;&nbsp;&nbsp;&nbsp;  `--function-name TEXT`      Function name on Lambda Management Console

&nbsp;&nbsp;&nbsp;&nbsp;  `--region TEXT`             AWS region

&nbsp;&nbsp;&nbsp;&nbsp;  `--role TEXT`               AWS IAM role

&nbsp;&nbsp;&nbsp;&nbsp;  `--memory-size TEXT`        Lambda memory size

&nbsp;&nbsp;&nbsp;&nbsp;  `--timeout TEXT`            Lambda TTL

&nbsp;&nbsp;&nbsp;&nbsp;  `--publish / --no-publish`  Publish a new version or not

&nbsp;&nbsp;&nbsp;&nbsp;  `--help`                    Show this message and exit.

## Update Package
Usage: `lit-cli update [OPTIONS]`

&nbsp;&nbsp;&nbsp;&nbsp;  Update package to AWS Lambda

Options:

&nbsp;&nbsp;&nbsp;&nbsp;  `--memory-size TEXT`        Lambda memory size

&nbsp;&nbsp;&nbsp;&nbsp;  `--timeout TEXT`            Lambda TTL

&nbsp;&nbsp;&nbsp;&nbsp;  `--publish / --no-publish`  Publish a new version or not

&nbsp;&nbsp;&nbsp;&nbsp;  `--help`                    Show this message and exit.

## Install Dependency
Usage: `lit-cli install [OPTIONS] PACKAGE_NAME`

&nbsp;&nbsp;&nbsp;&nbsp;  Install Python dependencies specified by PACKAGE_NAME

&nbsp;&nbsp;&nbsp;&nbsp;  This doesn't work with non-Python dependencies (MXNet, OpenCV, ...)

Options:

&nbsp;&nbsp;&nbsp;&nbsp;  `--help`  Show this message and exit.
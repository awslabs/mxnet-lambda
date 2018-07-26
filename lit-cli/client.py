import numpy as np
import click

import os
import shutil
import tempfile
import subprocess
import urllib


def do_install(package_name, requirement=False, target='.'):
    """Install packages locally without external dependency

    Parameters
    ----------
    package_name: string
        package_name or path/to/requirements.txt
    target: string
        the target local path for installation
    requirement: bool
        whether installation is using requirements.txt
    """
    # import pip main robustly against different version of pip and python
    try:
        from pip._internal import main
    except Exception:
        from pip import main
    # install requirement or requirements.txt
    if not requirement:
        main(['install', package_name, '-t', target])
    else:
        main(['install', '-r', package_name, '-t', target])


def download_url(url, target='.'):
    """Download online file

    Parameters
    ----------
    url: string
        url to the file to download
    target: string
        the target local path of the downloaded file
    """
    urllib.urlretrieve(url, target)


def check_existence(filename, path):
    """Check the existence of filename in path

    Parameters
    ----------
    filename: string
        name of file or dir to verify existence
    path: string
        path to verify the existence

    Returns
    -------
    bool: Returns True if exist, False otherwise
    
    Examples
    ----------
    >>> check_existence('mxnet/', '.')
    >>> check_existence('requirements.txt', '.')
    """
    return os.path.exists(os.path.join(path, filename))


@click.group()
def cli():
    """Lambda Inference Toolkit Command Line Client"""
    pass


@click.command()
@click.argument('package_name')
def create(package_name):
    """Create base package specified by PACKAGE_NAME"""
    shutil.copytree('lit-base',package_name)
    np.save(package_name+'/.lit-info.npy',{'package_name':package_name,'role':'','model_bucket':'serverless-server-models'})


@click.command()
@click.argument('package_name')
@click.option('--requirement', '-r', is_flag=True, help='Install from the given requirements file')
def install(package_name, requirement):
    """Install dependencies specified by PACKAGE_NAME"""
    do_install(package_name, requirement)


@click.command()
@click.option('--function-name', default='', help='Function name on Lambda Management Console')
@click.option('--region', default='us-east-2', help='AWS region')
@click.option('--role', default='', help='AWS IAM role')
@click.option('--memory-size', default='1536', help='Lambda memory size')
@click.option('--timeout', default='60', help='Lambda TTL')
@click.option('--publish/--no-publish', default=False, help='Publish a new version or not')
def deploy(function_name, region, role, memory_size, timeout, publish):
    """Deploy package to AWS Lambda"""
    info = np.load('.lit-info.npy').item()
    info['function_name'] = function_name
    if info['function_name'] == '':
        info['function_name'] = info['package_name']
    info['region'] = region
    if role == '' and info['role'] == '':
        raise ValueError('Unspecified IAM role')
    if role != '':
        info['role'] = role
    info['memory_size'] = memory_size
    info['timeout'] = timeout
    subprocess.call('zip -9r lambda_function.zip  * -x *.params *symbol.json', shell=True)
    cmd = 'aws lambda create-function'
    cmd += ' --function-name ' + info['function_name']
    cmd += ' --zip-file fileb://lambda_function.zip'
    cmd += ' --runtime python2.7'
    cmd += ' --region ' + info['region']
    cmd += ' --role ' + info['role']
    cmd += ' --handler lambda_function.lambda_handler'
    cmd += ' --memory-size ' + info['memory_size']
    cmd += ' --timeout ' + info['timeout']
    if publish:
        cmd += ' --publish'
    np.save('.lit-info.npy',info)
    subprocess.call(cmd, shell=True)


@click.command()
@click.option('--memory-size', default=None, help='Lambda memory size')
@click.option('--timeout', default=None, help='Lambda TTL')
@click.option('--publish/--no-publish', default=False, help='Publish a new version or not')
def update(memory_size, timeout, publish):
    """Update package to AWS Lambda"""
    info = np.load('.lit-info.npy').item()
    info['memory_size'] = memory_size or info['memory_size']
    info['timeout'] = timeout or info['timeout']
    subprocess.call('zip -9r lambda_function.zip  *', shell=True)
    cmd = 'aws lambda update-function-configuration'
    cmd += ' --function-name ' + info['function_name']
    cmd += ' --region ' + info['region']
    cmd += ' --memory-size ' + info['memory_size']
    cmd += ' --timeout ' + info['timeout']
    if publish:
        cmd += ' --publish'
    subprocess.call(cmd, shell=True)
    np.save('.lit-info.npy',info)
    subprocess.call('aws lambda update-function-code --region '+info['region']+' --function-name '+info['function_name']+' --zip-file fileb://lambda_function.zip', shell=True)


@click.command()
@click.option('--params', default=None, help="Model params to load (local file path or url link)")
@click.option('--symbol', default=None, help="Model symbol to load (local file path or url link)")
@click.option('--model-service', default=None, help="Model service that defines preprocess, inference, postprocess procedure (local file path)")
@click.option('--model-bucket', default=None, help="S3 bucket for model storage")
def config(params, symbol, model_bucket):
    """
    Cconfigure model PARAMS and SYMBOL in either local file name or online file link.
    If local file name is supplied, it will be uploaded to a S3 bucket and the link of the online copy will be used.
    When model-bucket is supplied, this file will be uploaded to (and during inference loaded from) the specified S3 bucket.
    """
    if '://' not in params or '://' not in symbol:
        if model_bucket == None:
            click.echo("Please specify S3 bucket for model storage")
            return
    info = np.load('.lit-info.npy').item()
    info['model_bucket'] = model_bucket or info['model_bucket']
    np.save('.lit-info.npy',info)
    if model_service != None:
        shutil.copyfile(model_service, 'model_service.py')
    assert(params[-7:] == '.params')
    assert(symbol[-5:] == '.json')
    if '://' not in params:
        subprocess.call("aws s3 cp " + params + " s3://" + info['model_bucket'] + " --grants read=uri=http://acs.amazonaws.com/groups/global/AllUsers", shell=True)
        params = "https://" + info['model_bucket'] + '.s3.amazonaws.com/' + params.split('/')[-1]
    if '://' not in symbol:
        subprocess.call("aws s3 cp " + symbol + " s3://" + info['model_bucket'] + " --grants read=uri=http://acs.amazonaws.com/groups/global/AllUsers", shell=True)
        symbol = "https://" + info['model_bucket'] + '.s3.amazonaws.com/' + symbol.split('/')[-1]
    with open('model_url.py', 'w') as f:
        f.write('url_params = "' + params + '"\nurl_symbol = "' + symbol + '"\n')


# Executed under path/to/lambda/function/package
@click.command()
@click.argument('model_archive')
@click.option('--model-bucket', default=None, help="S3 bucket for model storage")
def use(model_archive, model_bucket):
    """Configure Lambda Function to consume Model Archive
    MODEL_ARCHIVE could be provided either as a url or path to a local model archive
    """
    # check weither it is url
    is_url = "://" in model_archive
    url_mar = None
    if is_url==False and model_bucket==None:
        click.echo("Please specify S3 bucket for model storage")
        return
    # create a tmp path
    dirpath = tempfile.mkdtemp()
    # download if is url
    if is_url:
        download_url(model_archive, os.path.join(dirpath, "tmp.mar"))
        url_mar = model_archive
        model_archive = os.path.join(dirpath, "tmp.mar")
    # unzip
    subprocess.call("unzip " + model_archive + " -d " + dirpath, shell=True)
    # install requirements
    if check_existence('requirements.txt', dirpath):
        do_install(os.path.join(dirpath, 'requirements.txt'), requirement=True, target='.')
    if check_existence('mxnet/', dirpath) == False and check_existence('mxnet/', '.') == False:
        # rollback numpy to 1.13 (avoid problems with the latest version)
        do_install('numpy==1.13.3', requirement=False, target='.')
        do_install('mxnet', requirement=False, target='.')
    # remove temp path
    shutil.rmtree(dirpath)
    if not is_url:
        # upload model_archive
        status = subprocess.call("aws s3 cp " + model_archive + " s3://" + model_bucket + " --grants read=uri=http://acs.amazonaws.com/groups/global/AllUsers", shell=True)
        if status != 0:
            click.echo("Failed to upload model archive to S3.")
            return
        url_mar = "https://" + model_bucket + '.s3.amazonaws.com/' + model_archive.split('/')[-1]
    with open('config.json', 'w') as outfile:
        json.dump({"url_mar": str(url_mar)}, outfile)


cli.add_command(use)
cli.add_command(create)
cli.add_command(install)
cli.add_command(deploy)
cli.add_command(update)
cli.add_command(config)

if __name__ == "__main__":
    cli()

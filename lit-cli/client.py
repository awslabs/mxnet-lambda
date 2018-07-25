import click

import os
import shutil
import tempfile
import subprocess
import urllib
import yaml


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


# Executed under path/to/lambda/function/package
@click.command()
@click.argument('model_archive')
@click.option('--model-bucket', default=None, help="S3 bucket for model storage")
def create(model_archive, model_bucket):
    """Configure Lambda Function to consume Model Archive
    MODEL_ARCHIVE could be provided either as a url or path to a local model archive
    """
    # check weither it is url
    is_url = "://" in model_archive
    url_mar = None
    if is_url and model_bucket==None:
        click.echo("Please specify S3 bucket for model storage")
        return
    # create a tmp path
    dirpath = tempfile.mkdtemp()
    if is_url:
        download_url(model_archive, os.path.join(dirpath, "tmp.mar"))
        url_mar = model_archive
        model_archive = os.path.join(dirpath, "tmp.mar")
    subprocess.call("unzip " + model_archive + " -d " + dirpath, shell=True)
    do_install('pyyaml', requirement=False, target='.')
    if check_existence('requirements.txt', dirpath):
        do_install(os.path.join(dirpath, 'requirements.txt'), requirements=True, target='.')
    if not check_existence('mxnet/', dirpath):
        do_install('mxnet', requirement=False, target='.')
    # remove temp path
    shutil.rmtree(dirpath)
    if not is_url:
        # upload model_archive
        status = subprocess.call("aws s3 cp " + symbol + " s3://" + model_bucket + " --grants read=uri=http://acs.amazonaws.com/groups/global/AllUsers", shell=True)
        if status != 0:
            click.echo("Failed to upload model archive to S3.")
            return
        url_mar = "https://" + model_bucket + '.s3.amazonaws.com/' + model_archive.split('/')[-1]
    with open('config.yaml', 'w') as outfile:
        yaml.dump({"url_mar": str(url_mar)}, outfile, default_flow_style=False)


cli.add_command(create)


if __name__ == "__main__":
    cli()

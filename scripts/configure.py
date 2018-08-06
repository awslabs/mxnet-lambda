import os
import shutil
import tempfile
import subprocess
import urllib
import json
import sys


def do_install(package_name, requirement=False, target='.'):
    """Install packages locally without external dependency

    Parameters
    ----------
    package_name: string
        package_name or path/to/MAR-INF/requirements.txt
    target: string
        the target local path for installation
    requirement: bool
        whether installation is using MAR-INF/requirements.txt
    """
    # import pip main robustly against different version of pip and python
    try:
        from pip._internal import main
    except Exception:
        from pip import main
    # install requirement or MAR-INF/requirements.txt
    if not requirement:
        main(['install', package_name, '-t', target])
    else:
        main(['install', '-r', package_name, '-t', target])


def download_url(url, target):
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
    >>> check_existence('mxnet/', lambda_function_path)
    >>> check_existence('MAR-INF/requirements.txt', lambda_function_path)
    """
    return os.path.exists(os.path.join(path, filename))


def configure(model_archive, lambda_function_path, model_bucket=None):
    """Configure Lambda Function to consume Model Archive
    
    Parameters
    ----------
    model_archive: string
        url or path to the local model archive file
    model_bucket: string
        optional S3 bucket name to upload local model archive file
    """
    # check weither it is url
    is_url = "://" in model_archive
    url_mar = None
    if is_url==False and model_bucket==None:
        raise Exception("Please specify S3 bucket for model storage")
    # create a tmp path
    dirpath = tempfile.mkdtemp()
    # download if is url
    if is_url:
        download_url(model_archive, os.path.join(dirpath, "tmp.mar"))
        url_mar = model_archive
        model_archive = os.path.join(dirpath, "tmp.mar")
    # unzip
    status = subprocess.call(" ".join(["unzip", model_archive, "-d", dirpath]), shell=True)
    if status != 0:
        raise Exception("Failed to unzip model archive. Interrupt.")
    # install requirements
    if check_existence('MAR-INF/requirements.txt', dirpath):
        do_install(os.path.join(dirpath, 'MAR-INF/requirements.txt'), requirement=True, target=lambda_function_path)
    if check_existence('mxnet/', dirpath) == False and check_existence('mxnet/', lambda_function_path) == False:
        # rollback numpy to 1.13 (avoid problems with the latest version)
        do_install('numpy==1.13.3', requirement=False, target=lambda_function_path)
        do_install('mxnet', requirement=False, target=lambda_function_path)
    # remove temp path
    shutil.rmtree(dirpath)
    if not is_url:
        # upload model_archive
        status = subprocess.call(" ".join(["aws s3 cp", model_archive, "s3://", model_bucket, "--grants read=uri=http://acs.amazonaws.com/groups/global/AllUsers"]), shell=True)
        if status != 0:
            raise Exception("Failed to upload model archive to S3. Interrupt.")
        url_mar = "https://" + model_bucket + '.s3.amazonaws.com/' + model_archive.split('/')[-1]
    with open('config.json', 'w') as outfile:
        json.dump({"url_mar": str(url_mar)}, outfile)


if __name__ == "__main__":
    model_archive = sys.argv[1]
    lambda_function_path = sys.argv[2]
    if len(sys.argv == 4):
        model_bucket = sys.argv[3]
    elif len(sys.argv == 3):
        model_bucket = None
    else:
        raise Exception("Expected model_archive lambda_function_path [model_bucket] as arguements")
    configure(model_archive, lambda_function_path, model_bucket)

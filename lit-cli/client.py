import click
import os, shutil
import urllib


def do_install(package_name, target='.', requirement=False):
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
        main(['install'] + package_name + ['-t', target])
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
    >>> check_existence('mxnet', '.')
    >>> check_existence('requirements.txt', '.')
    """
    return os.path.exists(os.path.join(filename, path))


@click.group()
def cli():
    """Entry Point"""
    pass


@click.command()
@click.argument('package_name')
def config(model_archive):
    """Configure Lambda Function to consume mpdel_archive
    MODEL_ARCHIVE could be provided either as a url or
    path to a local model archive"""
    # check weither it is url
    is_url = "://" in model_archive:


cli.add_command(config)

if __name__ == "__main__":
    cli()

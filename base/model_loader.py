import json
import os

import mxnet as mx

import tempfile
import urllib
import time


def load_model(symbol_filename, params_filename):
    """
    Load model checkpoint from file.
    :return: (symbol, arg_params, aux_params)
    symbol : Symbol
        The network configuration.
    arg_params : dict of str to NDArray
        Model parameter, dict of name to NDArray of net's weights.
    aux_params : dict of str to NDArray
        Model parameter, dict of name to NDArray of net's auxiliary states.
    """
    symbol = mx.symbol.load(symbol_filename)
    save_dict = mx.nd.load(params_filename)
    arg_params = {}
    aux_params = {}
    for key, value in save_dict.items():
        tp, name = key.split(':', 1)
        if tp == 'arg':
            arg_params[name] = value
        if tp == 'aux':
            aux_params[name] = value
    return symbol, arg_params, aux_params


def download_url(url, target, retries=2, base_retry_interval=0.01):
    """Download url to a file.

    Parameters
    ----------
    url: string
        url to the file to download
    target: string
        the target local path of the downloaded file
    retries: int
        the max number of retries allowed for urlretrieve
    """
    assert retries >= 1, "Number of retries should be at least 1"

    retry = 0
    while retry < retries:
        try:
            urllib.urlretrieve(url, target)
            return
        except Exception as e:
            retry += 1
            if retry < retries: 
                time.sleep(2 ** retries * base_retry_interval)
            else:
                raise e
    

with open("config.json", "r") as file:
    config = json.load(file)
url_params = config["url_params"]
url_symbol = config["url_symbol"]
url_synset = config["url_synset"]

dirpath = tempfile.mkdtemp()

# download params
params_filename = os.path.join(dirpath, "model-params.params")
download_url(url_params, params_filename)

# download symbol
symbol_filename = os.path.join(dirpath, "model-symbol.json")
download_url(url_symbol, symbol_filename)

# download synset
synset_filename = os.path.join(dirpath, "synset.txt")
download_url(url_synset, synset_filename)

# load model from symbol and params
sym, arg_params, aux_params = load_model(symbol_filename, params_filename)

# load labels from synset
with open(synset_filename, 'r') as file:
    labels = [line.rstrip() for line in file][1:]

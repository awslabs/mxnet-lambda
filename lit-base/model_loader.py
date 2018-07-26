import json
import os

import mxnet as mx

import tempfile
import urllib


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


def download_url(url):
    """Download online file into tmp

    Parameters
    ----------
    url: string
        url to the file to download
        
    Return
    ----------
    filename: string
        full path to the file downloaded
    """
    f_file = tempfile.NamedTemporaryFile(delete=True)
    urlretrieve(url, f_file.name)
    f_file.flush()
    return f_file.name


with open("config.json", "r") as file:
    config = json.load(file)
url_params = config["url_params"]
url_symbol = config["url_symbol"]
url_synset = config["url_synset"]

dirpath = tempfile.mkdtemp()

# download params
params_filename = download_url(url_params)

# download symbol
symbol_filename = download_url(url_symbol)

# download synset
synset_filename = download_url(url_synset)

# load model from symbol and params
sym, arg_params, aux_params = load_model(symbol_filename, params_filename)

# load labels from synset
with open(synset_filename, 'r') as file:
    labels = [line.rstrip() for line in file]

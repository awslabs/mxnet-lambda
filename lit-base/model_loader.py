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


with open("config.json", "r") as file:
    model_url = json.load(file)
url_params = model_url["url_params"]
url_symbol = model_url["url_symbol"]

dirpath = tempfile.mkdtemp()

# download params
params_filename = os.path.join(dirpath, "model-params.params")
download_url(url_params, params_filename)

# download symbol
symbol_filename = os.path.join(dirpath, "model-symbol.json")
download_url(url_symbol, symbol_filename)

# load model from symbol and params
sym, arg_params, aux_params = load_model(symbol_file_name, params_file_name)
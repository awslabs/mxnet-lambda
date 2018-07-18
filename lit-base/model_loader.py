import yaml

import mxnet as mx

import tempfile
from urllib import urlretrieve


# load model
def load_model(s_fname, p_fname):
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
    symbol = mx.symbol.load(s_fname)
    save_dict = mx.nd.load(p_fname)
    arg_params = {}
    aux_params = {}
    for k, v in save_dict.items():
        tp, name = k.split(':', 1)
        if tp == 'arg':
            arg_params[name] = v
        if tp == 'aux':
            aux_params[name] = v
    return symbol, arg_params, aux_params


model_url = yaml.load(open("model_url.yaml", "r"))
url_params = model_url["url_params"]
url_symbol = model_url["url_symbol"]

# download params
f_params_file = tempfile.NamedTemporaryFile(delete=True)
urlretrieve(url_params, f_params_file.name)
f_params_file.flush()
f_params_file_name = f_params_file.name

# download symbol
f_symbol_file = tempfile.NamedTemporaryFile(delete=True)
urlretrieve(url_symbol, f_symbol_file.name)
f_symbol_file.flush()
f_symbol_file_name = f_symbol_file.name

# load model from symbol and params
sym, arg_params, aux_params = load_model(f_symbol_file_name, f_params_file.name)

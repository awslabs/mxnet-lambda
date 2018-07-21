from setuptools import setup
import platform

requirements = ['Click']

# Enable Cu90 only when using linux with cuda enabled
gpu_platform = False
if platform.system().lower() == 'linux':
    try:
        # Check if CUDA is installed
        cuda = ctypes.cdll.LoadLibrary('libcudart.so')
        deviceCount = ctypes.c_int()
        # get the number of supported GpUs
        cuda.cudaGetDeviceCount(ctypes.byref(deviceCount))
        if deviceCount.value > 0:
            gpu_platform = True
    except Exception as e:
        gpu_platform = False
if gpu_platform:
    requirements = ['mxnet-cu90mkl>=1.2'] + requirements
else:
    requirements = ['mxnet-mkl>=1.2'] + requirements

setup(
    name="lit-cli",
    version='0.1',
    py_modules=['client'],
    install_requires=requirements,
    entry_points='''
        [console_scripts]
        lit-cli=client:cli
    ''',
)

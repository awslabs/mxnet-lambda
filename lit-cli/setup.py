from setuptools import setup
import platform

setup(
    name="lit-cli",
    version='0.1',
    py_modules=['client'],
    install_requires=['Click', 'numpy'],
    entry_points='''
        [console_scripts]
        lit-cli=client:cli
    ''',
)

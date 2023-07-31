from setuptools import setup, find_packages
from codecs import open
from os import path
here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='messagemedia-messages-sdk',
    version='2.1.2',
    description='The MessageMedia Messages API provides a number of endpoints for building powerful two-way messaging applications.',
    long_description_content_type="text/markdown",
    long_description=long_description,
    author='MessageMedia Developers',
    author_email='developers@messagemedia.com',
    url='https://developers.messagemedia.com',
    packages=find_packages(),
    install_requires=[
        'requests>=2.28.2, <3.0',
        'jsonpickle>=3.0.1, <4.0',
        'cachecontrol>=0.12.11, <1.0',
        'python-dateutil>=2.8.2, <3.0',
        'responses>=0.22.0, <1.0',
        'urllib3>=1.26.14, <2.0',
        'setuptools>=67.2.0, <68'
    ]
)

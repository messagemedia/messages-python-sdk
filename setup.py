from setuptools import setup, find_packages
from codecs import open
from os import path
here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='messagemedia-messages-sdk',
    version='2.1.0',
    description='The MessageMedia Messages API provides a number of endpoints for building powerful two-way messaging applications.',
    long_description_content_type="text/markdown",
    long_description=long_description,
    author='MessageMedia Developers',
    author_email='developers@messagemedia.com',
    url='https://developers.messagemedia.com',
    packages=find_packages(),
    install_requires=[
        'requests>=2.9.1, <3.0',
        'jsonpickle>=0.7.1, <1.0',
        'cachecontrol>=0.11.7, <1.0',
        'python-dateutil>=2.5.3, <3.0'
    ]
)

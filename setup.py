from setuptools import setup, find_packages

# Try to convert markdown README to rst format for PyPI.
try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except(IOError, ImportError):
    long_description = open('README.md').read()

setup(
    name='messagemedia_messages_sdk',
    version='1.1.0',
    description='The MessageMedia Messages API provides a number of endpoints for building powerful two-way messaging '
                'applications.',
    long_description=long_description,
    author='MessageMedia Developers',
    author_email='developers@messagemedia.com',
    url='https://developers.messagemedia.com/',
    download_url='https://github.com/messagemedia/messages-python-sdk',
    license='Apache License 2.0',
    packages=find_packages(),
    install_requires=[
        'requests>=2.9.1, <3.0',
        'jsonpickle>=0.7.1, <1.0',
        'cachecontrol>=0.11.7, <1.0',
        'python-dateutil>=2.5.3, <3.0'
    ],
    tests_require=[
        'nose>=1.3.7'
    ],
    test_suite='nose.collector'
)

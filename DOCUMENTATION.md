# MessageMedia Messages Python SDK
[![Travis Build Status](https://api.travis-ci.org/messagemedia/messages-python-sdk.svg?branch=master)](https://travis-ci.org/messagemedia/messages-python-sdk)
[![PyPI](https://img.shields.io/pypi/v/messagemedia-messages-sdk.svg)](https://pypi.python.org/pypi/messagemedia-messages-sdk)

The MessageMedia Messages API provides a number of endpoints for building powerful two-way messaging applications.

## Getting started

You must have Python ```2 >=2.7``` or Python ```3 >=3.2``` installed on your system to install and run this SDK. This SDK package depends on other Python packages like nose, jsonpickle etc. 

##### Using PIP Dependency manager
Install PIP Dependency Manager by following steps at [https://pip.pypa.io/en/stable/installing/](https://pip.pypa.io/en/stable/installing/).

Python and PIP executables should be defined in your PATH. Open command prompt and type ```pip --version```.
This should display the version of the PIP Dependency Manager installed if your installation was successful and the paths are properly defined.

* Using the command line, navigate to the directory you wish to install to.
* Run the command ```pip install messagemedia-messages-sdk```. This will install the SDK and all it's required dependencies.

## Example Usage

The following section explains how to use the MessageMediaMessages SDK package in a new project.

### 1. Open Project in an IDE

Open up a Python IDE like PyCharm. The basic workflow presented here is also applicable if you prefer using a different editor or IDE.

![Open project in PyCharm - Step 1](https://apidocs.io/illustration/python?step=pyCharm)

Click on ```Open``` in PyCharm to browse to your generated SDK directory and then click ```OK```.

![Open project in PyCharm - Step 2](https://apidocs.io/illustration/python?step=openProject0&workspaceFolder=MessageMediaMessages-Python)     

The project files will be displayed in the side bar as follows:

![Open project in PyCharm - Step 3](https://apidocs.io/illustration/python?step=openProject1&workspaceFolder=MessageMediaMessages-Python&projectName=message_media_messages)     

### 2. Add a new Test Project

Create a new directory by right clicking on the solution name as shown below:

![Add a new project in PyCharm - Step 1](https://apidocs.io/illustration/python?step=createDirectory&workspaceFolder=MessageMediaMessages-Python&projectName=message_media_messages)

Name the directory as "test"

![Add a new project in PyCharm - Step 2](https://apidocs.io/illustration/python?step=nameDirectory)
   
Add a python file to this project with the name "testsdk"

![Add a new project in PyCharm - Step 3](https://apidocs.io/illustration/python?step=createFile&workspaceFolder=MessageMediaMessages-Python&projectName=message_media_messages)

Name it "testsdk"

![Add a new project in PyCharm - Step 4](https://apidocs.io/illustration/python?step=nameFile)

In your python file you will be required to import the generated python library using the following code lines

```Python
from message_media_messages.message_media_messages_client import MessageMediaMessagesClient
```

![Add a new project in PyCharm - Step 4](https://apidocs.io/illustration/python?step=projectFiles&workspaceFolder=MessageMediaMessages-Python&libraryName=message_media_messages.message_media_messages_client&projectName=message_media_messages&className=MessageMediaMessagesClient)

After this you can write code to instantiate an API client object, get a controller object and  make API calls. Sample code is given in the subsequent sections.

### 3. Run the Test Project

To run the file within your test project, right click on your Python file inside your Test project and click on ```Run```

![Run Test Project - Step 1](https://apidocs.io/illustration/python?step=runProject&workspaceFolder=MessageMediaMessages-Python&libraryName=message_media_messages.message_media_messages_client&projectName=message_media_messages&className=MessageMediaMessagesClient)

## Initialization

### Authentication
In order to setup authentication and initialization of the API client, you need the following information.

| Parameter | Description |
|-----------|-------------|
| basicAuthUserName | The username to use with basic authentication |
| basicAuthPassword | The password to use with basic authentication |
| hmacAuthUserName | The username to use with HMAC authentication |
| hmacAuthPassword | The password to use with HMAC authentication |



API client can be initialized as following.

```python
# Configuration parameters and credentials
auth_user_name = 'basic_auth_user_name' # The username to use with basic authentication
auth_password = 'basic_auth_password' # The password to use with basic authentication

client = MessageMediaMessagesClient(auth_user_name, auth_password)

# If you wish to use HMAC authentication, you simply specify it as the last parameter

client = MessageMediaMessagesClient(auth_user_name, auth_password, true)
```

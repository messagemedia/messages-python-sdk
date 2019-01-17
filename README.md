# Getting started

The MessageMedia Messages API provides a number of endpoints for building powerful two-way messaging applications.

## How to Build


You must have Python ```2 >=2.7.9``` or Python ```3 >=3.4``` installed on your system to install and run this SDK. This SDK package depends on other Python packages like nose, jsonpickle etc. 
These dependencies are defined in the ```requirements.txt``` file that comes with the SDK.
To resolve these dependencies, you can use the PIP Dependency manager. Install it by following steps at [https://pip.pypa.io/en/stable/installing/](https://pip.pypa.io/en/stable/installing/).

Python and PIP executables should be defined in your PATH. Open command prompt and type ```pip --version```.
This should display the version of the PIP Dependency Manager installed if your installation was successful and the paths are properly defined.

* Using command line, navigate to the directory containing the generated files (including ```requirements.txt```) for the SDK.
* Run the command ```pip install -r requirements.txt```. This should install all the required dependencies.

![Building SDK - Step 1](https://apidocs.io/illustration/python?step=installDependencies&workspaceFolder=MessageMediaMessages-Python)


## How to Use

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


## How to Test

You can test the generated SDK and the server with automatically generated test
cases. unittest is used as the testing framework and nose is used as the test
runner. You can run the tests as follows:

  1. From terminal/cmd navigate to the root directory of the SDK.
  2. Invoke ```pip install -r test-requirements.txt```
  3. Invoke ```nosetests```

## Initialization

### 

API client can be initialized as following.

```python

client = MessageMediaMessagesClient()
```



# Class Reference

## <a name="list_of_controllers"></a>List of Controllers

* [MessagesController](#messages_controller)
* [DeliveryReportsController](#delivery_reports_controller)
* [RepliesController](#replies_controller)

## <a name="messages_controller"></a>![Class: ](https://apidocs.io/img/class.png ".MessagesController") MessagesController

### Get controller instance

An instance of the ``` MessagesController ``` class can be accessed from the API Client.

```python
 messages_controller = client.messages
```

### <a name="get_message_status"></a>![Method: ](https://apidocs.io/img/method.png ".MessagesController.get_message_status") get_message_status

> Retrieve the current status of a message using the message ID returned in the send messages end point.
> A successful request to the get message status endpoint will return a response body as follows:
> ```json
> {
>     "format": "SMS",
>     "content": "My first message!",
>     "metadata": {
>         "key1": "value1",
>         "key2": "value2"
>     },
>     "message_id": "877c19ef-fa2e-4cec-827a-e1df9b5509f7",
>     "callback_url": "https://my.callback.url.com",
>     "delivery_report": true,
>     "destination_number": "+61401760575",
>     "scheduled": "2016-11-03T11:49:02.807Z",
>     "source_number": "+61491570157",
>     "source_number_type": "INTERNATIONAL",
>     "message_expiry_timestamp": "2016-11-03T11:49:02.807Z",
>     "status": "enroute"
> }
> ```
> The status property of the response indicates the current status of the message. See the Delivery
> Reports section of this documentation for more information on message statues.
> *Note: If an invalid or non existent message ID parameter is specified in the request, then
> a HTTP 404 Not Found response will be returned*

```python
def get_message_status(self,
                           message_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| messageId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
message_id = 'messageId'

result = messages_controller.get_message_status(message_id)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 404 | Resource not found |




### <a name="send_messages"></a>![Method: ](https://apidocs.io/img/method.png ".MessagesController.send_messages") send_messages

> Submit one or more (up to 100 per request) SMS, MMS or text to voice messages for delivery.
> The most basic message has the following structure:
> ```json
> {
>     "messages": [
>         {
>             "content": "My first message!",
>             "destination_number": "+61491570156"
>         }
>     ]
> }
> ```
> More advanced delivery features can be specified by setting the following properties in a message:
> - ```callback_url``` A URL can be included with each message to which Webhooks will be pushed to
>   via a HTTP POST request. Webhooks will be sent if and when the status of the message changes as
>   it is processed (if the delivery report property of the request is set to ```true```) and when replies
>   are received. Specifying a callback URL is optional.
> - ```content``` The content of the message. This can be a Unicode string, up to 5,000 characters long.
>   Message content is required.
> - ```delivery_report``` Delivery reports can be requested with each message. If delivery reports are requested, a webhook
>   will be submitted to the ```callback_url``` property specified for the message (or to the webhooks)
>   specified for the account every time the status of the message changes as it is processed. The
>   current status of the message can also be retrieved via the Delivery Reports endpoint of the
>   Messages API. Delivery reports are optional and by default will not be requested.
> - ```destination_number``` The destination number the message should be delivered to. This should be specified in E.164
>   international format. For information on E.164, please refer to http://en.wikipedia.org/wiki/E.164.
>   A destination number is required.
> - ```format``` The format specifies which format the message will be sent as, ```SMS``` (text message), ```MMS``` (multimedia message)
>   or ```TTS``` (text to speech). With ```TTS``` format, we will call the destination number and read out the
>   message using a computer generated voice. Specifying a format is optional, by default ```SMS``` will be used.
> - ```source_number``` A source number may be specified for the message, this will be the number that
>   the message appears from on the handset. By default this feature is _not_ available and will be ignored
>   in the request. Please contact <support@messagemedia.com> for more information. Specifying a source
>   number is optional and a by default a source number will be assigned to the message.
> - ```media``` The media is used to specify the url of the media file that you are trying to send. Supported file formats include png, jpeg and gif. ```format``` parameter must be set to ```MMS``` for this to work.
> - ```subject``` The subject field is used to denote subject of the MMS message and has a maximum size of 64 characters long. Specifying a subject is optional.
> - ```source_number_type``` If a source number is specified, the type of source number may also be
>   specified. This is recommended when using a source address type that is not an internationally
>   formatted number, available options are ```INTERNATIONAL```, ```ALPHANUMERIC``` or ```SHORTCODE```. Specifying a
>   source number type is only valid when the ```source_number``` parameter is specified and is optional.
>   If a source number is specified and no source number type is specified, the source number type will be
>   inferred from the source number, however this may be inaccurate.
> - ```scheduled``` A message can be scheduled for delivery in the future by setting the scheduled property.
>   The scheduled property expects a date time specified in ISO 8601 format. The scheduled time must be
>   provided in UTC and is optional. If no scheduled property is set, the message will be delivered immediately.
> - ```message_expiry_timestamp``` A message expiry timestamp can be provided to specify the latest time
>   at which the message should be delivered. If the message cannot be delivered before the specified
>   message expiry timestamp elapses, the message will be discarded. Specifying a message expiry 
>   timestamp is optional.
> - ```metadata``` Metadata can be included with the message which will then be included with any delivery
>   reports or replies matched to the message. This can be used to create powerful two-way messaging
>   applications without having to store persistent data in the application. Up to 10 key / value metadata data
>   pairs can be specified in a message. Each key can be up to 100 characters long, and each value up to 
>   256 characters long. Specifying metadata for a message is optional.
> The response body of a successful POST request to the messages endpoint will include a ```messages```
> property which contains a list of all messages submitted. The list of messages submitted will
> reflect the list of messages included in the request, but each message will also contain two new
> properties, ```message_id``` and ```status```. The returned message ID will be a 36 character UUID
> which can be used to check the status of the message via the Get Message Status endpoint. The status
> of the message which reflect the status of the message at submission time which will always be
> ```queued```. See the Delivery Reports section of this documentation for more information on message
> statues.
> *Note: when sending multiple messages in a request, all messages must be valid for the request to be successful.
> If any messages in the request are invalid, no messages will be sent.*

```python
def send_messages(self,
                      body)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| body |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
body = SendMessagesRequest()

result = messages_controller.send_messages(body)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Unexpected error in API call. See HTTP response body for details. |




### <a name="cancel_scheduled_message"></a>![Method: ](https://apidocs.io/img/method.png ".MessagesController.cancel_scheduled_message") cancel_scheduled_message

> Cancel a scheduled message that has not yet been delivered.
> A scheduled message can be cancelled by updating the status of a message from ```scheduled```
> to ```cancelled```. This is done by submitting a PUT request to the messages endpoint using
> the message ID as a parameter (the same endpoint used above to retrieve the status of a message).
> The body of the request simply needs to contain a ```status``` property with the value set
> to ```cancelled```.
> ```json
> {
>     "status": "cancelled"
> }
> ```
> *Note: Only messages with a status of scheduled can be cancelled. If an invalid or non existent
> message ID parameter is specified in the request, then a HTTP 404 Not Found response will be 
> returned*

```python
def cancel_scheduled_message(self,
                                 message_id,
                                 body)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| messageId |  ``` Required ```  | TODO: Add a parameter description |
| body |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
message_id = 'messageId'
body = CancelScheduledMessageRequest()

result = messages_controller.cancel_scheduled_message(message_id, body)

```


### <a name="check_credits_remaining"></a>![Method: ](https://apidocs.io/img/method.png ".MessagesController.check_credits_remaining") check_credits_remaining

> TODO: Add a method description

```python
def check_credits_remaining(self)
```

#### Example Usage

```python

result = messages_controller.check_credits_remaining()

```


[Back to List of Controllers](#list_of_controllers)

## <a name="delivery_reports_controller"></a>![Class: ](https://apidocs.io/img/class.png ".DeliveryReportsController") DeliveryReportsController

### Get controller instance

An instance of the ``` DeliveryReportsController ``` class can be accessed from the API Client.

```python
 delivery_reports_controller = client.delivery_reports
```

### <a name="check_delivery_reports"></a>![Method: ](https://apidocs.io/img/method.png ".DeliveryReportsController.check_delivery_reports") check_delivery_reports

> Check for any delivery reports that have been received.
> Delivery reports are a notification of the change in status of a message as it is being processed.
> Each request to the check delivery reports endpoint will return any delivery reports received that
> have not yet been confirmed using the confirm delivery reports endpoint. A response from the check
> delivery reports endpoint will have the following structure:
> ```json
> {
>     "delivery_reports": [
>         {
>             "callback_url": "https://my.callback.url.com",
>             "delivery_report_id": "01e1fa0a-6e27-4945-9cdb-18644b4de043",
>             "source_number": "+61491570157",
>             "date_received": "2017-05-20T06:30:37.642Z",
>             "status": "enroute",
>             "delay": 0,
>             "submitted_date": "2017-05-20T06:30:37.639Z",
>             "original_text": "My first message!",
>             "message_id": "d781dcab-d9d8-4fb2-9e03-872f07ae94ba",
>             "vendor_account_id": {
>                 "vendor_id": "MessageMedia",
>                 "account_id": "MyAccount"
>             },
>             "metadata": {
>                 "key1": "value1",
>                 "key2": "value2"
>             }
>         },
>         {
>             "callback_url": "https://my.callback.url.com",
>             "delivery_report_id": "0edf9022-7ccc-43e6-acab-480e93e98c1b",
>             "source_number": "+61491570158",
>             "date_received": "2017-05-21T01:46:42.579Z",
>             "status": "enroute",
>             "delay": 0,
>             "submitted_date": "2017-05-21T01:46:42.574Z",
>             "original_text": "My second message!",
>             "message_id": "fbb3b3f5-b702-4d8b-ab44-65b2ee39a281",
>             "vendor_account_id": {
>                 "vendor_id": "MessageMedia",
>                 "account_id": "MyAccount"
>             },
>             "metadata": {
>                 "key1": "value1",
>                 "key2": "value2"
>             }
>         }
>     ]
> }
> ```
> Each delivery report will contain details about the message, including any metadata specified
> and the new status of the message (as each delivery report indicates a change in status of a
> message) and the timestamp at which the status changed. Every delivery report will have a 
> unique delivery report ID for use with the confirm delivery reports endpoint.
> *Note: The source number and destination number properties in a delivery report are the inverse of
> those specified in the message that the delivery report relates to. The source number of the
> delivery report is the destination number of the original message.*
> Subsequent requests to the check delivery reports endpoint will return the same delivery reports
> and a maximum of 100 delivery reports will be returned in each request. Applications should use the
> confirm delivery reports endpoint in the following pattern so that delivery reports that have been
> processed are no longer returned in subsequent check delivery reports requests.
> 1. Call check delivery reports endpoint
> 2. Process each delivery report
> 3. Confirm all processed delivery reports using the confirm delivery reports endpoint
> *Note: It is recommended to use the Webhooks feature to receive reply messages rather than
> polling the check delivery reports endpoint.*

```python
def check_delivery_reports(self)
```

#### Example Usage

```python

result = delivery_reports_controller.check_delivery_reports()

```


### <a name="confirm_delivery_reports_as_received"></a>![Method: ](https://apidocs.io/img/method.png ".DeliveryReportsController.confirm_delivery_reports_as_received") confirm_delivery_reports_as_received

> Mark a delivery report as confirmed so it is no longer return in check delivery reports requests.
> The confirm delivery reports endpoint is intended to be used in conjunction with the check delivery
> reports endpoint to allow for robust processing of delivery reports. Once one or more delivery
> reports have been processed, they can then be confirmed using the confirm delivery reports endpoint so they
> are no longer returned in subsequent check delivery reports requests.
> The confirm delivery reports endpoint takes a list of delivery report IDs as follows:
> ```json
> {
>     "delivery_report_ids": [
>         "011dcead-6988-4ad6-a1c7-6b6c68ea628d",
>         "3487b3fa-6586-4979-a233-2d1b095c7718",
>         "ba28e94b-c83d-4759-98e7-ff9c7edb87a1"
>     ]
> }
> ```
> Up to 100 delivery reports can be confirmed in a single confirm delivery reports request.

```python
def confirm_delivery_reports_as_received(self,
                                             body)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| body |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
body = ConfirmDeliveryReportsAsReceivedRequest()

result = delivery_reports_controller.confirm_delivery_reports_as_received(body)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="replies_controller"></a>![Class: ](https://apidocs.io/img/class.png ".RepliesController") RepliesController

### Get controller instance

An instance of the ``` RepliesController ``` class can be accessed from the API Client.

```python
 replies_controller = client.replies
```

### <a name="check_replies"></a>![Method: ](https://apidocs.io/img/method.png ".RepliesController.check_replies") check_replies

> Check for any replies that have been received.
> Replies are messages that have been sent from a handset in response to a message sent by an
> application or messages that have been sent from a handset to a inbound number associated with
> an account, known as a dedicated inbound number (contact <support@messagemedia.com> for more
> information on dedicated inbound numbers).
> Each request to the check replies endpoint will return any replies received that have not yet
> been confirmed using the confirm replies endpoint. A response from the check replies endpoint
> will have the following structure:
> ```json
> {
>     "replies": [
>         {
>             "metadata": {
>                 "key1": "value1",
>                 "key2": "value2"
>             },
>             "message_id": "877c19ef-fa2e-4cec-827a-e1df9b5509f7",
>             "reply_id": "a175e797-2b54-468b-9850-41a3eab32f74",
>             "date_received": "2016-12-07T08:43:00.850Z",
>             "callback_url": "https://my.callback.url.com",
>             "destination_number": "+61491570156",
>             "source_number": "+61491570157",
>             "vendor_account_id": {
>                 "vendor_id": "MessageMedia",
>                 "account_id": "MyAccount"
>             },
>             "content": "My first reply!"
>         },
>         {
>             "metadata": {
>                 "key1": "value1",
>                 "key2": "value2"
>             },
>             "message_id": "8f2f5927-2e16-4f1c-bd43-47dbe2a77ae4",
>             "reply_id": "3d8d53d8-01d3-45dd-8cfa-4dfc81600f7f",
>             "date_received": "2016-12-07T08:43:00.850Z",
>             "callback_url": "https://my.callback.url.com",
>             "destination_number": "+61491570157",
>             "source_number": "+61491570158",
>             "vendor_account_id": {
>                 "vendor_id": "MessageMedia",
>                 "account_id": "MyAccount"
>             },
>             "content": "My second reply!"
>         }
>     ]
> }
> ```
> Each reply will contain details about the reply message, as well as details of the message the reply was sent
> in response to, including any metadata specified. Every reply will have a reply ID to be used with the
> confirm replies endpoint.
> *Note: The source number and destination number properties in a reply are the inverse of those
> specified in the message the reply is in response to. The source number of the reply message is the
> same as the destination number of the original message, and the destination number of the reply
> message is the same as the source number of the original message. If a source number
> wasn't specified in the original message, then the destination number property will not be present
> in the reply message.*
> Subsequent requests to the check replies endpoint will return the same reply messages and a maximum
> of 100 replies will be returned in each request. Applications should use the confirm replies endpoint
> in the following pattern so that replies that have been processed are no longer returned in
> subsequent check replies requests.
> 1. Call check replies endpoint
> 2. Process each reply message
> 3. Confirm all processed reply messages using the confirm replies endpoint
> *Note: It is recommended to use the Webhooks feature to receive reply messages rather than polling
> the check replies endpoint.*

```python
def check_replies(self)
```

#### Example Usage

```python

result = replies_controller.check_replies()

```


### <a name="confirm_replies_as_received"></a>![Method: ](https://apidocs.io/img/method.png ".RepliesController.confirm_replies_as_received") confirm_replies_as_received

> Mark a reply message as confirmed so it is no longer returned in check replies requests.
> The confirm replies endpoint is intended to be used in conjunction with the check replies endpoint
> to allow for robust processing of reply messages. Once one or more reply messages have been processed
> they can then be confirmed using the confirm replies endpoint so they are no longer returned in
> subsequent check replies requests.
> The confirm replies endpoint takes a list of reply IDs as follows:
> ```json
> {
>     "reply_ids": [
>         "011dcead-6988-4ad6-a1c7-6b6c68ea628d",
>         "3487b3fa-6586-4979-a233-2d1b095c7718",
>         "ba28e94b-c83d-4759-98e7-ff9c7edb87a1"
>     ]
> }
> ```
> Up to 100 replies can be confirmed in a single confirm replies request.

```python
def confirm_replies_as_received(self,
                                    body)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| body |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
body = ConfirmRepliesAsReceivedRequest()

result = replies_controller.confirm_replies_as_received(body)

```


[Back to List of Controllers](#list_of_controllers)




from message_media_messages.message_media_messages_client import MessageMediaMessagesClient
from message_media_messages.models.send_messages_request import SendMessagesRequest
from message_media_messages.models.message import Message
from message_media_messages.models.format_enum import FormatEnum
from message_media_messages.models.source_number_type_enum import SourceNumberTypeEnum
from message_media_messages.models.status_enum import StatusEnum
from message_media_messages.exceptions.send_messages_400_response_exception import SendMessages400ResponseException
from message_media_messages.exceptions.api_exception import APIException
import dateutil.parser
import jsonpickle

auth_user_name = 'API_KEY'
auth_password = 'API_SECRET'
use_hmac_authentication = False

client = MessageMediaMessagesClient(auth_user_name, auth_password, use_hmac_authentication)

messages_controller = client.messages
body = SendMessagesRequest()
body.messages = []

body.messages.append(Message())
body.messages[0].content = 'My first message'
body.messages[0].destination_number = '+61491570156'

try:
    result = messages_controller.send_messages(body)
    print(result)
except SendMessages400ResponseException as e:
    print(e)
except APIException as e:
    print(e)

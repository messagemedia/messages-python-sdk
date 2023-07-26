import traceback
from  message_media_messages.message_media_messages_client import MessageMediaMessagesClient
from message_media_messages.models.send_messages_request import SendMessagesRequest
from message_media_messages.models.message import Message
from message_media_messages.exceptions.send_messages_400_response_exception import SendMessages400ResponseException
from message_media_messages.exceptions.api_exception import APIException




auth_user_name = 'PreAnngQ4Bn53po8D0yw'
auth_password = '31LVO5ueiMrQ94RFjTVVtHrCdqNPIn'
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
    print(str(e))
    traceback.print_exc()
except APIException as e:
    print(str(e))
    print("Request details:")
    print("Parameters:", e.context.request.parameters)
    print("Query URL:", e.context.request.query_url)
    print("Headers:", e.context.request.headers)
    print("Response details:")
    print("Status code:", e.context.response.status_code)
    print("Headers:", e.context.response.headers)
    print("Raw body:", e.context.response.raw_body)
    traceback.print_exc()

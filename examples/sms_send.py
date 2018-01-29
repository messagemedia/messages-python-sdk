# Configuration parameters and credentials
from message_media_messages.message_media_messages_client import MessageMediaMessagesClient
import json

auth_user_name = 'YOUR_API_KEY' # The username to use with basic authentication
auth_password = 'YOUR_API_SECRET' # The password to use with basic authentication

client = MessageMediaMessagesClient(auth_user_name, auth_password)

messages_client = client.messages

body_value = '''{
    "messages":[
        {
            "content":"My first message",
            "destination_number":"YOUR_MOBILE_NUMBER"
        }
    ]
}'''

body = json.loads(body_value)

result = messages_client.create_send_messages(body)

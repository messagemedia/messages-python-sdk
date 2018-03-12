# Configuration parameters and credentials
from message_media_messages.message_media_messages_client import MessageMediaMessagesClient
import sys
import json

auth_user_name = 'YOUR_API_KEY' # The username to use with basic authentication
auth_password = 'YOUR_API_SECRET' # The password to use with basic authentication

client = MessageMediaMessagesClient(auth_user_name, auth_password)

messages_client = client.messages

message_id = 'messageId'

result = messages_client.get_message_status(message_id)

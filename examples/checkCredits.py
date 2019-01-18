# Configuration parameters and credentials
from message_media_messages.message_media_messages_client import MessageMediaMessagesClient
import sys
import json

auth_user_name = 'YOUR_API_KEY' # The username to use with basic/HMAC authentication
auth_password = 'YOUR_API_SECRET' # The password to use with basic/HMAC authentication
use_hmac_authentication = False # Change to True if you are using HMAC keys

client = MessageMediaMessagesClient(auth_user_name, auth_password, use_hmac_authentication)

delivery_reports_client = client.delivery_reports

result = delivery_reports_client.get_check_delivery_reports()

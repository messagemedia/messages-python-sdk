# -*- coding: utf-8 -*-

"""
    message_media_messages

    This file was automatically generated for MessageMedia by APIMATIC v2.0 ( https://apimatic.io ).
"""

import hashlib
import unittest
from datetime import datetime
from time import mktime
from wsgiref.handlers import format_date_time
from message_media_messages.exceptions.api_exception import APIException
from tests.testConfiguration import TestConfiguration
from message_media_messages.http.auth.auth_manager import AuthManager
from message_media_messages.configuration import Configuration
from message_media_messages.api_helper import APIHelper
from message_media_messages.message_media_messages_client import MessageMediaMessagesClient
from message_media_messages.models.send_messages_request import SendMessagesRequest
from message_media_messages.models.message import Message
from message_media_messages.models.format_enum import FormatEnum
import urllib3


class Test_MM_send_message(unittest.TestCase):
    """@classmethod
    def setUpClass(cls):"""

    # Testing successful message to MM endpoint
    def test_successful_message_to_endpoint(self):
        use_hmac_authentication = True
        body = TestConfiguration.create_body()

        client = MessageMediaMessagesClient(use_hmac_authentication)
        messages_controller = client.messages

        result = messages_controller.send_messages(body)

        self.assertIsNotNone(result)

    # Testing unsupported request raises exception
    def test_unsuccessful_request_raises_exception(self):
        auth_user_name = 'Rubbish'
        auth_password = 'Random'
        use_hmac_authentication = True
        body = TestConfiguration.create_body()

        client = MessageMediaMessagesClient(auth_user_name, auth_password, use_hmac_authentication)
        messages_controller = client.messages

        with self.assertRaises(APIException) as context_manager:
            messages_controller.send_messages(body)
        raised_exception = context_manager.exception
        self.assertIsNotNone(raised_exception)

    # Testing get message endpoint
    def test_get_message_endpoint(self):
        actual_id = 'Enter Your Id'
        use_hmac_authentication = True

        client = MessageMediaMessagesClient(use_hmac_authentication)
        messages_controller = client.messages

        result = messages_controller.get_message_status(actual_id)
        expected_id = result.message_id
        assert expected_id == actual_id

# -*- coding: utf-8 -*-

"""
    message_media_messages

    This file was automatically generated for MessageMedia by APIMATIC v2.0 ( https://apimatic.io ).
"""

import unittest
from message_media_messages.exceptions.api_exception import APIException
from tests.test_util import TestUtility
from message_media_messages.message_media_messages_client import MessageMediaMessagesClient



class TestMessages(unittest.TestCase):

    # Testing successful message to MM endpoint
    def test_successful_message_to_endpoint(self):
        use_hmac_authentication = True
        body = TestUtility.create_body()

        client = MessageMediaMessagesClient(use_hmac_authentication)
        messages_controller = client.messages

        result = messages_controller.send_messages(body)

        self.assertIsNotNone(result)

    # Testing unsupported request raises exception
    def test_unsuccessful_request_raises_exception(self):
        auth_user_name = 'Rubbish'
        auth_password = 'Random'
        use_hmac_authentication = True
        body = TestUtility.create_body()

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

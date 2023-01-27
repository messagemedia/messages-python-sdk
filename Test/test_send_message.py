# -*- coding: utf-8 -*-

"""
    message_media_messages

    This file was automatically generated for MessageMedia by APIMATIC v2.0 ( https://apimatic.io ).
"""

import hashlib
import unittest
from message_media_messages.http.auth.auth_manager import AuthManager
from message_media_messages.configuration import Configuration
from message_media_messages.api_helper import APIHelper
from message_media_messages.message_media_messages_client import MessageMediaMessagesClient
from message_media_messages.models.send_messages_request import SendMessagesRequest
from message_media_messages.models.message import Message
from message_media_messages.models.format_enum import FormatEnum
import urllib3
import os


class test_send_message(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.body = SendMessagesRequest()
        cls.body.messages = []

        cls.body.messages.append(Message())
        cls.body.messages[0].content = 'My Test message'
        cls.body.messages[0].destination_number = 'Number'
        cls.body.messages[0].format = FormatEnum.SMS

        cls._url_path = '/v1/messages'
        cls._query_builder = Configuration.base_uri
        cls._query_builder += cls._url_path
        cls._query_url = APIHelper.clean_url(cls._query_builder)

        cls._headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json; charset=utf-8'
        }

    # Testing successful message to MM endpoint
    def test_successful_message_to_endpoint(self):
        auth_user_name = os.environ.get('AUTHUSERNAME')
        auth_password = os.environ.get('AUTHPASSWORD')
        use_hmac_authentication = True

        client = MessageMediaMessagesClient(auth_user_name, auth_password, use_hmac_authentication)
        messages_controller = client.messages

        result = messages_controller.send_messages(self.__class__.body)

        self.assertIsNotNone(result)

    # Testing HMAC Auth content hash is appropriate
    def test_content_hash(self):
        http = urllib3.PoolManager()

        m = hashlib.md5()
        m.update(bytes(APIHelper.json_serialize(self.__class__.body), 'utf-8'))
        expected = m.hexdigest()

        _request = http.request(
            'POST',
            self.__class__._query_url,
            body=APIHelper.json_serialize(self.__class__.body),
            headers=self.__class__._headers
        )

        AuthManager.apply_hmac_auth(_request, self.__class__._url_path, APIHelper.json_serialize(self.__class__.body))
        actualValue = _request.getheader('x-Content-MD5')

        assert expected == actualValue
        print(os.environ.get('AUTHUSERNAME'))

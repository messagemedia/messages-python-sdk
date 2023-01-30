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

    # Testing successful message to MM endpoint
    def test_successful_message_to_endpoint(self):
        use_hmac_authentication = True

        client = MessageMediaMessagesClient(use_hmac_authentication)
        messages_controller = client.messages

        result = messages_controller.send_messages(self.__class__.body)

        self.assertIsNotNone(result)

    # Testing HMAC content hash is appropriate
    def test_MD5_content_hash_equivalent_to_body(self):
        http = urllib3.PoolManager()
        body = APIHelper.json_serialize(self.__class__.body)
        MD5 = self.__class__.content_hash

        _request = http.request(
            'POST',
            self.__class__._query_url,
            body=body,
            headers=self.__class__._headers
        )

        AuthManager.apply_hmac_auth(_request, self.__class__._query_url, body)
        requestMD5 = _request.getheader('x-Content-MD5')
        assert MD5 == requestMD5

    # Testing HMAC Auth is appropriate
    def test_AUTH_is_same_as_request(self):
        http = urllib3.PoolManager()
        body = APIHelper.json_serialize(self.__class__.body)
        date_header = self.__class__.date_header
        MD5 = self.__class__.content_hash

        hmac_auth = TestConfiguration.create_auth(self.__class__._query_url, 'POST', date_header,
                                                  MD5)
        _request = http.request(
            'POST',
            self.__class__._query_url,
            body=body,
            headers=self.__class__._headers
        )

        AuthManager.apply_hmac_auth(_request, self.__class__._query_url, body)
        request_authorization = _request.getheader('Authorization')
        assert request_authorization == hmac_auth

    # Testing unsupported request raises exception
    def test_unsuccessful_request_raises_exception(self):
        auth_user_name = 'Rubbish'
        auth_password = 'Random'
        use_hmac_authentication = True
        body = self.__class__.body

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

    @classmethod
    def setUpClass(cls):
        # Prepare request body
        cls.body = SendMessagesRequest()
        cls.body.messages = []
        cls.body.messages.append(Message())
        cls.body.messages[0].content = 'My tests message'
        cls.body.messages[0].destination_number = '+My Number'
        cls.body.messages[0].format = FormatEnum.SMS

        cls._url_path = '/v1/messages'
        cls._query_builder = Configuration.base_uri
        cls._query_builder += cls._url_path
        cls._query_url = APIHelper.clean_url(cls._query_builder)

        # Prepare header
        cls._headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json; charset=utf-8',
        }

        # Prepare content hash
        m = hashlib.md5()
        m.update(bytes(APIHelper.json_serialize(cls.body), 'utf-8'))
        cls.content_hash = m.hexdigest()

        # Prepare date header
        now = datetime.now()
        stamp = mktime(now.timetuple())
        cls.date_header = format_date_time(stamp)

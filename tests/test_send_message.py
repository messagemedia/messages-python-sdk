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

from message_media_messages.exceptions.send_messages_400_response_exception import SendMessages400ResponseException

from tests.TestConfiguration import TestConfiguration
from message_media_messages.http.auth.auth_manager import AuthManager
from message_media_messages.configuration import Configuration
from message_media_messages.api_helper import APIHelper
from message_media_messages.message_media_messages_client import MessageMediaMessagesClient
from message_media_messages.models.send_messages_request import SendMessagesRequest
from message_media_messages.models.message import Message
from message_media_messages.models.format_enum import FormatEnum
import urllib3
import requests
import os


class Test_MM_send_message(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.body = SendMessagesRequest()
        cls.body.messages = []

        cls.body.messages.append(Message())
        cls.body.messages[0].content = 'My tests message'
        cls.body.messages[0].destination_number = '+61452549798'
        cls.body.messages[0].format = FormatEnum.SMS

        cls._url_path = '/v1/messages'
        cls._query_builder = Configuration.base_uri
        cls._query_builder += cls._url_path
        cls._query_url = APIHelper.clean_url(cls._query_builder)

        cls._headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json; charset=utf-8',
        }

        m = hashlib.md5()
        m.update(bytes(APIHelper.json_serialize(cls.body), 'utf-8'))

        cls.content_hash = m.hexdigest()

    # Testing successful message to MM endpoint
    def test_successful_message_to_endpoint(self):
        use_hmac_authentication = True

        client = MessageMediaMessagesClient(use_hmac_authentication)
        messages_controller = client.messages

        result = messages_controller.send_messages(self.__class__.body)

        self.assertIsNotNone(result)

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

        print(_request.headers)
        print(MD5)
        print(requestMD5)
        print(_request.getheader('x-Content-MD5'))
        print(_request.status)

        assert MD5 == requestMD5

    # Testing HMAC Auth content hash is appropriate
    def test_AUTH_is_same_as_request(self):
        http = urllib3.PoolManager()
        body = APIHelper.json_serialize(self.__class__.body)
        now = datetime.now()
        stamp = mktime(now.timetuple())
        date_header = format_date_time(stamp)
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
        """print(_request.getheader('Authorization'))
        print(_request.getheader('x-Content-MD5'))
        print(MD5)
        print(hmac_auth)"""

    def test_unsuccessful_request_raises_exception(self):
        auth_user_name = 'Rubbish'
        auth_password = 'Random'
        use_hmac_authentication = True

        client = MessageMediaMessagesClient(auth_user_name, auth_password, use_hmac_authentication)
        messages_controller = client.messages

        body = SendMessagesRequest()
        body.messages = []

        body.messages.append(Message())
        body.messages[0].content = 'My tests message'
        body.messages[0].destination_number = '+61452549798'
        body.messages[0].format = FormatEnum.SMS

        with self.assertRaises(APIException) as cm:
            messages_controller.send_messages(body)
        the_exception = cm.exception
        self.assertIsNotNone(the_exception)
        print(the_exception)

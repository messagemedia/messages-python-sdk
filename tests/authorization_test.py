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


class TestAuthorization(unittest.TestCase):

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

    def test_post_request_authorization_values_are_appropriate(self):
        http = urllib3.PoolManager()
        body = APIHelper.json_serialize(self.__class__.body)
        date_header = self.__class__.date_header
        request_header = self.__class__._headers
        md5 = self.__class__.content_hash
        query_url = self.__class__._query_url
        content_signature = "x-Content-MD5: {}\n".format(md5)
        expected_username = 'hmac username="FxJMSlsivOoHAjDbWcO7"'
        expected_algorithm = ' algorithm="hmac-sha1"'
        expected_header = ' headers="date x-Content-MD5 request-line"'
        expected_signature = TestConfiguration.create_signature(date_header, content_signature, query_url, 'POST', True)

        _request = http.request(
            'POST',
            query_url,
            body=body,
            headers=request_header
        )

        AuthManager.apply_hmac_auth(_request, query_url, body)
        username, algorithm, header, signature = _request.getheader('Authorization').split(',')

        with self.subTest():
            self.assertEqual(expected_username, username)
            self.assertEqual(expected_header, header)
            self.assertEqual(expected_algorithm, algorithm)
            self.assertEqual(expected_signature, signature)

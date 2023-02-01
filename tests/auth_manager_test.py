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
from tests.test_util import TestUtility
from message_media_messages.http.auth.auth_manager import AuthManager
from message_media_messages.configuration import Configuration
from message_media_messages.api_helper import APIHelper
from message_media_messages.models.send_messages_request import SendMessagesRequest
from message_media_messages.models.message import Message
from message_media_messages.models.format_enum import FormatEnum
import urllib3


class AuthManagerTests(unittest.TestCase):

    body = SendMessagesRequest()
    body.messages = []
    body.messages.append(Message())
    body.messages[0].content = 'My tests message'
    body.messages[0].destination_number = '{}'
    body.messages[0].format = FormatEnum.SMS

    _url_path = '/v1/messages'
    _query_builder = Configuration.base_uri
    _query_builder += _url_path
    _query_url = APIHelper.clean_url(_query_builder)

    _headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json; charset=utf-8',
    }

    m = hashlib.md5()
    m.update(bytes(APIHelper.json_serialize(body), 'utf-8'))
    content_hash = m.hexdigest()

    now = datetime.now()
    stamp = mktime(now.timetuple())
    date_header = format_date_time(stamp)

    content_signature = "x-Content-MD5: {}\n".format(content_hash)
    get_content_signature = ""

    def test_post_request_authorization_header_values_are_appropriate(self):
        date_header, expected_algorithm, expected_username, http, query_url, request_header = self.header_setup()
        body = APIHelper.json_serialize(self.body)
        content_signature = self.content_signature
        expected_header = ' headers="date x-Content-MD5 request-line"'
        expected_signature = TestUtility.create_signature(date_header, content_signature, query_url, 'POST', True)

        _request = http.request(
            'POST',
            query_url,
            body=body,
            headers=request_header
        )

        AuthManager.apply_hmac_auth(_request, query_url, body)
        username, algorithm, header, signature = _request.getheader('Authorization').split(',')

        self.assert_cases(algorithm, expected_algorithm, expected_header, expected_signature, expected_username,
                          header, signature, username)

    def test_md5_content_hash_equivalent_to_body(self):
        http = urllib3.PoolManager()
        body = APIHelper.json_serialize(self.body)
        md5 = self.content_hash
        query_url = self._query_url
        request_header = self._headers

        _request = http.request(
            'POST',
            query_url,
            body=body,
            headers=request_header
        )

        AuthManager.apply_hmac_auth(_request, query_url, body)
        requestMD5 = _request.getheader('x-Content-MD5')
        assert md5 == requestMD5

    def test_get_request_authorization_header_values_are_appropriate(self):
        date_header, expected_algorithm, expected_username, http, query_url, request_header = self.header_setup()
        content_signature = ""
        expected_header = ' headers="date request-line"'
        expected_signature = TestUtility.create_signature(date_header, content_signature, query_url, 'GET', True)

        _request = http.request(
            'GET',
            query_url,
            headers=request_header
        )

        AuthManager.apply_hmac_auth(_request, query_url)
        username, algorithm, header, signature = _request.getheader('Authorization').split(',')

        self.assert_cases(algorithm, expected_algorithm, expected_header, expected_signature, expected_username,
                          header, signature, username)

    def header_setup(self):
        http = urllib3.PoolManager()
        date_header = self.date_header
        request_header = self._headers
        query_url = self._query_url
        expected_username = 'hmac username="{}"'
        expected_algorithm = ' algorithm="hmac-sha1"'
        return date_header, expected_algorithm, expected_username, http, query_url, request_header

    def assert_cases(self, algorithm, expected_algorithm, expected_header, expected_signature, expected_username,
                     header, signature, username):
        with self.subTest():
            self.assertEqual(expected_username, username)
            self.assertEqual(expected_header, header)
            self.assertEqual(expected_algorithm, algorithm)
            self.assertEqual(expected_signature, signature)

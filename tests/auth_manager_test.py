# -*- coding: utf-8 -*-

import hashlib
import unittest

from freezegun import freeze_time

from message_media_messages.api_helper import APIHelper
from message_media_messages.configuration import Configuration
from message_media_messages.http.auth.auth_manager import AuthManager
from message_media_messages.http.requests_client import RequestsClient
from message_media_messages.models.format_enum import FormatEnum
from message_media_messages.models.message import Message
from message_media_messages.models.send_messages_request import SendMessagesRequest
from tests.test_util import TestUtil


class AuthManagerTest(unittest.TestCase):

    def __init__(self, method_name: str = ...):
        super().__init__(method_name)
        self.content_hash = None
        self.query_url = None
        self.send_message_request = None

    def setUp(self):
        self.send_message_request = self.get_send_message_request()
        self.query_url = APIHelper.clean_url(Configuration.base_uri + '/v1/messages')
        self.content_hash = self.get_content_hash(self.send_message_request)
        self.content_md5_header = "x-Content-MD5: {}\n".format(self.content_hash)
        self.date_header = 'Wed, 08 Feb 2023 03:00:00 GMT'
        self.expected_algorithm = ' algorithm="hmac-sha1"'
        Configuration.hmac_auth_user_name = "some_user_name"
        self.expected_username = "hmac username=\"" + Configuration.hmac_auth_user_name + "\""

    @freeze_time("2023-02-08 14:00:00")
    def test_post_request_hmac_authorization_header_values_are_appropriate(self):
        body = APIHelper.json_serialize(self.send_message_request)

        request = RequestsClient().post(
            query_url=self.query_url,
            parameters=body,
            headers={}
        )

        AuthManager.apply_hmac_auth(request, self.query_url, body)

        expected_headers_property = ' headers="date x-Content-MD5 request-line"'
        expected_signature = TestUtil.create_signature(self.date_header, self.content_md5_header,
                                                       self.query_url, 'POST', True)
        self.assert_auth_header(request, expected_headers_property, expected_signature)

    def test_post_request_content_md5_is_md5_of_request_body(self):
        body = APIHelper.json_serialize(self.send_message_request)

        request = RequestsClient().post(
            query_url=self.query_url,
            parameters=body,
            headers={}
        )

        AuthManager.apply_hmac_auth(request, self.query_url, body)
        request_md5 = request.headers['x-Content-MD5']
        assert self.content_hash == request_md5

    @freeze_time("2023-02-08 14:00:00")
    def test_get_request_hmac_authorization_header_values_are_appropriate(self):
        request = RequestsClient().get(
            query_url=self.query_url,
            headers={}
        )

        AuthManager.apply_hmac_auth(request, self.query_url)

        expected_headers_property = ' headers="date request-line"'
        expected_signature = TestUtil.create_signature(self.date_header, "",
                                                       self.query_url, 'GET', True)
        self.assert_auth_header(request, expected_headers_property, expected_signature)

    def assert_auth_header(self, request, expected_headers_property, expected_signature):
        username, algorithm, headers, signature = request.headers['Authorization'].split(',')
        with self.subTest():
            self.assertEqual(self.expected_username, username)
            self.assertEqual(expected_headers_property, headers)
            self.assertEqual(self.expected_algorithm, algorithm)
            self.assertEqual(expected_signature, signature)

    @staticmethod
    def get_send_message_request():
        send_message_request = SendMessagesRequest()
        send_message_request.messages = []
        send_message_request.messages.append(Message())
        send_message_request.messages[0].content = 'My tests message'
        send_message_request.messages[0].destination_number = '+61491570006'
        send_message_request.messages[0].format = FormatEnum.SMS
        return send_message_request

    @staticmethod
    def get_content_hash(request):
        m = hashlib.md5()
        m.update(bytes(APIHelper.json_serialize(request), 'utf-8'))
        content_hash = m.hexdigest()
        return content_hash

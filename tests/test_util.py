# -*- coding: utf-8 -*-

"""
    message_media_messages

    This file was automatically generated for MessageMedia by APIMATIC v2.0 ( https://apimatic.io ).
"""
import base64
import hashlib
import hmac

from message_media_messages.configuration import Configuration
from message_media_messages.models.format_enum import FormatEnum
from message_media_messages.models.message import Message
from message_media_messages.models.send_messages_request import SendMessagesRequest
from tests.test_configuration import TestConfiguration


class TestUtility(object):

    @staticmethod
    def create_signature(date, content_signature, url, request_type, wrapper=None):
        signature = ' signature="'
        signing_string = "date: {}\n{}{} {} HTTP/1.1"\
            .format(date, content_signature, request_type, url)

        hashed = hmac.new(Configuration.hmac_auth_password.encode("utf-8"),
                          signing_string.encode("utf-8"), hashlib.sha1)
        if wrapper is not None:
            signature += (base64.b64encode(hashed.digest()).decode('utf-8')) + '"'
            return signature
        else:
            return base64.b64encode(hashed.digest()).decode('utf-8')

    @staticmethod
    def create_body():
        body = SendMessagesRequest()
        body.messages = []
        body.messages.append(Message())
        body.messages[0].content = 'My tests message'
        body.messages[0].destination_number = '{}'.format(TestConfiguration.request_dest_number)
        body.messages[0].format = FormatEnum.SMS

        return body


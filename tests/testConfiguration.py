# -*- coding: utf-8 -*-

"""
    message_media_messages

    This file was automatically generated for MessageMedia by APIMATIC v2.0 ( https://apimatic.io ).
"""
import base64
import hashlib
import hmac

from message_media_messages.api_helper import APIHelper
from message_media_messages.configuration import Configuration
from message_media_messages.models.format_enum import FormatEnum
from message_media_messages.models.message import Message
from message_media_messages.models.send_messages_request import SendMessagesRequest


class TestConfiguration(object):
    """A class used for configuring the sendMessageTests by a user.

    This class need not be instantiated and all properties and methods
    are accessible without instance creation.

    """

    """def create_auth(url, request_type, date_header, content_hash):
        content_header = "x-Content-MD5 "
        content_signature = "x-Content-MD5: {}\n".format(content_hash)

        hmac_signature = TestConfiguration.create_signature(date_header,
                                                            content_signature,
                                                            url,
                                                            request_type)

        joined = 'username="{}", algorithm="hmac-sha1", headers="date {}'\
                 'request-line", signature="{}"'\
            .format(Configuration.hmac_auth_user_name, content_header, hmac_signature)

        header_value = "hmac {}".format(joined)
        return header_value"""
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
        body.messages[0].destination_number = '+My Number'
        body.messages[0].format = FormatEnum.SMS

        return body

    @staticmethod
    def create_url(message_id):
        _url_path = '/v1/messages/{messageId}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'messageId': message_id
        })
        _query_builder = Configuration.base_uri
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        return _query_url

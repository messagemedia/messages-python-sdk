# -*- coding: utf-8 -*-

"""
    message_media_messages

    This file was automatically generated for MessageMedia by APIMATIC v2.0 ( https://apimatic.io ).
"""
import base64
import hashlib
import hmac
from message_media_messages.configuration import Configuration


class TestConfiguration(object):
    """A class used for configuring the sendMessageTests by a user.

    This class need not be instantiated and all properties and methods
    are accessible without instance creation.

    """

    def create_auth(url, request_type, date_header, content_hash):
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
        return header_value

    def create_signature(date, content_signature, url, request_type):
        signing_string = "date: {}\n{}{} {} HTTP/1.1" \
            .format(date, content_signature, request_type, url)

        hashed = hmac.new(Configuration.hmac_auth_password.encode("utf-8"),
                          signing_string.encode("utf-8"), hashlib.sha1)

        return base64.b64encode(hashed.digest()).decode('utf-8')

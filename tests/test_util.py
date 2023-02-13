# -*- coding: utf-8 -*-

import base64
import hashlib
import hmac

from message_media_messages.configuration import Configuration


class TestUtil(object):

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




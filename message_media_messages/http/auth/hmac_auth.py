# -*- coding: utf-8 -*-

"""
   message_media_messages.http.auth.basic_auth

"""
import base64
from struct import unpack
from wsgiref.handlers import format_date_time
from datetime import datetime
from time import mktime
from ...configuration import Configuration
import hmac
import hashlib


class HmacAuth:

    def __init__(self):
        pass

    @staticmethod
    def apply(http_request, url, body=None):
        """ Add basic authentication to the request.

        Args:
            http_request (HttpRequest): The HttpRequest object to which
                authentication will be added.
            body: the body of the request. None for GET requests
            url: the url of the request

        """
        username = Configuration.hmac_auth_user_name

        content_signature = ""
        content_header = ""

        now = datetime.now()
        stamp = mktime(now.timetuple())
        date_header = format_date_time(stamp)

        if body is not None:
            m = hashlib.md5()
            content_hash = m.hexdigest()
            content_signature = "x-Content-MD5: {}\n".format(content_hash)
            content_header = "x-Content-MD5 "
            http_request.headers["x-Content-MD5"] = content_hash

        http_request.headers["date"] = date_header

        hmac_signature = HmacAuth.create_signature(date_header, content_signature, url, body)

        joined = "username=\"{}\", algorithm=\"hmac-sha1\", headers=\"date {}request-line\", signature=\"{}\""\
            .format(username, content_header, hmac_signature)

        header_value = "hmac {}".format(joined)
        http_request.headers["Authorization"] = header_value

    @staticmethod
    def create_signature(date, content_signature, url, body=None):
        request_type = "GET"

        if body is not None:
            request_type = "POST"

        signing_string = "date: {}\n{}{} {} HTTP/1.1".format(date, content_signature, request_type, url)
        hashed = hmac.new(Configuration.hmac_auth_password.encode("utf-8"), signing_string.encode("utf-8"), hashlib.sha1)

        return base64.b64encode(hashed.digest()).decode('utf-8');

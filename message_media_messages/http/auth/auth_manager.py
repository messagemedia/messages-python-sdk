# -*- coding: utf-8 -*-

"""
    message_media_messages

    This file was automatically generated for MessageMedia by APIMATIC v2.0 ( https://apimatic.io ).
"""

import base64
import hashlib
import hmac
from datetime import datetime
from time import mktime
from wsgiref.handlers import format_date_time
from message_media_messages.configuration import Configuration


class AuthManager:

    @staticmethod
    def apply(http_request, url, body=None):
        """ Add authentication to the request.

        Args:
            http_request (HttpRequest): The HttpRequest object to which
                authentication will be added.
            url (str): The url of the request.
            body (str): The body of the request. None for GET requests.

        """

        if Configuration.hmac_auth_user_name is not None and \
                Configuration.hmac_auth_password is not None:
            AuthManager.apply_hmac_auth(http_request, url, body)
        else:
            AuthManager.apply_basic_auth(http_request)

    @staticmethod
    def apply_basic_auth(http_request):
        """ Add basic authentication to the request.

        Args:
            http_request (HttpRequest): The HttpRequest object to which
                authentication will be added.

        """

        username = Configuration.basic_auth_user_name
        password = Configuration.basic_auth_password
        joined = "{}:{}".format(username, password)
        encoded = base64.b64encode(str.encode(joined)).decode('iso-8859-1')
        header_value = "Basic {}".format(encoded)
        http_request.headers["Authorization"] = header_value

    @staticmethod
    def apply_hmac_auth(http_request, url, body=None):
        """ Add hmac authentication to the request.

        Args:
            http_request (HttpRequest): The HttpRequest object to which
                authentication will be added.
            url (str): The url of the request.
            body (str): The body of the request. None for GET requests.

        """

        username = Configuration.hmac_auth_user_name

        content_signature = ""
        content_header = ""

        now = datetime.now()
        stamp = mktime(now.timetuple())
        date_header = format_date_time(stamp)

        request_type = "GET"

        if body is not None:
            request_type = "POST"
            m = hashlib.md5()
            m.update(bytes(body, 'utf-8'))
            content_hash = m.hexdigest()
            content_signature = "x-Content-MD5: {}\n".format(content_hash)
            content_header = "x-Content-MD5 "
            http_request.headers["x-Content-MD5"] = content_hash

        http_request.headers["date"] = date_header

        hmac_signature = AuthManager.create_signature(date_header,
                                                      content_signature,
                                                      url,
                                                      request_type)

        joined = 'username="{}", algorithm="hmac-sha1", headers="date {}'\
                 'request-line", signature="{}"'\
            .format(username, content_header, hmac_signature)

        header_value = "hmac {}".format(joined)
        http_request.headers["Authorization"] = header_value

    @staticmethod
    def create_signature(date, content_signature, url, request_type):
        signing_string = "date: {}\n{}{} {} HTTP/1.1" \
            .format(date, content_signature, request_type, url)

        hashed = hmac.new(Configuration.hmac_auth_password.encode("utf-8"),
                          signing_string.encode("utf-8"), hashlib.sha1)

        return base64.b64encode(hashed.digest()).decode('utf-8')

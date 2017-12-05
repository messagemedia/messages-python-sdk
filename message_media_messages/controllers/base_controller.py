# -*- coding: utf-8 -*-

"""
    message_media_messagescontrollers.base_controller

"""

from ..api_helper import APIHelper
from ..configuration import Configuration
from ..http.auth.basic_auth import BasicAuth
from ..http.auth.hmac_auth import HmacAuth
from ..http.http_context import HttpContext
from ..http.requests_client import RequestsClient
from ..exceptions.api_exception import APIException


class BaseController(object):

    """All controllers inherit from this base class.

    Attributes:
        http_client (HttpClient): The HttpClient which a specific controller
            instance will use. By default all the controller objects share
            the same HttpClient. A user can use his own custom HttpClient
            as well.
        http_call_back (HttpCallBack): An object which holds call back
            methods to be called before and after the execution of an HttpRequest.
        global_headers (dict): The global headers of the API which are sent with
            every request.

    """

    http_client = RequestsClient()

    http_call_back = None

    global_headers = {
        'user-agent': 'messagemedia-messages-python-sdk-1.1.0'
    }

    def __init__(self, client=None, call_back=None):
        if client is not None:
            self.http_client = client
        if call_back is not None:
            self.http_call_back = call_back

    @staticmethod
    def validate_parameters(**kwargs):
        """Validates required parameters of an endpoint.

        Args:
            kwargs (dict): A dictionary of the required parameters.

        """
        for name, value in kwargs.items():
            if value is None:
                raise ValueError("Required parameter {} cannot be None.".format(name))

    def execute_request(self, request, binary=False, name=None):
        """Executes an HttpRequest.

        Args:
            request (HttpRequest): The HttpRequest to execute.
            binary (bool): A flag which should be set to True if
                a binary response is expected.

        Returns:
            HttpContext: The HttpContext of the request. It contains,
                both, the request itself and the HttpResponse object.
                :param request:
                :param binary:
                :param name:

        """
        # Invoke the on before request HttpCallBack if specified
        if self.http_call_back is not None:
            self.logger.info("Calling the on_before_request method of http_call_back for {}.".format(name))
            self.http_call_back.on_before_request(request)

        # Add global headers to request
        self.logger.info("Merging global headers with endpoint headers for {}.".format(name))
        request.headers = APIHelper.merge_dicts(self.global_headers, request.headers)

        # Invoke the API call to fetch the response.
        self.logger.debug("Raw request for {} is: {}".format(name, vars(request)))
        func = self.http_client.execute_as_binary if binary else self.http_client.execute_as_string
        response = func(request)
        self.logger.debug("Raw response for {} is: {}".format(name, vars(response)))
        self.logger.info("Wrapping request and response in a context object for {}.".format(name))
        context = HttpContext(request, response)

        # Invoke the on after response HttpCallBack if specified
        if self.http_call_back is not None:
            self.logger.info("Calling on_after_response method of http_call_back for {}.".format(name))
            self.http_call_back.on_after_response(context)

        return context

    @staticmethod
    def apply_authentication(request, url, body=None):
        if Configuration.hmac_auth_user_name is None or Configuration.hmac_auth_password is None:
            BasicAuth.apply(request)
        else:
            HmacAuth.apply(request, url, body)

    @staticmethod
    def add_account_header(headers, account_header):
        if account_header is not None:
            headers['account'] = account_header

    @staticmethod
    def validate_response(context):
        """Validates an HTTP response by checking for global errors.

        Args:
            context (HttpContext): The HttpContext of the API call.

        """
        if (context.response.status_code < 200) or (context.response.status_code > 208): # [200,208] = HTTP OK
            raise APIException('HTTP response not OK.', context)

# -*- coding: utf-8 -*-

"""
    message_media_messages

    This file was automatically generated for MessageMedia by APIMATIC v2.0 ( https://apimatic.io ).
"""
import os


class TestConfiguration(object):
    """A class used for configuring the SDK Test cases by a user.

    This class need not be instantiated and all properties and methods
    are accessible without instance creation.

    """

    # Set the id for a request
    request_message_id = os.environ.get('message_id')

    # The base Uri for API calls
    request_dest_number = os.environ.get('dest_number')

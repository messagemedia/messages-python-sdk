# -*- coding: utf-8 -*-

"""
   message_media_messages.configuration

"""
import sys
import logging

from .api_helper import APIHelper

logging.basicConfig(stream=sys.stdout, level=logging.INFO)

class Configuration(object):

    """A class used for configuring the SDK by a user.

    This class need not be instantiated and all properties and methods
    are accessible without instance creation.

    """

    # Set the array parameter serialization method
    # (allowed: indexed, unindexed, plain, csv, tsv, psv)
    array_serialization = "indexed"

    # The base Uri for API calls
    base_uri = 'https://api.messagemedia.com'

    # The username to use with basic authentication
    # TODO: Set an appropriate value
    basic_auth_user_name = "TODO: Replace"

    # The password to use with basic authentication
    # TODO: Set an appropriate value
    basic_auth_password = "TODO: Replace"


# -*- coding: utf-8 -*-

"""
    message_media_messages

    This file was automatically generated for MessageMedia by APIMATIC v2.0 ( https://apimatic.io ).
"""

from .decorators import lazy_property
from message_media_messages.configuration import Configuration
from message_media_messages.controllers.messages_controller import MessagesController
from message_media_messages.controllers.delivery_reports_controller import DeliveryReportsController
from message_media_messages.controllers.replies_controller import RepliesController


class MessageMediaMessagesClient(object):

    config = Configuration

    @lazy_property
    def messages(self):
        return MessagesController()

    @lazy_property
    def delivery_reports(self):
        return DeliveryReportsController()

    @lazy_property
    def replies(self):
        return RepliesController()


    def __init__(self,
                 auth_user_name=None,
                 auth_password=None,
                 use_hmac_authentication=False):
        if use_hmac_authentication:
            Configuration.hmac_auth_user_name = auth_user_name
            Configuration.hmac_auth_password = auth_password
        else:
            Configuration.basic_auth_user_name = auth_user_name
            Configuration.basic_auth_password = auth_password



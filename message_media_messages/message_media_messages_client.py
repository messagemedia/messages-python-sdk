# -*- coding: utf-8 -*-

"""
    message_media_messages.message_media_messages_client

"""
from .decorators import LazyProperty
from .configuration import Configuration
from .controllers.messages_controller import MessagesController
from .controllers.delivery_reports_controller import DeliveryReportsController
from .controllers.replies_controller import RepliesController


class MessageMediaMessagesClient(object):

    config = Configuration

    @LazyProperty
    def messages(self):
        return MessagesController()

    @LazyProperty
    def delivery_reports(self):
        return DeliveryReportsController()

    @LazyProperty
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

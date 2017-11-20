# -*- coding: utf-8 -*-

"""
    message_media_messages.message_media_messages_client

    This file was automatically generated for MessageMedia by APIMATIC v2.0 ( https://apimatic.io ).
"""
from .decorators import lazy_property
from .configuration import Configuration
from .controllers.messages_controller import MessagesController
from .controllers.delivery_reports_controller import DeliveryReportsController
from .controllers.replies_controller import RepliesController

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
                 basic_auth_user_name = None,
                 basic_auth_password = None):
        if basic_auth_user_name != None:
            Configuration.basic_auth_user_name = basic_auth_user_name
        if basic_auth_password != None:
            Configuration.basic_auth_password = basic_auth_password



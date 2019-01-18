# -*- coding: utf-8 -*-

"""
    message_media_messages

    This file was automatically generated for MessageMedia by APIMATIC v2.0 ( https://apimatic.io ).
"""

from message_media_messages.api_helper import APIHelper
import message_media_messages.models.vendor_account_id

class Reply(object):

    """Implementation of the 'Reply' model.

    TODO: type model description here.

    Attributes:
        callback_url (string): The URL specified as the callback URL in the
            original submit message request
        content (string): Content of the reply
        date_received (datetime): Date time when the reply was received
        destination_number (string): Address from which this reply was sent
            to
        message_id (uuid|string): Unique ID of the original message
        metadata (object): Any metadata that was included in the original
            submit message request
        reply_id (uuid|string): Unique ID of this reply
        source_number (string): Address from which this reply was received
            from
        vendor_account_id (VendorAccountId): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "callback_url":'callback_url',
        "content":'content',
        "date_received":'date_received',
        "destination_number":'destination_number',
        "message_id":'message_id',
        "metadata":'metadata',
        "reply_id":'reply_id',
        "source_number":'source_number',
        "vendor_account_id":'vendor_account_id'
    }

    def __init__(self,
                 callback_url=None,
                 content=None,
                 date_received=None,
                 destination_number=None,
                 message_id=None,
                 metadata=None,
                 reply_id=None,
                 source_number=None,
                 vendor_account_id=None):
        """Constructor for the Reply class"""

        # Initialize members of the class
        self.callback_url = callback_url
        self.content = content
        self.date_received = APIHelper.RFC3339DateTime(date_received) if date_received else None
        self.destination_number = destination_number
        self.message_id = message_id
        self.metadata = metadata
        self.reply_id = reply_id
        self.source_number = source_number
        self.vendor_account_id = vendor_account_id


    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object as
            obtained from the deserialization of the server's response. The keys
            MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        callback_url = dictionary.get('callback_url')
        content = dictionary.get('content')
        date_received = APIHelper.RFC3339DateTime.from_value(dictionary.get("date_received")).datetime if dictionary.get("date_received") else None
        destination_number = dictionary.get('destination_number')
        message_id = dictionary.get('message_id')
        metadata = dictionary.get('metadata')
        reply_id = dictionary.get('reply_id')
        source_number = dictionary.get('source_number')
        vendor_account_id = message_media_messages.models.vendor_account_id.VendorAccountId.from_dictionary(dictionary.get('vendor_account_id')) if dictionary.get('vendor_account_id') else None

        # Return an object of this model
        return cls(callback_url,
                   content,
                   date_received,
                   destination_number,
                   message_id,
                   metadata,
                   reply_id,
                   source_number,
                   vendor_account_id)



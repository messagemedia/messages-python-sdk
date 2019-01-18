# -*- coding: utf-8 -*-

"""
    message_media_messages

    This file was automatically generated for MessageMedia by APIMATIC v2.0 ( https://apimatic.io ).
"""

from message_media_messages.api_helper import APIHelper
import message_media_messages.models.vendor_account_id

class DeliveryReport(object):

    """Implementation of the 'DeliveryReport' model.

    TODO: type model description here.

    Attributes:
        callback_url (string): The URL specified as the callback URL in the
            original submit message request
        date_received (datetime): The date and time at which this delivery
            report was generated in UTC.
        delay (int): Deprecated, no longer in use
        delivery_report_id (uuid|string): Unique ID for this delivery report
        message_id (uuid|string): Unique ID of the original message
        metadata (object): Any metadata that was included in the original
            submit message request
        original_text (string): Text of the original message.
        source_number (string): Address from which this delivery report was
            received
        status (Status2Enum): The status of the message as per the delivery
            report
        submitted_date (datetime): The date and time when the message status
            changed in UTC. For a delivered DR this may indicate the time at
            which the message was received on the handset.
        vendor_account_id (VendorAccountId): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "callback_url":'callback_url',
        "date_received":'date_received',
        "delay":'delay',
        "delivery_report_id":'delivery_report_id',
        "message_id":'message_id',
        "metadata":'metadata',
        "original_text":'original_text',
        "source_number":'source_number',
        "status":'status',
        "submitted_date":'submitted_date',
        "vendor_account_id":'vendor_account_id'
    }

    def __init__(self,
                 callback_url=None,
                 date_received=None,
                 delay=None,
                 delivery_report_id=None,
                 message_id=None,
                 metadata=None,
                 original_text=None,
                 source_number=None,
                 status=None,
                 submitted_date=None,
                 vendor_account_id=None):
        """Constructor for the DeliveryReport class"""

        # Initialize members of the class
        self.callback_url = callback_url
        self.date_received = APIHelper.RFC3339DateTime(date_received) if date_received else None
        self.delay = delay
        self.delivery_report_id = delivery_report_id
        self.message_id = message_id
        self.metadata = metadata
        self.original_text = original_text
        self.source_number = source_number
        self.status = status
        self.submitted_date = APIHelper.RFC3339DateTime(submitted_date) if submitted_date else None
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
        date_received = APIHelper.RFC3339DateTime.from_value(dictionary.get("date_received")).datetime if dictionary.get("date_received") else None
        delay = dictionary.get('delay')
        delivery_report_id = dictionary.get('delivery_report_id')
        message_id = dictionary.get('message_id')
        metadata = dictionary.get('metadata')
        original_text = dictionary.get('original_text')
        source_number = dictionary.get('source_number')
        status = dictionary.get('status')
        submitted_date = APIHelper.RFC3339DateTime.from_value(dictionary.get("submitted_date")).datetime if dictionary.get("submitted_date") else None
        vendor_account_id = message_media_messages.models.vendor_account_id.VendorAccountId.from_dictionary(dictionary.get('vendor_account_id')) if dictionary.get('vendor_account_id') else None

        # Return an object of this model
        return cls(callback_url,
                   date_received,
                   delay,
                   delivery_report_id,
                   message_id,
                   metadata,
                   original_text,
                   source_number,
                   status,
                   submitted_date,
                   vendor_account_id)



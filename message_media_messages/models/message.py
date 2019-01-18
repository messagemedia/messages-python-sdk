# -*- coding: utf-8 -*-

"""
    message_media_messages

    This file was automatically generated for MessageMedia by APIMATIC v2.0 ( https://apimatic.io ).
"""

from message_media_messages.api_helper import APIHelper

class Message(object):

    """Implementation of the 'Message' model.

    TODO: type model description here.

    Attributes:
        callback_url (string): URL replies and delivery reports to this
            message will be pushed to
        content (string): Content of the message
        destination_number (string): Destination number of the message
        delivery_report (bool): Request a delivery report for this message
        format (FormatEnum): Format of message, SMS or TTS (Text To Speech).
        message_expiry_timestamp (datetime): Date time after which the message
            expires and will not be sent
        metadata (object): Metadata for the message specified as a set of key
            value pairs, each key can be up to 100 characters long and each
            value can be up to 256 characters long ``` {    "myKey":
            "myValue",    "anotherKey": "anotherValue" } ```
        scheduled (datetime): Scheduled delivery date time of the message
        source_number (string): TODO: type description here.
        source_number_type (SourceNumberTypeEnum): Type of source address
            specified, this can be INTERNATIONAL, ALPHANUMERIC or SHORTCODE
        message_id (uuid|string): Unique ID of this message
        status (StatusEnum): The status of the message
        media (list of string): The media is used to specify the url of the
            media file that you are trying to send. Supported file formats
            include png, jpeg and gif. format parameter must be set to MMS for
            this to work.
        subject (string): The subject field is used to denote subject of the
            MMS message and has a maximum size of 64 characters long

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "content":'content',
        "destination_number":'destination_number',
        "callback_url":'callback_url',
        "delivery_report":'delivery_report',
        "format":'format',
        "message_expiry_timestamp":'message_expiry_timestamp',
        "metadata":'metadata',
        "scheduled":'scheduled',
        "source_number":'source_number',
        "source_number_type":'source_number_type',
        "message_id":'message_id',
        "status":'status',
        "media":'media',
        "subject":'subject'
    }

    def __init__(self,
                 content=None,
                 destination_number=None,
                 callback_url=None,
                 delivery_report=False,
                 format=None,
                 message_expiry_timestamp=None,
                 metadata=None,
                 scheduled=None,
                 source_number=None,
                 source_number_type=None,
                 message_id=None,
                 status=None,
                 media=None,
                 subject=None):
        """Constructor for the Message class"""

        # Initialize members of the class
        self.callback_url = callback_url
        self.content = content
        self.destination_number = destination_number
        self.delivery_report = delivery_report
        self.format = format
        self.message_expiry_timestamp = APIHelper.RFC3339DateTime(message_expiry_timestamp) if message_expiry_timestamp else None
        self.metadata = metadata
        self.scheduled = APIHelper.RFC3339DateTime(scheduled) if scheduled else None
        self.source_number = source_number
        self.source_number_type = source_number_type
        self.message_id = message_id
        self.status = status
        self.media = media
        self.subject = subject


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
        content = dictionary.get('content')
        destination_number = dictionary.get('destination_number')


        # Return an object of this model
        return cls(content,
                   destination_number)

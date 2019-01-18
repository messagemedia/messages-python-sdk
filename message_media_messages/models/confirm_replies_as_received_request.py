# -*- coding: utf-8 -*-

"""
    message_media_messages

    This file was automatically generated for MessageMedia by APIMATIC v2.0 ( https://apimatic.io ).
"""


class ConfirmRepliesAsReceivedRequest(object):

    """Implementation of the 'Confirm replies as received request' model.

    TODO: type model description here.

    Attributes:
        reply_ids (list of string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "reply_ids":'reply_ids'
    }

    def __init__(self,
                 reply_ids=None):
        """Constructor for the ConfirmRepliesAsReceivedRequest class"""

        # Initialize members of the class
        self.reply_ids = reply_ids


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
        reply_ids = dictionary.get('reply_ids')

        # Return an object of this model
        return cls(reply_ids)



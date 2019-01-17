# -*- coding: utf-8 -*-

"""
    message_media_messages

    This file was automatically generated for MessageMedia by APIMATIC v2.0 ( https://apimatic.io ).
"""


class CancelScheduledMessageRequest(object):

    """Implementation of the 'Cancel scheduled message request' model.

    TODO: type model description here.

    Attributes:
        status (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "status":'status'
    }

    def __init__(self,
                 status='cancelled'):
        """Constructor for the CancelScheduledMessageRequest class"""

        # Initialize members of the class
        self.status = status


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
        status = dictionary.get("status") if dictionary.get("status") else 'cancelled'

        # Return an object of this model
        return cls(status)



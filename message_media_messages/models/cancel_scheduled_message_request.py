# -*- coding: utf-8 -*-

"""
    message_media_messages.models.cancel_scheduled_message_request

"""


class CancelScheduledMessageRequest(object):

    """
    Implementation of the 'Cancel scheduled message request' model.

    TODO: type model description here.

    Attributes:
        status (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "status": "status"
    }

    def __init__(self,
                 status=None):
        """
        Constructor for the CancelScheduledMessageRequest class
        """

        # Initialize members of the class
        self.status = status

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """
        Creates an instance of this model from a dictionary

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
        status = dictionary.get("status")

        # Return an object of this model
        return cls(status)

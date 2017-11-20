# -*- coding: utf-8 -*-

"""
    message_media_messages.models.check_replies_response

    This file was automatically generated for MessageMedia by APIMATIC v2.0 ( https://apimatic.io )
"""


class CheckRepliesResponse(object):

    """Implementation of the 'Check replies response' model.

    TODO: type model description here.

    Attributes:
        replies (list of object): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "replies" : "replies"
    }

    def __init__(self,
                 replies=None):
        """Constructor for the CheckRepliesResponse class"""

        # Initialize members of the class
        self.replies = replies


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
        replies = dictionary.get("replies")

        # Return an object of this model
        return cls(replies)



# -*- coding: utf-8 -*-

"""
    message_media_messages

    This file was automatically generated for MessageMedia by APIMATIC v2.0 ( https://apimatic.io ).
"""

import message_media_messages.models.reply

class CheckRepliesResponse(object):

    """Implementation of the 'Check replies response' model.

    TODO: type model description here.

    Attributes:
        replies (list of Reply): The oldest 100 unconfirmed replies

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "replies":'replies'
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
        replies = None
        if dictionary.get('replies') != None:
            replies = list()
            for structure in dictionary.get('replies'):
                replies.append(message_media_messages.models.reply.Reply.from_dictionary(structure))

        # Return an object of this model
        return cls(replies)



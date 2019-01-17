# -*- coding: utf-8 -*-

"""
    message_media_messages

    This file was automatically generated for MessageMedia by APIMATIC v2.0 ( https://apimatic.io ).
"""


class ConfirmDeliveryReportsAsReceivedRequest(object):

    """Implementation of the 'Confirm delivery reports as received request' model.

    TODO: type model description here.

    Attributes:
        delivery_report_ids (list of string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "delivery_report_ids":'delivery_report_ids'
    }

    def __init__(self,
                 delivery_report_ids=None):
        """Constructor for the ConfirmDeliveryReportsAsReceivedRequest class"""

        # Initialize members of the class
        self.delivery_report_ids = delivery_report_ids


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
        delivery_report_ids = dictionary.get('delivery_report_ids')

        # Return an object of this model
        return cls(delivery_report_ids)



# -*- coding: utf-8 -*-

"""
    message_media_messages.models.check_delivery_reports_response

    This file was automatically generated for MessageMedia by APIMATIC v2.0 ( https://apimatic.io )
"""


class CheckDeliveryReportsResponse(object):

    """Implementation of the 'Check delivery reports response' model.

    TODO: type model description here.

    Attributes:
        delivery_reports (list of object): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "delivery_reports" : "delivery_reports"
    }

    def __init__(self,
                 delivery_reports=None):
        """Constructor for the CheckDeliveryReportsResponse class"""

        # Initialize members of the class
        self.delivery_reports = delivery_reports


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
        delivery_reports = dictionary.get("delivery_reports")

        # Return an object of this model
        return cls(delivery_reports)



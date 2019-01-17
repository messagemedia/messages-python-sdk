# -*- coding: utf-8 -*-

"""
    message_media_messages

    This file was automatically generated for MessageMedia by APIMATIC v2.0 ( https://apimatic.io ).
"""

import message_media_messages.models.delivery_report

class CheckDeliveryReportsResponse(object):

    """Implementation of the 'Check delivery reports response' model.

    TODO: type model description here.

    Attributes:
        delivery_reports (list of DeliveryReport): The oldest 100 unconfirmed
            delivery reports

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "delivery_reports":'delivery_reports'
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
        delivery_reports = None
        if dictionary.get('delivery_reports') != None:
            delivery_reports = list()
            for structure in dictionary.get('delivery_reports'):
                delivery_reports.append(message_media_messages.models.delivery_report.DeliveryReport.from_dictionary(structure))

        # Return an object of this model
        return cls(delivery_reports)



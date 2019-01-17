# -*- coding: utf-8 -*-

"""
    message_media_messages

    This file was automatically generated for MessageMedia by APIMATIC v2.0 ( https://apimatic.io ).
"""


class VendorAccountId(object):

    """Implementation of the 'VendorAccountId' model.

    TODO: type model description here.

    Attributes:
        vendor_id (string): TODO: type description here.
        account_id (string): The account used to submit the original message.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "vendor_id":'vendor_id',
        "account_id":'account_id'
    }

    def __init__(self,
                 vendor_id=None,
                 account_id=None):
        """Constructor for the VendorAccountId class"""

        # Initialize members of the class
        self.vendor_id = vendor_id
        self.account_id = account_id


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
        vendor_id = dictionary.get('vendor_id')
        account_id = dictionary.get('account_id')

        # Return an object of this model
        return cls(vendor_id,
                   account_id)



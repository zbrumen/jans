# coding: utf-8

"""
    SCIM API

    Gluu SCIM 2.0 server API. Developers can think of SCIM as a REST API with endpoints exposing CRUD functionality (create, update, retrieve and delete) for identity management resources such as users, groups, and fido devices.   # noqa: E501

    OpenAPI spec version: 4.2.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Address(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'formatted': 'str',
        'street_address': 'str',
        'locality': 'str',
        'region': 'str',
        'postal_code': 'str',
        'country': 'str',
        'type': 'str',
        'primary': 'bool'
    }

    attribute_map = {
        'formatted': 'formatted',
        'street_address': 'streetAddress',
        'locality': 'locality',
        'region': 'region',
        'postal_code': 'postalCode',
        'country': 'country',
        'type': 'type',
        'primary': 'primary'
    }

    def __init__(self, formatted=None, street_address=None, locality=None, region=None, postal_code=None, country=None, type=None, primary=None):  # noqa: E501
        """Address - a model defined in Swagger"""  # noqa: E501
        self._formatted = None
        self._street_address = None
        self._locality = None
        self._region = None
        self._postal_code = None
        self._country = None
        self._type = None
        self._primary = None
        self.discriminator = None
        if formatted is not None:
            self.formatted = formatted
        if street_address is not None:
            self.street_address = street_address
        if locality is not None:
            self.locality = locality
        if region is not None:
            self.region = region
        if postal_code is not None:
            self.postal_code = postal_code
        if country is not None:
            self.country = country
        if type is not None:
            self.type = type
        if primary is not None:
            self.primary = primary

    @property
    def formatted(self):
        """Gets the formatted of this Address.  # noqa: E501


        :return: The formatted of this Address.  # noqa: E501
        :rtype: str
        """
        return self._formatted

    @formatted.setter
    def formatted(self, formatted):
        """Sets the formatted of this Address.


        :param formatted: The formatted of this Address.  # noqa: E501
        :type: str
        """

        self._formatted = formatted

    @property
    def street_address(self):
        """Gets the street_address of this Address.  # noqa: E501


        :return: The street_address of this Address.  # noqa: E501
        :rtype: str
        """
        return self._street_address

    @street_address.setter
    def street_address(self, street_address):
        """Sets the street_address of this Address.


        :param street_address: The street_address of this Address.  # noqa: E501
        :type: str
        """

        self._street_address = street_address

    @property
    def locality(self):
        """Gets the locality of this Address.  # noqa: E501


        :return: The locality of this Address.  # noqa: E501
        :rtype: str
        """
        return self._locality

    @locality.setter
    def locality(self, locality):
        """Sets the locality of this Address.


        :param locality: The locality of this Address.  # noqa: E501
        :type: str
        """

        self._locality = locality

    @property
    def region(self):
        """Gets the region of this Address.  # noqa: E501


        :return: The region of this Address.  # noqa: E501
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this Address.


        :param region: The region of this Address.  # noqa: E501
        :type: str
        """

        self._region = region

    @property
    def postal_code(self):
        """Gets the postal_code of this Address.  # noqa: E501


        :return: The postal_code of this Address.  # noqa: E501
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """Sets the postal_code of this Address.


        :param postal_code: The postal_code of this Address.  # noqa: E501
        :type: str
        """

        self._postal_code = postal_code

    @property
    def country(self):
        """Gets the country of this Address.  # noqa: E501


        :return: The country of this Address.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this Address.


        :param country: The country of this Address.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def type(self):
        """Gets the type of this Address.  # noqa: E501


        :return: The type of this Address.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Address.


        :param type: The type of this Address.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def primary(self):
        """Gets the primary of this Address.  # noqa: E501


        :return: The primary of this Address.  # noqa: E501
        :rtype: bool
        """
        return self._primary

    @primary.setter
    def primary(self, primary):
        """Sets the primary of this Address.


        :param primary: The primary of this Address.  # noqa: E501
        :type: bool
        """

        self._primary = primary

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Address, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Address):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

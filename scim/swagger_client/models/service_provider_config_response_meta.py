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

class ServiceProviderConfigResponseMeta(object):
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
        'resource_type': 'str',
        'location': 'str'
    }

    attribute_map = {
        'resource_type': 'resourceType',
        'location': 'location'
    }

    def __init__(self, resource_type=None, location=None):  # noqa: E501
        """ServiceProviderConfigResponseMeta - a model defined in Swagger"""  # noqa: E501
        self._resource_type = None
        self._location = None
        self.discriminator = None
        if resource_type is not None:
            self.resource_type = resource_type
        if location is not None:
            self.location = location

    @property
    def resource_type(self):
        """Gets the resource_type of this ServiceProviderConfigResponseMeta.  # noqa: E501


        :return: The resource_type of this ServiceProviderConfigResponseMeta.  # noqa: E501
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this ServiceProviderConfigResponseMeta.


        :param resource_type: The resource_type of this ServiceProviderConfigResponseMeta.  # noqa: E501
        :type: str
        """

        self._resource_type = resource_type

    @property
    def location(self):
        """Gets the location of this ServiceProviderConfigResponseMeta.  # noqa: E501


        :return: The location of this ServiceProviderConfigResponseMeta.  # noqa: E501
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this ServiceProviderConfigResponseMeta.


        :param location: The location of this ServiceProviderConfigResponseMeta.  # noqa: E501
        :type: str
        """

        self._location = location

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
        if issubclass(ServiceProviderConfigResponseMeta, dict):
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
        if not isinstance(other, ServiceProviderConfigResponseMeta):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

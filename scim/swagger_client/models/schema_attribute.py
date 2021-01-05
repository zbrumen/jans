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

class SchemaAttribute(object):
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
        'name': 'str',
        'type': 'str',
        'sub_attributes': 'list[SchemaAttribute]',
        'multi_valued': 'bool',
        'description': 'str',
        'required': 'str',
        'canonical_values': 'list[str]',
        'case_exact': 'bool',
        'mutability': 'str',
        'returned': 'str',
        'uniqueness': 'str',
        'reference_types': 'list[str]'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'sub_attributes': 'subAttributes',
        'multi_valued': 'multiValued',
        'description': 'description',
        'required': 'required',
        'canonical_values': 'canonicalValues',
        'case_exact': 'caseExact',
        'mutability': 'mutability',
        'returned': 'returned',
        'uniqueness': 'uniqueness',
        'reference_types': 'referenceTypes'
    }

    def __init__(self, name=None, type=None, sub_attributes=None, multi_valued=None, description=None, required=None, canonical_values=None, case_exact=None, mutability=None, returned=None, uniqueness=None, reference_types=None):  # noqa: E501
        """SchemaAttribute - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._type = None
        self._sub_attributes = None
        self._multi_valued = None
        self._description = None
        self._required = None
        self._canonical_values = None
        self._case_exact = None
        self._mutability = None
        self._returned = None
        self._uniqueness = None
        self._reference_types = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if sub_attributes is not None:
            self.sub_attributes = sub_attributes
        if multi_valued is not None:
            self.multi_valued = multi_valued
        if description is not None:
            self.description = description
        if required is not None:
            self.required = required
        if canonical_values is not None:
            self.canonical_values = canonical_values
        if case_exact is not None:
            self.case_exact = case_exact
        if mutability is not None:
            self.mutability = mutability
        if returned is not None:
            self.returned = returned
        if uniqueness is not None:
            self.uniqueness = uniqueness
        if reference_types is not None:
            self.reference_types = reference_types

    @property
    def name(self):
        """Gets the name of this SchemaAttribute.  # noqa: E501


        :return: The name of this SchemaAttribute.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SchemaAttribute.


        :param name: The name of this SchemaAttribute.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def type(self):
        """Gets the type of this SchemaAttribute.  # noqa: E501


        :return: The type of this SchemaAttribute.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SchemaAttribute.


        :param type: The type of this SchemaAttribute.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def sub_attributes(self):
        """Gets the sub_attributes of this SchemaAttribute.  # noqa: E501


        :return: The sub_attributes of this SchemaAttribute.  # noqa: E501
        :rtype: list[SchemaAttribute]
        """
        return self._sub_attributes

    @sub_attributes.setter
    def sub_attributes(self, sub_attributes):
        """Sets the sub_attributes of this SchemaAttribute.


        :param sub_attributes: The sub_attributes of this SchemaAttribute.  # noqa: E501
        :type: list[SchemaAttribute]
        """

        self._sub_attributes = sub_attributes

    @property
    def multi_valued(self):
        """Gets the multi_valued of this SchemaAttribute.  # noqa: E501


        :return: The multi_valued of this SchemaAttribute.  # noqa: E501
        :rtype: bool
        """
        return self._multi_valued

    @multi_valued.setter
    def multi_valued(self, multi_valued):
        """Sets the multi_valued of this SchemaAttribute.


        :param multi_valued: The multi_valued of this SchemaAttribute.  # noqa: E501
        :type: bool
        """

        self._multi_valued = multi_valued

    @property
    def description(self):
        """Gets the description of this SchemaAttribute.  # noqa: E501


        :return: The description of this SchemaAttribute.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this SchemaAttribute.


        :param description: The description of this SchemaAttribute.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def required(self):
        """Gets the required of this SchemaAttribute.  # noqa: E501


        :return: The required of this SchemaAttribute.  # noqa: E501
        :rtype: str
        """
        return self._required

    @required.setter
    def required(self, required):
        """Sets the required of this SchemaAttribute.


        :param required: The required of this SchemaAttribute.  # noqa: E501
        :type: str
        """

        self._required = required

    @property
    def canonical_values(self):
        """Gets the canonical_values of this SchemaAttribute.  # noqa: E501


        :return: The canonical_values of this SchemaAttribute.  # noqa: E501
        :rtype: list[str]
        """
        return self._canonical_values

    @canonical_values.setter
    def canonical_values(self, canonical_values):
        """Sets the canonical_values of this SchemaAttribute.


        :param canonical_values: The canonical_values of this SchemaAttribute.  # noqa: E501
        :type: list[str]
        """

        self._canonical_values = canonical_values

    @property
    def case_exact(self):
        """Gets the case_exact of this SchemaAttribute.  # noqa: E501


        :return: The case_exact of this SchemaAttribute.  # noqa: E501
        :rtype: bool
        """
        return self._case_exact

    @case_exact.setter
    def case_exact(self, case_exact):
        """Sets the case_exact of this SchemaAttribute.


        :param case_exact: The case_exact of this SchemaAttribute.  # noqa: E501
        :type: bool
        """

        self._case_exact = case_exact

    @property
    def mutability(self):
        """Gets the mutability of this SchemaAttribute.  # noqa: E501


        :return: The mutability of this SchemaAttribute.  # noqa: E501
        :rtype: str
        """
        return self._mutability

    @mutability.setter
    def mutability(self, mutability):
        """Sets the mutability of this SchemaAttribute.


        :param mutability: The mutability of this SchemaAttribute.  # noqa: E501
        :type: str
        """

        self._mutability = mutability

    @property
    def returned(self):
        """Gets the returned of this SchemaAttribute.  # noqa: E501


        :return: The returned of this SchemaAttribute.  # noqa: E501
        :rtype: str
        """
        return self._returned

    @returned.setter
    def returned(self, returned):
        """Sets the returned of this SchemaAttribute.


        :param returned: The returned of this SchemaAttribute.  # noqa: E501
        :type: str
        """

        self._returned = returned

    @property
    def uniqueness(self):
        """Gets the uniqueness of this SchemaAttribute.  # noqa: E501


        :return: The uniqueness of this SchemaAttribute.  # noqa: E501
        :rtype: str
        """
        return self._uniqueness

    @uniqueness.setter
    def uniqueness(self, uniqueness):
        """Sets the uniqueness of this SchemaAttribute.


        :param uniqueness: The uniqueness of this SchemaAttribute.  # noqa: E501
        :type: str
        """

        self._uniqueness = uniqueness

    @property
    def reference_types(self):
        """Gets the reference_types of this SchemaAttribute.  # noqa: E501


        :return: The reference_types of this SchemaAttribute.  # noqa: E501
        :rtype: list[str]
        """
        return self._reference_types

    @reference_types.setter
    def reference_types(self, reference_types):
        """Sets the reference_types of this SchemaAttribute.


        :param reference_types: The reference_types of this SchemaAttribute.  # noqa: E501
        :type: list[str]
        """

        self._reference_types = reference_types

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
        if issubclass(SchemaAttribute, dict):
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
        if not isinstance(other, SchemaAttribute):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

# coding: utf-8

"""
    jans-config-api

    jans-config-api - Authorization services  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: xxx@gluu.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class GluuAttribute(object):
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
        'dn': 'str',
        'inum': 'str',
        'selected': 'bool',
        'name': 'str',
        'display_name': 'str',
        'description': 'str',
        'data_type': 'str',
        'status': 'str',
        'lifetime': 'str',
        'source_attribute': 'str',
        'salt': 'str',
        'name_id_type': 'str',
        'origin': 'str',
        'edit_type': 'list[str]',
        'view_type': 'list[str]',
        'usage_type': 'list[str]',
        'claim_name': 'str',
        'see_also': 'str',
        'saml1_uri': 'str',
        'saml2_uri': 'str',
        'urn': 'str',
        'scim_custom_attr': 'bool',
        'ox_multi_valued_attribute': 'bool',
        'custom': 'bool',
        'requred': 'bool',
        'attribute_validation': 'GluuAttributeAttributeValidation',
        'tooltip': 'str'
    }

    attribute_map = {
        'dn': 'dn',
        'inum': 'inum',
        'selected': 'selected',
        'name': 'name',
        'display_name': 'displayName',
        'description': 'description',
        'data_type': 'dataType',
        'status': 'status',
        'lifetime': 'lifetime',
        'source_attribute': 'sourceAttribute',
        'salt': 'salt',
        'name_id_type': 'nameIdType',
        'origin': 'origin',
        'edit_type': 'editType',
        'view_type': 'viewType',
        'usage_type': 'usageType',
        'claim_name': 'claimName',
        'see_also': 'seeAlso',
        'saml1_uri': 'saml1Uri',
        'saml2_uri': 'saml2Uri',
        'urn': 'urn',
        'scim_custom_attr': 'scimCustomAttr',
        'ox_multi_valued_attribute': 'oxMultiValuedAttribute',
        'custom': 'custom',
        'requred': 'requred',
        'attribute_validation': 'attributeValidation',
        'tooltip': 'tooltip'
    }

    def __init__(self, dn=None, inum=None, selected=None, name=None, display_name=None, description=None, data_type=None, status=None, lifetime=None, source_attribute=None, salt=None, name_id_type=None, origin=None, edit_type=None, view_type=None, usage_type=None, claim_name=None, see_also=None, saml1_uri=None, saml2_uri=None, urn=None, scim_custom_attr=None, ox_multi_valued_attribute=None, custom=None, requred=None, attribute_validation=None, tooltip=None):  # noqa: E501
        """GluuAttribute - a model defined in Swagger"""  # noqa: E501
        self._dn = None
        self._inum = None
        self._selected = None
        self._name = None
        self._display_name = None
        self._description = None
        self._data_type = None
        self._status = None
        self._lifetime = None
        self._source_attribute = None
        self._salt = None
        self._name_id_type = None
        self._origin = None
        self._edit_type = None
        self._view_type = None
        self._usage_type = None
        self._claim_name = None
        self._see_also = None
        self._saml1_uri = None
        self._saml2_uri = None
        self._urn = None
        self._scim_custom_attr = None
        self._ox_multi_valued_attribute = None
        self._custom = None
        self._requred = None
        self._attribute_validation = None
        self._tooltip = None
        self.discriminator = None
        if dn is not None:
            self.dn = dn
        if inum is not None:
            self.inum = inum
        if selected is not None:
            self.selected = selected
        if name is not None:
            self.name = name
        if display_name is not None:
            self.display_name = display_name
        if description is not None:
            self.description = description
        if data_type is not None:
            self.data_type = data_type
        if status is not None:
            self.status = status
        if lifetime is not None:
            self.lifetime = lifetime
        if source_attribute is not None:
            self.source_attribute = source_attribute
        if salt is not None:
            self.salt = salt
        if name_id_type is not None:
            self.name_id_type = name_id_type
        if origin is not None:
            self.origin = origin
        if edit_type is not None:
            self.edit_type = edit_type
        if view_type is not None:
            self.view_type = view_type
        if usage_type is not None:
            self.usage_type = usage_type
        if claim_name is not None:
            self.claim_name = claim_name
        if see_also is not None:
            self.see_also = see_also
        if saml1_uri is not None:
            self.saml1_uri = saml1_uri
        if saml2_uri is not None:
            self.saml2_uri = saml2_uri
        if urn is not None:
            self.urn = urn
        if scim_custom_attr is not None:
            self.scim_custom_attr = scim_custom_attr
        if ox_multi_valued_attribute is not None:
            self.ox_multi_valued_attribute = ox_multi_valued_attribute
        if custom is not None:
            self.custom = custom
        if requred is not None:
            self.requred = requred
        if attribute_validation is not None:
            self.attribute_validation = attribute_validation
        if tooltip is not None:
            self.tooltip = tooltip

    @property
    def dn(self):
        """Gets the dn of this GluuAttribute.  # noqa: E501


        :return: The dn of this GluuAttribute.  # noqa: E501
        :rtype: str
        """
        return self._dn

    @dn.setter
    def dn(self, dn):
        """Sets the dn of this GluuAttribute.


        :param dn: The dn of this GluuAttribute.  # noqa: E501
        :type: str
        """

        self._dn = dn

    @property
    def inum(self):
        """Gets the inum of this GluuAttribute.  # noqa: E501

        XRI i-number. Identifier to uniquely identify the attribute.  # noqa: E501

        :return: The inum of this GluuAttribute.  # noqa: E501
        :rtype: str
        """
        return self._inum

    @inum.setter
    def inum(self, inum):
        """Sets the inum of this GluuAttribute.

        XRI i-number. Identifier to uniquely identify the attribute.  # noqa: E501

        :param inum: The inum of this GluuAttribute.  # noqa: E501
        :type: str
        """

        self._inum = inum

    @property
    def selected(self):
        """Gets the selected of this GluuAttribute.  # noqa: E501

        Boolean value to indicate if the atrribute is selected.  # noqa: E501

        :return: The selected of this GluuAttribute.  # noqa: E501
        :rtype: bool
        """
        return self._selected

    @selected.setter
    def selected(self, selected):
        """Sets the selected of this GluuAttribute.

        Boolean value to indicate if the atrribute is selected.  # noqa: E501

        :param selected: The selected of this GluuAttribute.  # noqa: E501
        :type: bool
        """

        self._selected = selected

    @property
    def name(self):
        """Gets the name of this GluuAttribute.  # noqa: E501

        Name of the attribute.  # noqa: E501

        :return: The name of this GluuAttribute.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GluuAttribute.

        Name of the attribute.  # noqa: E501

        :param name: The name of this GluuAttribute.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def display_name(self):
        """Gets the display_name of this GluuAttribute.  # noqa: E501


        :return: The display_name of this GluuAttribute.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this GluuAttribute.


        :param display_name: The display_name of this GluuAttribute.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def description(self):
        """Gets the description of this GluuAttribute.  # noqa: E501

        User friendly descriptive detail of attribute.  # noqa: E501

        :return: The description of this GluuAttribute.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this GluuAttribute.

        User friendly descriptive detail of attribute.  # noqa: E501

        :param description: The description of this GluuAttribute.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def data_type(self):
        """Gets the data_type of this GluuAttribute.  # noqa: E501

        Data Type of attribute.  # noqa: E501

        :return: The data_type of this GluuAttribute.  # noqa: E501
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        """Sets the data_type of this GluuAttribute.

        Data Type of attribute.  # noqa: E501

        :param data_type: The data_type of this GluuAttribute.  # noqa: E501
        :type: str
        """
        allowed_values = ["STRING", "NUMERIC", "BOOLEAN", "BINARY", "CERTIFICATE", "DATE"]  # noqa: E501
        if data_type not in allowed_values:
            raise ValueError(
                "Invalid value for `data_type` ({0}), must be one of {1}"  # noqa: E501
                .format(data_type, allowed_values)
            )

        self._data_type = data_type

    @property
    def status(self):
        """Gets the status of this GluuAttribute.  # noqa: E501

        Attrubute status  # noqa: E501

        :return: The status of this GluuAttribute.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this GluuAttribute.

        Attrubute status  # noqa: E501

        :param status: The status of this GluuAttribute.  # noqa: E501
        :type: str
        """
        allowed_values = ["ACTIVE", "INACTIVE", "EXPIRED", "REGISTER"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def lifetime(self):
        """Gets the lifetime of this GluuAttribute.  # noqa: E501


        :return: The lifetime of this GluuAttribute.  # noqa: E501
        :rtype: str
        """
        return self._lifetime

    @lifetime.setter
    def lifetime(self, lifetime):
        """Sets the lifetime of this GluuAttribute.


        :param lifetime: The lifetime of this GluuAttribute.  # noqa: E501
        :type: str
        """

        self._lifetime = lifetime

    @property
    def source_attribute(self):
        """Gets the source_attribute of this GluuAttribute.  # noqa: E501


        :return: The source_attribute of this GluuAttribute.  # noqa: E501
        :rtype: str
        """
        return self._source_attribute

    @source_attribute.setter
    def source_attribute(self, source_attribute):
        """Sets the source_attribute of this GluuAttribute.


        :param source_attribute: The source_attribute of this GluuAttribute.  # noqa: E501
        :type: str
        """

        self._source_attribute = source_attribute

    @property
    def salt(self):
        """Gets the salt of this GluuAttribute.  # noqa: E501


        :return: The salt of this GluuAttribute.  # noqa: E501
        :rtype: str
        """
        return self._salt

    @salt.setter
    def salt(self, salt):
        """Sets the salt of this GluuAttribute.


        :param salt: The salt of this GluuAttribute.  # noqa: E501
        :type: str
        """

        self._salt = salt

    @property
    def name_id_type(self):
        """Gets the name_id_type of this GluuAttribute.  # noqa: E501


        :return: The name_id_type of this GluuAttribute.  # noqa: E501
        :rtype: str
        """
        return self._name_id_type

    @name_id_type.setter
    def name_id_type(self, name_id_type):
        """Sets the name_id_type of this GluuAttribute.


        :param name_id_type: The name_id_type of this GluuAttribute.  # noqa: E501
        :type: str
        """

        self._name_id_type = name_id_type

    @property
    def origin(self):
        """Gets the origin of this GluuAttribute.  # noqa: E501


        :return: The origin of this GluuAttribute.  # noqa: E501
        :rtype: str
        """
        return self._origin

    @origin.setter
    def origin(self, origin):
        """Sets the origin of this GluuAttribute.


        :param origin: The origin of this GluuAttribute.  # noqa: E501
        :type: str
        """

        self._origin = origin

    @property
    def edit_type(self):
        """Gets the edit_type of this GluuAttribute.  # noqa: E501

        GluuUserRole  # noqa: E501

        :return: The edit_type of this GluuAttribute.  # noqa: E501
        :rtype: list[str]
        """
        return self._edit_type

    @edit_type.setter
    def edit_type(self, edit_type):
        """Sets the edit_type of this GluuAttribute.

        GluuUserRole  # noqa: E501

        :param edit_type: The edit_type of this GluuAttribute.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["ADMIN", "OWNER", "MANAGER", "USER", "WHITEPAGES"]  # noqa: E501
        if not set(edit_type).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `edit_type` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(edit_type) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._edit_type = edit_type

    @property
    def view_type(self):
        """Gets the view_type of this GluuAttribute.  # noqa: E501

        GluuUserRole  # noqa: E501

        :return: The view_type of this GluuAttribute.  # noqa: E501
        :rtype: list[str]
        """
        return self._view_type

    @view_type.setter
    def view_type(self, view_type):
        """Sets the view_type of this GluuAttribute.

        GluuUserRole  # noqa: E501

        :param view_type: The view_type of this GluuAttribute.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["ADMIN", "OWNER", "MANAGER", "USER", "WHITEPAGES"]  # noqa: E501
        if not set(view_type).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `view_type` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(view_type) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._view_type = view_type

    @property
    def usage_type(self):
        """Gets the usage_type of this GluuAttribute.  # noqa: E501

        GluuAttributeUsageType  # noqa: E501

        :return: The usage_type of this GluuAttribute.  # noqa: E501
        :rtype: list[str]
        """
        return self._usage_type

    @usage_type.setter
    def usage_type(self, usage_type):
        """Sets the usage_type of this GluuAttribute.

        GluuAttributeUsageType  # noqa: E501

        :param usage_type: The usage_type of this GluuAttribute.  # noqa: E501
        :type: list[str]
        """

        self._usage_type = usage_type

    @property
    def claim_name(self):
        """Gets the claim_name of this GluuAttribute.  # noqa: E501


        :return: The claim_name of this GluuAttribute.  # noqa: E501
        :rtype: str
        """
        return self._claim_name

    @claim_name.setter
    def claim_name(self, claim_name):
        """Sets the claim_name of this GluuAttribute.


        :param claim_name: The claim_name of this GluuAttribute.  # noqa: E501
        :type: str
        """

        self._claim_name = claim_name

    @property
    def see_also(self):
        """Gets the see_also of this GluuAttribute.  # noqa: E501


        :return: The see_also of this GluuAttribute.  # noqa: E501
        :rtype: str
        """
        return self._see_also

    @see_also.setter
    def see_also(self, see_also):
        """Sets the see_also of this GluuAttribute.


        :param see_also: The see_also of this GluuAttribute.  # noqa: E501
        :type: str
        """

        self._see_also = see_also

    @property
    def saml1_uri(self):
        """Gets the saml1_uri of this GluuAttribute.  # noqa: E501


        :return: The saml1_uri of this GluuAttribute.  # noqa: E501
        :rtype: str
        """
        return self._saml1_uri

    @saml1_uri.setter
    def saml1_uri(self, saml1_uri):
        """Sets the saml1_uri of this GluuAttribute.


        :param saml1_uri: The saml1_uri of this GluuAttribute.  # noqa: E501
        :type: str
        """

        self._saml1_uri = saml1_uri

    @property
    def saml2_uri(self):
        """Gets the saml2_uri of this GluuAttribute.  # noqa: E501


        :return: The saml2_uri of this GluuAttribute.  # noqa: E501
        :rtype: str
        """
        return self._saml2_uri

    @saml2_uri.setter
    def saml2_uri(self, saml2_uri):
        """Sets the saml2_uri of this GluuAttribute.


        :param saml2_uri: The saml2_uri of this GluuAttribute.  # noqa: E501
        :type: str
        """

        self._saml2_uri = saml2_uri

    @property
    def urn(self):
        """Gets the urn of this GluuAttribute.  # noqa: E501


        :return: The urn of this GluuAttribute.  # noqa: E501
        :rtype: str
        """
        return self._urn

    @urn.setter
    def urn(self, urn):
        """Sets the urn of this GluuAttribute.


        :param urn: The urn of this GluuAttribute.  # noqa: E501
        :type: str
        """

        self._urn = urn

    @property
    def scim_custom_attr(self):
        """Gets the scim_custom_attr of this GluuAttribute.  # noqa: E501

        Boolean value indicating if the attribute is a SCIM custom attribute  # noqa: E501

        :return: The scim_custom_attr of this GluuAttribute.  # noqa: E501
        :rtype: bool
        """
        return self._scim_custom_attr

    @scim_custom_attr.setter
    def scim_custom_attr(self, scim_custom_attr):
        """Sets the scim_custom_attr of this GluuAttribute.

        Boolean value indicating if the attribute is a SCIM custom attribute  # noqa: E501

        :param scim_custom_attr: The scim_custom_attr of this GluuAttribute.  # noqa: E501
        :type: bool
        """

        self._scim_custom_attr = scim_custom_attr

    @property
    def ox_multi_valued_attribute(self):
        """Gets the ox_multi_valued_attribute of this GluuAttribute.  # noqa: E501

        Boolean value indicating if the attribute can hold multiple value.  # noqa: E501

        :return: The ox_multi_valued_attribute of this GluuAttribute.  # noqa: E501
        :rtype: bool
        """
        return self._ox_multi_valued_attribute

    @ox_multi_valued_attribute.setter
    def ox_multi_valued_attribute(self, ox_multi_valued_attribute):
        """Sets the ox_multi_valued_attribute of this GluuAttribute.

        Boolean value indicating if the attribute can hold multiple value.  # noqa: E501

        :param ox_multi_valued_attribute: The ox_multi_valued_attribute of this GluuAttribute.  # noqa: E501
        :type: bool
        """

        self._ox_multi_valued_attribute = ox_multi_valued_attribute

    @property
    def custom(self):
        """Gets the custom of this GluuAttribute.  # noqa: E501

        Boolean value indicating if the attribute is a custom attribute  # noqa: E501

        :return: The custom of this GluuAttribute.  # noqa: E501
        :rtype: bool
        """
        return self._custom

    @custom.setter
    def custom(self, custom):
        """Sets the custom of this GluuAttribute.

        Boolean value indicating if the attribute is a custom attribute  # noqa: E501

        :param custom: The custom of this GluuAttribute.  # noqa: E501
        :type: bool
        """

        self._custom = custom

    @property
    def requred(self):
        """Gets the requred of this GluuAttribute.  # noqa: E501

        Boolean value indicating is a mandatory attribute  # noqa: E501

        :return: The requred of this GluuAttribute.  # noqa: E501
        :rtype: bool
        """
        return self._requred

    @requred.setter
    def requred(self, requred):
        """Sets the requred of this GluuAttribute.

        Boolean value indicating is a mandatory attribute  # noqa: E501

        :param requred: The requred of this GluuAttribute.  # noqa: E501
        :type: bool
        """

        self._requred = requred

    @property
    def attribute_validation(self):
        """Gets the attribute_validation of this GluuAttribute.  # noqa: E501


        :return: The attribute_validation of this GluuAttribute.  # noqa: E501
        :rtype: GluuAttributeAttributeValidation
        """
        return self._attribute_validation

    @attribute_validation.setter
    def attribute_validation(self, attribute_validation):
        """Sets the attribute_validation of this GluuAttribute.


        :param attribute_validation: The attribute_validation of this GluuAttribute.  # noqa: E501
        :type: GluuAttributeAttributeValidation
        """

        self._attribute_validation = attribute_validation

    @property
    def tooltip(self):
        """Gets the tooltip of this GluuAttribute.  # noqa: E501


        :return: The tooltip of this GluuAttribute.  # noqa: E501
        :rtype: str
        """
        return self._tooltip

    @tooltip.setter
    def tooltip(self, tooltip):
        """Sets the tooltip of this GluuAttribute.


        :param tooltip: The tooltip of this GluuAttribute.  # noqa: E501
        :type: str
        """

        self._tooltip = tooltip

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
        if issubclass(GluuAttribute, dict):
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
        if not isinstance(other, GluuAttribute):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

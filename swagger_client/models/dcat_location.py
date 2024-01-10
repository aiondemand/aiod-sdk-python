# coding: utf-8

"""
    FastAPI

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class DcatLocation(object):
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
        'id': 'object',
        'type': 'object',
        'dcatbbox': 'object',
        'dcatcentroid': 'object',
        'dcatgeometry': 'object'
    }

    attribute_map = {
        'id': '@id',
        'type': '@type',
        'dcatbbox': 'dcat:bbox',
        'dcatcentroid': 'dcat:centroid',
        'dcatgeometry': 'dcat:geometry'
    }

    def __init__(self, id=None, type=None, dcatbbox=None, dcatcentroid=None, dcatgeometry=None):  # noqa: E501
        """DcatLocation - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._type = None
        self._dcatbbox = None
        self._dcatcentroid = None
        self._dcatgeometry = None
        self.discriminator = None
        self.id = id
        if type is not None:
            self.type = type
        if dcatbbox is not None:
            self.dcatbbox = dcatbbox
        if dcatcentroid is not None:
            self.dcatcentroid = dcatcentroid
        if dcatgeometry is not None:
            self.dcatgeometry = dcatgeometry

    @property
    def id(self):
        """Gets the id of this DcatLocation.  # noqa: E501


        :return: The id of this DcatLocation.  # noqa: E501
        :rtype: object
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DcatLocation.


        :param id: The id of this DcatLocation.  # noqa: E501
        :type: object
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def type(self):
        """Gets the type of this DcatLocation.  # noqa: E501


        :return: The type of this DcatLocation.  # noqa: E501
        :rtype: object
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this DcatLocation.


        :param type: The type of this DcatLocation.  # noqa: E501
        :type: object
        """

        self._type = type

    @property
    def dcatbbox(self):
        """Gets the dcatbbox of this DcatLocation.  # noqa: E501


        :return: The dcatbbox of this DcatLocation.  # noqa: E501
        :rtype: object
        """
        return self._dcatbbox

    @dcatbbox.setter
    def dcatbbox(self, dcatbbox):
        """Sets the dcatbbox of this DcatLocation.


        :param dcatbbox: The dcatbbox of this DcatLocation.  # noqa: E501
        :type: object
        """

        self._dcatbbox = dcatbbox

    @property
    def dcatcentroid(self):
        """Gets the dcatcentroid of this DcatLocation.  # noqa: E501


        :return: The dcatcentroid of this DcatLocation.  # noqa: E501
        :rtype: object
        """
        return self._dcatcentroid

    @dcatcentroid.setter
    def dcatcentroid(self, dcatcentroid):
        """Sets the dcatcentroid of this DcatLocation.


        :param dcatcentroid: The dcatcentroid of this DcatLocation.  # noqa: E501
        :type: object
        """

        self._dcatcentroid = dcatcentroid

    @property
    def dcatgeometry(self):
        """Gets the dcatgeometry of this DcatLocation.  # noqa: E501


        :return: The dcatgeometry of this DcatLocation.  # noqa: E501
        :rtype: object
        """
        return self._dcatgeometry

    @dcatgeometry.setter
    def dcatgeometry(self, dcatgeometry):
        """Sets the dcatgeometry of this DcatLocation.


        :param dcatgeometry: The dcatgeometry of this DcatLocation.  # noqa: E501
        :type: object
        """

        self._dcatgeometry = dcatgeometry

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
        if issubclass(DcatLocation, dict):
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
        if not isinstance(other, DcatLocation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
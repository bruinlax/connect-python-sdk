# coding: utf-8

"""
    Square Connect API


    OpenAPI spec version: 2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from pprint import pformat
from six import iteritems
import re


class ListRefundsResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, errors=None, refunds=None, cursor=None):
        """
        ListRefundsResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'errors': 'list[Error]',
            'refunds': 'list[Refund]',
            'cursor': 'str'
        }

        self.attribute_map = {
            'errors': 'errors',
            'refunds': 'refunds',
            'cursor': 'cursor'
        }

        self._errors = errors
        self._refunds = refunds
        self._cursor = cursor

    @property
    def errors(self):
        """
        Gets the errors of this ListRefundsResponse.
        Any errors that occurred during the request.

        :return: The errors of this ListRefundsResponse.
        :rtype: list[Error]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """
        Sets the errors of this ListRefundsResponse.
        Any errors that occurred during the request.

        :param errors: The errors of this ListRefundsResponse.
        :type: list[Error]
        """

        self._errors = errors

    @property
    def refunds(self):
        """
        Gets the refunds of this ListRefundsResponse.
        An array of refunds that match your query.

        :return: The refunds of this ListRefundsResponse.
        :rtype: list[Refund]
        """
        return self._refunds

    @refunds.setter
    def refunds(self, refunds):
        """
        Sets the refunds of this ListRefundsResponse.
        An array of refunds that match your query.

        :param refunds: The refunds of this ListRefundsResponse.
        :type: list[Refund]
        """

        self._refunds = refunds

    @property
    def cursor(self):
        """
        Gets the cursor of this ListRefundsResponse.
        A pagination cursor for retrieving the next set of results, if any remain.  Provide this value as the `cursor` parameter in a subsequent request to the **ListTenderRefunds** endpoint.

        :return: The cursor of this ListRefundsResponse.
        :rtype: str
        """
        return self._cursor

    @cursor.setter
    def cursor(self, cursor):
        """
        Sets the cursor of this ListRefundsResponse.
        A pagination cursor for retrieving the next set of results, if any remain.  Provide this value as the `cursor` parameter in a subsequent request to the **ListTenderRefunds** endpoint.

        :param cursor: The cursor of this ListRefundsResponse.
        :type: str
        """

        self._cursor = cursor

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

# coding: utf-8

"""
Copyright 2016 Square, Inc.

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


class OrderLineItem(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, name=None, quantity=None, base_price_money=None, total_money=None):
        """
        OrderLineItem - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'quantity': 'str',
            'base_price_money': 'Money',
            'total_money': 'Money'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'quantity': 'quantity',
            'base_price_money': 'base_price_money',
            'total_money': 'total_money'
        }

        self._id = id
        self._name = name
        self._quantity = quantity
        self._base_price_money = base_price_money
        self._total_money = total_money

    @property
    def id(self):
        """
        Gets the id of this OrderLineItem.
        The line item's ID, unique only within this order.

        :return: The id of this OrderLineItem.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this OrderLineItem.
        The line item's ID, unique only within this order.

        :param id: The id of this OrderLineItem.
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this OrderLineItem.
        The name of the line item.

        :return: The name of this OrderLineItem.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this OrderLineItem.
        The name of the line item.

        :param name: The name of this OrderLineItem.
        :type: str
        """

        self._name = name

    @property
    def quantity(self):
        """
        Gets the quantity of this OrderLineItem.
        The quantity of the product to purchase. Currently, this string must have an integer value.

        :return: The quantity of this OrderLineItem.
        :rtype: str
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """
        Sets the quantity of this OrderLineItem.
        The quantity of the product to purchase. Currently, this string must have an integer value.

        :param quantity: The quantity of this OrderLineItem.
        :type: str
        """

        self._quantity = quantity

    @property
    def base_price_money(self):
        """
        Gets the base_price_money of this OrderLineItem.
        The base price for a single unit of the line item's associated variation.  If a line item represents a Custom Amount instead of a particular product, this field indicates that amount.

        :return: The base_price_money of this OrderLineItem.
        :rtype: Money
        """
        return self._base_price_money

    @base_price_money.setter
    def base_price_money(self, base_price_money):
        """
        Sets the base_price_money of this OrderLineItem.
        The base price for a single unit of the line item's associated variation.  If a line item represents a Custom Amount instead of a particular product, this field indicates that amount.

        :param base_price_money: The base_price_money of this OrderLineItem.
        :type: Money
        """

        self._base_price_money = base_price_money

    @property
    def total_money(self):
        """
        Gets the total_money of this OrderLineItem.
        The total amount of money to collect for this line item.

        :return: The total_money of this OrderLineItem.
        :rtype: Money
        """
        return self._total_money

    @total_money.setter
    def total_money(self, total_money):
        """
        Sets the total_money of this OrderLineItem.
        The total amount of money to collect for this line item.

        :param total_money: The total_money of this OrderLineItem.
        :type: Money
        """

        self._total_money = total_money

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
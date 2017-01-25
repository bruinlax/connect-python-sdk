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


class Tender(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, location_id=None, transaction_id=None, created_at=None, note=None, amount_money=None, processing_fee_money=None, customer_id=None, type=None, card_details=None, cash_details=None):
        """
        Tender - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'location_id': 'str',
            'transaction_id': 'str',
            'created_at': 'str',
            'note': 'str',
            'amount_money': 'Money',
            'processing_fee_money': 'Money',
            'customer_id': 'str',
            'type': 'str',
            'card_details': 'TenderCardDetails',
            'cash_details': 'TenderCashDetails'
        }

        self.attribute_map = {
            'id': 'id',
            'location_id': 'location_id',
            'transaction_id': 'transaction_id',
            'created_at': 'created_at',
            'note': 'note',
            'amount_money': 'amount_money',
            'processing_fee_money': 'processing_fee_money',
            'customer_id': 'customer_id',
            'type': 'type',
            'card_details': 'card_details',
            'cash_details': 'cash_details'
        }

        self._id = id
        self._location_id = location_id
        self._transaction_id = transaction_id
        self._created_at = created_at
        self._note = note
        self._amount_money = amount_money
        self._processing_fee_money = processing_fee_money
        self._customer_id = customer_id
        self._type = type
        self._card_details = card_details
        self._cash_details = cash_details

    @property
    def id(self):
        """
        Gets the id of this Tender.
        The tender's unique ID.

        :return: The id of this Tender.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Tender.
        The tender's unique ID.

        :param id: The id of this Tender.
        :type: str
        """

        self._id = id

    @property
    def location_id(self):
        """
        Gets the location_id of this Tender.
        The ID of the transaction's associated location.

        :return: The location_id of this Tender.
        :rtype: str
        """
        return self._location_id

    @location_id.setter
    def location_id(self, location_id):
        """
        Sets the location_id of this Tender.
        The ID of the transaction's associated location.

        :param location_id: The location_id of this Tender.
        :type: str
        """

        self._location_id = location_id

    @property
    def transaction_id(self):
        """
        Gets the transaction_id of this Tender.
        The ID of the tender's associated transaction.

        :return: The transaction_id of this Tender.
        :rtype: str
        """
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, transaction_id):
        """
        Sets the transaction_id of this Tender.
        The ID of the tender's associated transaction.

        :param transaction_id: The transaction_id of this Tender.
        :type: str
        """

        self._transaction_id = transaction_id

    @property
    def created_at(self):
        """
        Gets the created_at of this Tender.
        The time when the tender was created, in RFC 3339 format.

        :return: The created_at of this Tender.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this Tender.
        The time when the tender was created, in RFC 3339 format.

        :param created_at: The created_at of this Tender.
        :type: str
        """

        self._created_at = created_at

    @property
    def note(self):
        """
        Gets the note of this Tender.
        An optional note associated with the tender at the time of payment.

        :return: The note of this Tender.
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        """
        Sets the note of this Tender.
        An optional note associated with the tender at the time of payment.

        :param note: The note of this Tender.
        :type: str
        """

        self._note = note

    @property
    def amount_money(self):
        """
        Gets the amount_money of this Tender.
        The amount of the tender.

        :return: The amount_money of this Tender.
        :rtype: Money
        """
        return self._amount_money

    @amount_money.setter
    def amount_money(self, amount_money):
        """
        Sets the amount_money of this Tender.
        The amount of the tender.

        :param amount_money: The amount_money of this Tender.
        :type: Money
        """

        self._amount_money = amount_money

    @property
    def processing_fee_money(self):
        """
        Gets the processing_fee_money of this Tender.
        The amount of any Square processing fees applied to the tender.  This field is not immediately populated when a new transaction is created. It is usually available after about ten seconds.

        :return: The processing_fee_money of this Tender.
        :rtype: Money
        """
        return self._processing_fee_money

    @processing_fee_money.setter
    def processing_fee_money(self, processing_fee_money):
        """
        Sets the processing_fee_money of this Tender.
        The amount of any Square processing fees applied to the tender.  This field is not immediately populated when a new transaction is created. It is usually available after about ten seconds.

        :param processing_fee_money: The processing_fee_money of this Tender.
        :type: Money
        """

        self._processing_fee_money = processing_fee_money

    @property
    def customer_id(self):
        """
        Gets the customer_id of this Tender.
        If the tender is associated with a customer or represents a customer's card on file, this is the ID of the associated customer.

        :return: The customer_id of this Tender.
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """
        Sets the customer_id of this Tender.
        If the tender is associated with a customer or represents a customer's card on file, this is the ID of the associated customer.

        :param customer_id: The customer_id of this Tender.
        :type: str
        """

        self._customer_id = customer_id

    @property
    def type(self):
        """
        Gets the type of this Tender.
        The type of tender, such as `CARD` or `CASH`.

        :return: The type of this Tender.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this Tender.
        The type of tender, such as `CARD` or `CASH`.

        :param type: The type of this Tender.
        :type: str
        """
        allowed_values = ["CARD", "CASH", "THIRD_PARTY_CARD", "SQUARE_GIFT_CARD", "NO_SALE", "OTHER"]
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def card_details(self):
        """
        Gets the card_details of this Tender.
        The details of the card tender.  This value is present only if the value of `type` is `CARD`.

        :return: The card_details of this Tender.
        :rtype: TenderCardDetails
        """
        return self._card_details

    @card_details.setter
    def card_details(self, card_details):
        """
        Sets the card_details of this Tender.
        The details of the card tender.  This value is present only if the value of `type` is `CARD`.

        :param card_details: The card_details of this Tender.
        :type: TenderCardDetails
        """

        self._card_details = card_details

    @property
    def cash_details(self):
        """
        Gets the cash_details of this Tender.
        The details of the cash tender.  This value is present only if the value of `type` is `CASH`.

        :return: The cash_details of this Tender.
        :rtype: TenderCashDetails
        """
        return self._cash_details

    @cash_details.setter
    def cash_details(self, cash_details):
        """
        Sets the cash_details of this Tender.
        The details of the cash tender.  This value is present only if the value of `type` is `CASH`.

        :param cash_details: The cash_details of this Tender.
        :type: TenderCashDetails
        """

        self._cash_details = cash_details

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

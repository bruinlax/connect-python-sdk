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


class CreateCustomerRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, given_name=None, family_name=None, company_name=None, nickname=None, email_address=None, address=None, phone_number=None, reference_id=None, note=None):
        """
        CreateCustomerRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'given_name': 'str',
            'family_name': 'str',
            'company_name': 'str',
            'nickname': 'str',
            'email_address': 'str',
            'address': 'Address',
            'phone_number': 'str',
            'reference_id': 'str',
            'note': 'str'
        }

        self.attribute_map = {
            'given_name': 'given_name',
            'family_name': 'family_name',
            'company_name': 'company_name',
            'nickname': 'nickname',
            'email_address': 'email_address',
            'address': 'address',
            'phone_number': 'phone_number',
            'reference_id': 'reference_id',
            'note': 'note'
        }

        self._given_name = given_name
        self._family_name = family_name
        self._company_name = company_name
        self._nickname = nickname
        self._email_address = email_address
        self._address = address
        self._phone_number = phone_number
        self._reference_id = reference_id
        self._note = note

    @property
    def given_name(self):
        """
        Gets the given_name of this CreateCustomerRequest.
        

        :return: The given_name of this CreateCustomerRequest.
        :rtype: str
        """
        return self._given_name

    @given_name.setter
    def given_name(self, given_name):
        """
        Sets the given_name of this CreateCustomerRequest.
        

        :param given_name: The given_name of this CreateCustomerRequest.
        :type: str
        """

        self._given_name = given_name

    @property
    def family_name(self):
        """
        Gets the family_name of this CreateCustomerRequest.
        

        :return: The family_name of this CreateCustomerRequest.
        :rtype: str
        """
        return self._family_name

    @family_name.setter
    def family_name(self, family_name):
        """
        Sets the family_name of this CreateCustomerRequest.
        

        :param family_name: The family_name of this CreateCustomerRequest.
        :type: str
        """

        self._family_name = family_name

    @property
    def company_name(self):
        """
        Gets the company_name of this CreateCustomerRequest.
        

        :return: The company_name of this CreateCustomerRequest.
        :rtype: str
        """
        return self._company_name

    @company_name.setter
    def company_name(self, company_name):
        """
        Sets the company_name of this CreateCustomerRequest.
        

        :param company_name: The company_name of this CreateCustomerRequest.
        :type: str
        """

        self._company_name = company_name

    @property
    def nickname(self):
        """
        Gets the nickname of this CreateCustomerRequest.
        

        :return: The nickname of this CreateCustomerRequest.
        :rtype: str
        """
        return self._nickname

    @nickname.setter
    def nickname(self, nickname):
        """
        Sets the nickname of this CreateCustomerRequest.
        

        :param nickname: The nickname of this CreateCustomerRequest.
        :type: str
        """

        self._nickname = nickname

    @property
    def email_address(self):
        """
        Gets the email_address of this CreateCustomerRequest.
        

        :return: The email_address of this CreateCustomerRequest.
        :rtype: str
        """
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        """
        Sets the email_address of this CreateCustomerRequest.
        

        :param email_address: The email_address of this CreateCustomerRequest.
        :type: str
        """

        self._email_address = email_address

    @property
    def address(self):
        """
        Gets the address of this CreateCustomerRequest.
        

        :return: The address of this CreateCustomerRequest.
        :rtype: Address
        """
        return self._address

    @address.setter
    def address(self, address):
        """
        Sets the address of this CreateCustomerRequest.
        

        :param address: The address of this CreateCustomerRequest.
        :type: Address
        """

        self._address = address

    @property
    def phone_number(self):
        """
        Gets the phone_number of this CreateCustomerRequest.
        

        :return: The phone_number of this CreateCustomerRequest.
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """
        Sets the phone_number of this CreateCustomerRequest.
        

        :param phone_number: The phone_number of this CreateCustomerRequest.
        :type: str
        """

        self._phone_number = phone_number

    @property
    def reference_id(self):
        """
        Gets the reference_id of this CreateCustomerRequest.
        

        :return: The reference_id of this CreateCustomerRequest.
        :rtype: str
        """
        return self._reference_id

    @reference_id.setter
    def reference_id(self, reference_id):
        """
        Sets the reference_id of this CreateCustomerRequest.
        

        :param reference_id: The reference_id of this CreateCustomerRequest.
        :type: str
        """

        self._reference_id = reference_id

    @property
    def note(self):
        """
        Gets the note of this CreateCustomerRequest.
        

        :return: The note of this CreateCustomerRequest.
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        """
        Sets the note of this CreateCustomerRequest.
        

        :param note: The note of this CreateCustomerRequest.
        :type: str
        """

        self._note = note

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

# coding: utf-8

"""
    Yahoo!広告 検索広告 API リファレンス / Yahoo! Ads Search Ads API Reference

    <div lang=\"ja\">Yahoo!広告 検索広告 APIのWebサービスについて説明します。<br> 「Try it out」のご利用には、事前にアプリケーションの登録が必要です。また、アプリケーションのリダイレクトURIの1つに<br> https://yahoojp-marketing.github.io/ads-search-api-documents/oauth2-redirect.htmlを登録してください。 </div> <div lang=\"en\">Search Ads API Web Services supported in Yahoo! Ads API.<br> When you use \"Try it out\", you need to register your application in advance.<br> As one of redirect URI for application, you need to set \"https://yahoojp-marketing.github.io/ads-search-api-documents/oauth2-redirect.html\". </div>   # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from yahoo_ads_search.configuration import Configuration


class DictionaryServiceGeographicLocation(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'child': 'list[DictionaryServiceGeographicLocation]',
        'code': 'str',
        'full_name': 'str',
        'geographic_location_status': 'DictionaryServiceGeographicLocationStatus',
        'name': 'str',
        'order': 'str',
        'parent': 'str'
    }

    attribute_map = {
        'child': 'child',
        'code': 'code',
        'full_name': 'fullName',
        'geographic_location_status': 'geographicLocationStatus',
        'name': 'name',
        'order': 'order',
        'parent': 'parent'
    }

    def __init__(self, child=None, code=None, full_name=None, geographic_location_status=None, name=None, order=None, parent=None, local_vars_configuration=None):  # noqa: E501
        """DictionaryServiceGeographicLocation - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._child = None
        self._code = None
        self._full_name = None
        self._geographic_location_status = None
        self._name = None
        self._order = None
        self._parent = None
        self.discriminator = None

        self.child = child
        self.code = code
        self.full_name = full_name
        self.geographic_location_status = geographic_location_status
        self.name = name
        self.order = order
        self.parent = parent

    @property
    def child(self):
        """Gets the child of this DictionaryServiceGeographicLocation.  # noqa: E501


        :return: The child of this DictionaryServiceGeographicLocation.  # noqa: E501
        :rtype: list[DictionaryServiceGeographicLocation]
        """
        return self._child

    @child.setter
    def child(self, child):
        """Sets the child of this DictionaryServiceGeographicLocation.


        :param child: The child of this DictionaryServiceGeographicLocation.  # noqa: E501
        :type: list[DictionaryServiceGeographicLocation]
        """

        self._child = child

    @property
    def code(self):
        """Gets the code of this DictionaryServiceGeographicLocation.  # noqa: E501

        <div lang=\"ja\">地域コードです。</div> <div lang=\"en\">Geographic code</div>   # noqa: E501

        :return: The code of this DictionaryServiceGeographicLocation.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this DictionaryServiceGeographicLocation.

        <div lang=\"ja\">地域コードです。</div> <div lang=\"en\">Geographic code</div>   # noqa: E501

        :param code: The code of this DictionaryServiceGeographicLocation.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def full_name(self):
        """Gets the full_name of this DictionaryServiceGeographicLocation.  # noqa: E501

        <div lang=\"ja\">地域名(都道府県名からすべて)です。</div> <div lang=\"en\">Name of places (Prefecture and all)</div>   # noqa: E501

        :return: The full_name of this DictionaryServiceGeographicLocation.  # noqa: E501
        :rtype: str
        """
        return self._full_name

    @full_name.setter
    def full_name(self, full_name):
        """Sets the full_name of this DictionaryServiceGeographicLocation.

        <div lang=\"ja\">地域名(都道府県名からすべて)です。</div> <div lang=\"en\">Name of places (Prefecture and all)</div>   # noqa: E501

        :param full_name: The full_name of this DictionaryServiceGeographicLocation.  # noqa: E501
        :type: str
        """

        self._full_name = full_name

    @property
    def geographic_location_status(self):
        """Gets the geographic_location_status of this DictionaryServiceGeographicLocation.  # noqa: E501


        :return: The geographic_location_status of this DictionaryServiceGeographicLocation.  # noqa: E501
        :rtype: DictionaryServiceGeographicLocationStatus
        """
        return self._geographic_location_status

    @geographic_location_status.setter
    def geographic_location_status(self, geographic_location_status):
        """Sets the geographic_location_status of this DictionaryServiceGeographicLocation.


        :param geographic_location_status: The geographic_location_status of this DictionaryServiceGeographicLocation.  # noqa: E501
        :type: DictionaryServiceGeographicLocationStatus
        """

        self._geographic_location_status = geographic_location_status

    @property
    def name(self):
        """Gets the name of this DictionaryServiceGeographicLocation.  # noqa: E501

        <div lang=\"ja\">地域名(市区町村のみ)です。</div> <div lang=\"en\">Name of places (City Only)</div>   # noqa: E501

        :return: The name of this DictionaryServiceGeographicLocation.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DictionaryServiceGeographicLocation.

        <div lang=\"ja\">地域名(市区町村のみ)です。</div> <div lang=\"en\">Name of places (City Only)</div>   # noqa: E501

        :param name: The name of this DictionaryServiceGeographicLocation.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def order(self):
        """Gets the order of this DictionaryServiceGeographicLocation.  # noqa: E501

        <div lang=\"ja\">並び順です。<br>下記の順序に基づいた連番となります。<br> 都道府県は北海道、青森、・・・・沖縄の順<br>都道府県配下の市区町村は五十音順</div> <div lang=\"en\">Order of list<br><br>Sequential number based on the order below.<br><br> - Prefecture is in order of Hokkaido, Aomori to Okinawa. (North to South)<br><br> - Cities under prefecture are listed in the order of the 50-character Japanese kana syllabary.</div>   # noqa: E501

        :return: The order of this DictionaryServiceGeographicLocation.  # noqa: E501
        :rtype: str
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this DictionaryServiceGeographicLocation.

        <div lang=\"ja\">並び順です。<br>下記の順序に基づいた連番となります。<br> 都道府県は北海道、青森、・・・・沖縄の順<br>都道府県配下の市区町村は五十音順</div> <div lang=\"en\">Order of list<br><br>Sequential number based on the order below.<br><br> - Prefecture is in order of Hokkaido, Aomori to Okinawa. (North to South)<br><br> - Cities under prefecture are listed in the order of the 50-character Japanese kana syllabary.</div>   # noqa: E501

        :param order: The order of this DictionaryServiceGeographicLocation.  # noqa: E501
        :type: str
        """

        self._order = order

    @property
    def parent(self):
        """Gets the parent of this DictionaryServiceGeographicLocation.  # noqa: E501

        <div lang=\"ja\">上位地域コードです。</div> <div lang=\"en\">Parent geographic code</div>   # noqa: E501

        :return: The parent of this DictionaryServiceGeographicLocation.  # noqa: E501
        :rtype: str
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """Sets the parent of this DictionaryServiceGeographicLocation.

        <div lang=\"ja\">上位地域コードです。</div> <div lang=\"en\">Parent geographic code</div>   # noqa: E501

        :param parent: The parent of this DictionaryServiceGeographicLocation.  # noqa: E501
        :type: str
        """

        self._parent = parent

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DictionaryServiceGeographicLocation):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DictionaryServiceGeographicLocation):
            return True

        return self.to_dict() != other.to_dict()

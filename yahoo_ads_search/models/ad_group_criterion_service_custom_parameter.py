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


class AdGroupCriterionServiceCustomParameter(object):
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
        'key': 'str',
        'value': 'str'
    }

    attribute_map = {
        'key': 'key',
        'value': 'value'
    }

    def __init__(self, key=None, value=None, local_vars_configuration=None):  # noqa: E501
        """AdGroupCriterionServiceCustomParameter - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._key = None
        self._value = None
        self.discriminator = None

        self.key = key
        self.value = value

    @property
    def key(self):
        """Gets the key of this AdGroupCriterionServiceCustomParameter.  # noqa: E501

        <div lang=\"ja\">キーです。<br> ADDおよびSET時、このフィールドは必須となります。</div> <div lang=\"en\">Key of parameter.<br> This field is required in ADD and SET operation.</div>   # noqa: E501

        :return: The key of this AdGroupCriterionServiceCustomParameter.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this AdGroupCriterionServiceCustomParameter.

        <div lang=\"ja\">キーです。<br> ADDおよびSET時、このフィールドは必須となります。</div> <div lang=\"en\">Key of parameter.<br> This field is required in ADD and SET operation.</div>   # noqa: E501

        :param key: The key of this AdGroupCriterionServiceCustomParameter.  # noqa: E501
        :type: str
        """

        self._key = key

    @property
    def value(self):
        """Gets the value of this AdGroupCriterionServiceCustomParameter.  # noqa: E501

        <div lang=\"ja\">値です。<br> ADDおよびSET時、このフィールドは省略可能となります。</div> <div lang=\"en\">Value of parameter.<br> This field is optional in ADD and SET operation.</div>   # noqa: E501

        :return: The value of this AdGroupCriterionServiceCustomParameter.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this AdGroupCriterionServiceCustomParameter.

        <div lang=\"ja\">値です。<br> ADDおよびSET時、このフィールドは省略可能となります。</div> <div lang=\"en\">Value of parameter.<br> This field is optional in ADD and SET operation.</div>   # noqa: E501

        :param value: The value of this AdGroupCriterionServiceCustomParameter.  # noqa: E501
        :type: str
        """

        self._value = value

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
        if not isinstance(other, AdGroupCriterionServiceCustomParameter):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AdGroupCriterionServiceCustomParameter):
            return True

        return self.to_dict() != other.to_dict()

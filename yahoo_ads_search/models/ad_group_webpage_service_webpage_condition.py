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


class AdGroupWebpageServiceWebpageCondition(object):
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
        'argument': 'str',
        'webpage_condition_type': 'AdGroupWebpageServiceWebpageConditionType'
    }

    attribute_map = {
        'argument': 'argument',
        'webpage_condition_type': 'webpageConditionType'
    }

    def __init__(self, argument=None, webpage_condition_type=None, local_vars_configuration=None):  # noqa: E501
        """AdGroupWebpageServiceWebpageCondition - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._argument = None
        self._webpage_condition_type = None
        self.discriminator = None

        self.argument = argument
        self.webpage_condition_type = webpage_condition_type

    @property
    def argument(self):
        """Gets the argument of this AdGroupWebpageServiceWebpageCondition.  # noqa: E501

        <div lang=\"ja\">条件の設定値(正規表現の指定可)です。<br>ADD時、このフィールドは必須です。※typeがALL_PAGESの場合は省略可能となります。SET時、このフィールドは無視されます。</div> <div lang=\"en\">Value of rule setting (Can specify regular expression)<br>This field is required in ADD operation, and will be ignored in SET operation. *If type is 'ALL_PAGES', this field is optional in ADD operation.</div>   # noqa: E501

        :return: The argument of this AdGroupWebpageServiceWebpageCondition.  # noqa: E501
        :rtype: str
        """
        return self._argument

    @argument.setter
    def argument(self, argument):
        """Sets the argument of this AdGroupWebpageServiceWebpageCondition.

        <div lang=\"ja\">条件の設定値(正規表現の指定可)です。<br>ADD時、このフィールドは必須です。※typeがALL_PAGESの場合は省略可能となります。SET時、このフィールドは無視されます。</div> <div lang=\"en\">Value of rule setting (Can specify regular expression)<br>This field is required in ADD operation, and will be ignored in SET operation. *If type is 'ALL_PAGES', this field is optional in ADD operation.</div>   # noqa: E501

        :param argument: The argument of this AdGroupWebpageServiceWebpageCondition.  # noqa: E501
        :type: str
        """

        self._argument = argument

    @property
    def webpage_condition_type(self):
        """Gets the webpage_condition_type of this AdGroupWebpageServiceWebpageCondition.  # noqa: E501


        :return: The webpage_condition_type of this AdGroupWebpageServiceWebpageCondition.  # noqa: E501
        :rtype: AdGroupWebpageServiceWebpageConditionType
        """
        return self._webpage_condition_type

    @webpage_condition_type.setter
    def webpage_condition_type(self, webpage_condition_type):
        """Sets the webpage_condition_type of this AdGroupWebpageServiceWebpageCondition.


        :param webpage_condition_type: The webpage_condition_type of this AdGroupWebpageServiceWebpageCondition.  # noqa: E501
        :type: AdGroupWebpageServiceWebpageConditionType
        """

        self._webpage_condition_type = webpage_condition_type

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
        if not isinstance(other, AdGroupWebpageServiceWebpageCondition):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AdGroupWebpageServiceWebpageCondition):
            return True

        return self.to_dict() != other.to_dict()

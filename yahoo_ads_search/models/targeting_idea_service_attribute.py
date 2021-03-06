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


class TargetingIdeaServiceAttribute(object):
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
        'attribute_type': 'TargetingIdeaServiceAttributeType',
        'keyword_attribute': 'TargetingIdeaServiceKeywordAttribute'
    }

    attribute_map = {
        'attribute_type': 'attributeType',
        'keyword_attribute': 'keywordAttribute'
    }

    def __init__(self, attribute_type=None, keyword_attribute=None, local_vars_configuration=None):  # noqa: E501
        """TargetingIdeaServiceAttribute - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._attribute_type = None
        self._keyword_attribute = None
        self.discriminator = None

        self.attribute_type = attribute_type
        self.keyword_attribute = keyword_attribute

    @property
    def attribute_type(self):
        """Gets the attribute_type of this TargetingIdeaServiceAttribute.  # noqa: E501


        :return: The attribute_type of this TargetingIdeaServiceAttribute.  # noqa: E501
        :rtype: TargetingIdeaServiceAttributeType
        """
        return self._attribute_type

    @attribute_type.setter
    def attribute_type(self, attribute_type):
        """Sets the attribute_type of this TargetingIdeaServiceAttribute.


        :param attribute_type: The attribute_type of this TargetingIdeaServiceAttribute.  # noqa: E501
        :type: TargetingIdeaServiceAttributeType
        """

        self._attribute_type = attribute_type

    @property
    def keyword_attribute(self):
        """Gets the keyword_attribute of this TargetingIdeaServiceAttribute.  # noqa: E501


        :return: The keyword_attribute of this TargetingIdeaServiceAttribute.  # noqa: E501
        :rtype: TargetingIdeaServiceKeywordAttribute
        """
        return self._keyword_attribute

    @keyword_attribute.setter
    def keyword_attribute(self, keyword_attribute):
        """Sets the keyword_attribute of this TargetingIdeaServiceAttribute.


        :param keyword_attribute: The keyword_attribute of this TargetingIdeaServiceAttribute.  # noqa: E501
        :type: TargetingIdeaServiceKeywordAttribute
        """

        self._keyword_attribute = keyword_attribute

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
        if not isinstance(other, TargetingIdeaServiceAttribute):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TargetingIdeaServiceAttribute):
            return True

        return self.to_dict() != other.to_dict()

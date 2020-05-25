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


class CampaignCriterionServiceKeyword(object):
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
        'keyword_match_type': 'CampaignCriterionServiceKeywordMatchType',
        'text': 'str'
    }

    attribute_map = {
        'keyword_match_type': 'keywordMatchType',
        'text': 'text'
    }

    def __init__(self, keyword_match_type=None, text=None, local_vars_configuration=None):  # noqa: E501
        """CampaignCriterionServiceKeyword - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._keyword_match_type = None
        self._text = None
        self.discriminator = None

        self.keyword_match_type = keyword_match_type
        self.text = text

    @property
    def keyword_match_type(self):
        """Gets the keyword_match_type of this CampaignCriterionServiceKeyword.  # noqa: E501


        :return: The keyword_match_type of this CampaignCriterionServiceKeyword.  # noqa: E501
        :rtype: CampaignCriterionServiceKeywordMatchType
        """
        return self._keyword_match_type

    @keyword_match_type.setter
    def keyword_match_type(self, keyword_match_type):
        """Sets the keyword_match_type of this CampaignCriterionServiceKeyword.


        :param keyword_match_type: The keyword_match_type of this CampaignCriterionServiceKeyword.  # noqa: E501
        :type: CampaignCriterionServiceKeywordMatchType
        """

        self._keyword_match_type = keyword_match_type

    @property
    def text(self):
        """Gets the text of this CampaignCriterionServiceKeyword.  # noqa: E501

        <div lang=\"ja\">キーワードの内容です。<br> ADD時、このフィールドは必須です。<br> ※最大80文字、10ワードです。</div> <div lang=\"en\">CampaignCriterionServiceKeyword element.<br> This field is required in ADD operation.<br> * Maximum of 80 letters, 10 word.</div>   # noqa: E501

        :return: The text of this CampaignCriterionServiceKeyword.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this CampaignCriterionServiceKeyword.

        <div lang=\"ja\">キーワードの内容です。<br> ADD時、このフィールドは必須です。<br> ※最大80文字、10ワードです。</div> <div lang=\"en\">CampaignCriterionServiceKeyword element.<br> This field is required in ADD operation.<br> * Maximum of 80 letters, 10 word.</div>   # noqa: E501

        :param text: The text of this CampaignCriterionServiceKeyword.  # noqa: E501
        :type: str
        """

        self._text = text

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
        if not isinstance(other, CampaignCriterionServiceKeyword):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CampaignCriterionServiceKeyword):
            return True

        return self.to_dict() != other.to_dict()

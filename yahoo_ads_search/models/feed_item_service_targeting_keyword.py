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


class FeedItemServiceTargetingKeyword(object):
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
        'keyword_match_type': 'FeedItemServiceKeywordMatchType',
        'targeting_keyword_id': 'int',
        'text': 'str'
    }

    attribute_map = {
        'keyword_match_type': 'keywordMatchType',
        'targeting_keyword_id': 'targetingKeywordId',
        'text': 'text'
    }

    def __init__(self, keyword_match_type=None, targeting_keyword_id=None, text=None, local_vars_configuration=None):  # noqa: E501
        """FeedItemServiceTargetingKeyword - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._keyword_match_type = None
        self._targeting_keyword_id = None
        self._text = None
        self.discriminator = None

        self.keyword_match_type = keyword_match_type
        self.targeting_keyword_id = targeting_keyword_id
        self.text = text

    @property
    def keyword_match_type(self):
        """Gets the keyword_match_type of this FeedItemServiceTargetingKeyword.  # noqa: E501


        :return: The keyword_match_type of this FeedItemServiceTargetingKeyword.  # noqa: E501
        :rtype: FeedItemServiceKeywordMatchType
        """
        return self._keyword_match_type

    @keyword_match_type.setter
    def keyword_match_type(self, keyword_match_type):
        """Sets the keyword_match_type of this FeedItemServiceTargetingKeyword.


        :param keyword_match_type: The keyword_match_type of this FeedItemServiceTargetingKeyword.  # noqa: E501
        :type: FeedItemServiceKeywordMatchType
        """

        self._keyword_match_type = keyword_match_type

    @property
    def targeting_keyword_id(self):
        """Gets the targeting_keyword_id of this FeedItemServiceTargetingKeyword.  # noqa: E501

        <div lang=\"ja\">指定したキーワード（text）を識別する IDになります。<br> ※設定を解除する場合は「0」を指定 してください。<br> このフィールドは、SET時に省略可能となります。</div> <div lang=\"en\">ID to identify the Targeting keyword (text).<br> * To deactive, set &#34;0&#34;.<br> This field is optional in SET operation.</div>   # noqa: E501

        :return: The targeting_keyword_id of this FeedItemServiceTargetingKeyword.  # noqa: E501
        :rtype: int
        """
        return self._targeting_keyword_id

    @targeting_keyword_id.setter
    def targeting_keyword_id(self, targeting_keyword_id):
        """Sets the targeting_keyword_id of this FeedItemServiceTargetingKeyword.

        <div lang=\"ja\">指定したキーワード（text）を識別する IDになります。<br> ※設定を解除する場合は「0」を指定 してください。<br> このフィールドは、SET時に省略可能となります。</div> <div lang=\"en\">ID to identify the Targeting keyword (text).<br> * To deactive, set &#34;0&#34;.<br> This field is optional in SET operation.</div>   # noqa: E501

        :param targeting_keyword_id: The targeting_keyword_id of this FeedItemServiceTargetingKeyword.  # noqa: E501
        :type: int
        """

        self._targeting_keyword_id = targeting_keyword_id

    @property
    def text(self):
        """Gets the text of this FeedItemServiceTargetingKeyword.  # noqa: E501

        <div lang=\"ja\">指定するキーワードです。<br>※入力制限：80文字、10ワード までです。<br> このフィールドはADDおよびSET時に必須となります。</div> <div lang=\"en\">Keyword text.<br> * Insert limit: Up to 80 characters and/or 10 words.<br> This field is required in ADD and SET operation.</div>   # noqa: E501

        :return: The text of this FeedItemServiceTargetingKeyword.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this FeedItemServiceTargetingKeyword.

        <div lang=\"ja\">指定するキーワードです。<br>※入力制限：80文字、10ワード までです。<br> このフィールドはADDおよびSET時に必須となります。</div> <div lang=\"en\">Keyword text.<br> * Insert limit: Up to 80 characters and/or 10 words.<br> This field is required in ADD and SET operation.</div>   # noqa: E501

        :param text: The text of this FeedItemServiceTargetingKeyword.  # noqa: E501
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
        if not isinstance(other, FeedItemServiceTargetingKeyword):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FeedItemServiceTargetingKeyword):
            return True

        return self.to_dict() != other.to_dict()

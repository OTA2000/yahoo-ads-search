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


class ConversionTrackerServiceWebConversion(object):
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
        'markup_language': 'ConversionTrackerServiceMarkupLanguage',
        'snippet': 'str',
        'advanced_snippet': 'str',
        'tracking_code_type': 'ConversionTrackerServiceTrackingCodeType'
    }

    attribute_map = {
        'markup_language': 'markupLanguage',
        'snippet': 'snippet',
        'advanced_snippet': 'advancedSnippet',
        'tracking_code_type': 'trackingCodeType'
    }

    def __init__(self, markup_language=None, snippet=None, advanced_snippet=None, tracking_code_type=None, local_vars_configuration=None):  # noqa: E501
        """ConversionTrackerServiceWebConversion - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._markup_language = None
        self._snippet = None
        self._advanced_snippet = None
        self._tracking_code_type = None
        self.discriminator = None

        self.markup_language = markup_language
        self.snippet = snippet
        self.advanced_snippet = advanced_snippet
        self.tracking_code_type = tracking_code_type

    @property
    def markup_language(self):
        """Gets the markup_language of this ConversionTrackerServiceWebConversion.  # noqa: E501


        :return: The markup_language of this ConversionTrackerServiceWebConversion.  # noqa: E501
        :rtype: ConversionTrackerServiceMarkupLanguage
        """
        return self._markup_language

    @markup_language.setter
    def markup_language(self, markup_language):
        """Sets the markup_language of this ConversionTrackerServiceWebConversion.


        :param markup_language: The markup_language of this ConversionTrackerServiceWebConversion.  # noqa: E501
        :type: ConversionTrackerServiceMarkupLanguage
        """

        self._markup_language = markup_language

    @property
    def snippet(self):
        """Gets the snippet of this ConversionTrackerServiceWebConversion.  # noqa: E501

        <div lang=\"ja\">トラッキングスクリプトです。<br> このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。</div> <div lang=\"en\"> Tracking script.<br> Although this field will be returned in the response, it will be ignored on input.</div>   # noqa: E501

        :return: The snippet of this ConversionTrackerServiceWebConversion.  # noqa: E501
        :rtype: str
        """
        return self._snippet

    @snippet.setter
    def snippet(self, snippet):
        """Sets the snippet of this ConversionTrackerServiceWebConversion.

        <div lang=\"ja\">トラッキングスクリプトです。<br> このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。</div> <div lang=\"en\"> Tracking script.<br> Although this field will be returned in the response, it will be ignored on input.</div>   # noqa: E501

        :param snippet: The snippet of this ConversionTrackerServiceWebConversion.  # noqa: E501
        :type: str
        """

        self._snippet = snippet

    @property
    def advanced_snippet(self):
        """Gets the advanced_snippet of this ConversionTrackerServiceWebConversion.  # noqa: E501

        <div lang=\"ja\">リニューアル版のコンバージョンタグは、従来のタグよりもブラウザーなどの環境の影響を受けづらい新しいフォーマットです。<br/> 詳細は[ヘルプ](https://support-marketing.yahoo.co.jp/promotionalads/ss/articledetail?lan=ja&aid=1159)をご参照ください。<br> このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。</div> <div lang=\"en\">The new format of conversion tag avoids the impacts such as changes made to the browser. <br/> [Help Page](https://support-marketing.yahoo.co.jp/promotionalads/ss/articledetail?lan=en&aid=353) <br> Although this field will be returned in the response, it will be ignored on input.</div>   # noqa: E501

        :return: The advanced_snippet of this ConversionTrackerServiceWebConversion.  # noqa: E501
        :rtype: str
        """
        return self._advanced_snippet

    @advanced_snippet.setter
    def advanced_snippet(self, advanced_snippet):
        """Sets the advanced_snippet of this ConversionTrackerServiceWebConversion.

        <div lang=\"ja\">リニューアル版のコンバージョンタグは、従来のタグよりもブラウザーなどの環境の影響を受けづらい新しいフォーマットです。<br/> 詳細は[ヘルプ](https://support-marketing.yahoo.co.jp/promotionalads/ss/articledetail?lan=ja&aid=1159)をご参照ください。<br> このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。</div> <div lang=\"en\">The new format of conversion tag avoids the impacts such as changes made to the browser. <br/> [Help Page](https://support-marketing.yahoo.co.jp/promotionalads/ss/articledetail?lan=en&aid=353) <br> Although this field will be returned in the response, it will be ignored on input.</div>   # noqa: E501

        :param advanced_snippet: The advanced_snippet of this ConversionTrackerServiceWebConversion.  # noqa: E501
        :type: str
        """

        self._advanced_snippet = advanced_snippet

    @property
    def tracking_code_type(self):
        """Gets the tracking_code_type of this ConversionTrackerServiceWebConversion.  # noqa: E501


        :return: The tracking_code_type of this ConversionTrackerServiceWebConversion.  # noqa: E501
        :rtype: ConversionTrackerServiceTrackingCodeType
        """
        return self._tracking_code_type

    @tracking_code_type.setter
    def tracking_code_type(self, tracking_code_type):
        """Sets the tracking_code_type of this ConversionTrackerServiceWebConversion.


        :param tracking_code_type: The tracking_code_type of this ConversionTrackerServiceWebConversion.  # noqa: E501
        :type: ConversionTrackerServiceTrackingCodeType
        """

        self._tracking_code_type = tracking_code_type

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
        if not isinstance(other, ConversionTrackerServiceWebConversion):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ConversionTrackerServiceWebConversion):
            return True

        return self.to_dict() != other.to_dict()

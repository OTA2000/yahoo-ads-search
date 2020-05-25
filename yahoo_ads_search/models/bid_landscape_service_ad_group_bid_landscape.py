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


class BidLandscapeServiceAdGroupBidLandscape(object):
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
        'ad_group_bid_landscape_type': 'BidLandscapeServiceAdGroupBidLandscapeType',
        'landscape_current': 'bool'
    }

    attribute_map = {
        'ad_group_bid_landscape_type': 'adGroupBidLandscapeType',
        'landscape_current': 'landscapeCurrent'
    }

    def __init__(self, ad_group_bid_landscape_type=None, landscape_current=None, local_vars_configuration=None):  # noqa: E501
        """BidLandscapeServiceAdGroupBidLandscape - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._ad_group_bid_landscape_type = None
        self._landscape_current = None
        self.discriminator = None

        self.ad_group_bid_landscape_type = ad_group_bid_landscape_type
        self.landscape_current = landscape_current

    @property
    def ad_group_bid_landscape_type(self):
        """Gets the ad_group_bid_landscape_type of this BidLandscapeServiceAdGroupBidLandscape.  # noqa: E501


        :return: The ad_group_bid_landscape_type of this BidLandscapeServiceAdGroupBidLandscape.  # noqa: E501
        :rtype: BidLandscapeServiceAdGroupBidLandscapeType
        """
        return self._ad_group_bid_landscape_type

    @ad_group_bid_landscape_type.setter
    def ad_group_bid_landscape_type(self, ad_group_bid_landscape_type):
        """Sets the ad_group_bid_landscape_type of this BidLandscapeServiceAdGroupBidLandscape.


        :param ad_group_bid_landscape_type: The ad_group_bid_landscape_type of this BidLandscapeServiceAdGroupBidLandscape.  # noqa: E501
        :type: BidLandscapeServiceAdGroupBidLandscapeType
        """

        self._ad_group_bid_landscape_type = ad_group_bid_landscape_type

    @property
    def landscape_current(self):
        """Gets the landscape_current of this BidLandscapeServiceAdGroupBidLandscape.  # noqa: E501

        <div lang=\"ja\">「LandscapeCurrent」の値を選択します。</div> <div lang=\"en\">It selects the value of &#34;LandscapeCurrent&#34;</div>   # noqa: E501

        :return: The landscape_current of this BidLandscapeServiceAdGroupBidLandscape.  # noqa: E501
        :rtype: bool
        """
        return self._landscape_current

    @landscape_current.setter
    def landscape_current(self, landscape_current):
        """Sets the landscape_current of this BidLandscapeServiceAdGroupBidLandscape.

        <div lang=\"ja\">「LandscapeCurrent」の値を選択します。</div> <div lang=\"en\">It selects the value of &#34;LandscapeCurrent&#34;</div>   # noqa: E501

        :param landscape_current: The landscape_current of this BidLandscapeServiceAdGroupBidLandscape.  # noqa: E501
        :type: bool
        """

        self._landscape_current = landscape_current

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
        if not isinstance(other, BidLandscapeServiceAdGroupBidLandscape):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BidLandscapeServiceAdGroupBidLandscape):
            return True

        return self.to_dict() != other.to_dict()

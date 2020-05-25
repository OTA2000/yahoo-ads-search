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


class BiddingStrategyServiceTargetCpaBiddingScheme(object):
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
        'bid_ceiling': 'int',
        'bid_floor': 'int',
        'target_cpa': 'int'
    }

    attribute_map = {
        'bid_ceiling': 'bidCeiling',
        'bid_floor': 'bidFloor',
        'target_cpa': 'targetCpa'
    }

    def __init__(self, bid_ceiling=None, bid_floor=None, target_cpa=None, local_vars_configuration=None):  # noqa: E501
        """BiddingStrategyServiceTargetCpaBiddingScheme - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._bid_ceiling = None
        self._bid_floor = None
        self._target_cpa = None
        self.discriminator = None

        self.bid_ceiling = bid_ceiling
        self.bid_floor = bid_floor
        self.target_cpa = target_cpa

    @property
    def bid_ceiling(self):
        """Gets the bid_ceiling of this BiddingStrategyServiceTargetCpaBiddingScheme.  # noqa: E501

        <div lang=\"ja\">入札価格の上限です。<br>※「0」が設定された場合、上限設定はありません。<br> このフィールドは、いずれの場合でも省略可能となります。</div> <div lang=\"en\">CPC limit.<br>* No limits if &#34;0&#34; is set.<br> This field is optional in any cases.</div>   # noqa: E501

        :return: The bid_ceiling of this BiddingStrategyServiceTargetCpaBiddingScheme.  # noqa: E501
        :rtype: int
        """
        return self._bid_ceiling

    @bid_ceiling.setter
    def bid_ceiling(self, bid_ceiling):
        """Sets the bid_ceiling of this BiddingStrategyServiceTargetCpaBiddingScheme.

        <div lang=\"ja\">入札価格の上限です。<br>※「0」が設定された場合、上限設定はありません。<br> このフィールドは、いずれの場合でも省略可能となります。</div> <div lang=\"en\">CPC limit.<br>* No limits if &#34;0&#34; is set.<br> This field is optional in any cases.</div>   # noqa: E501

        :param bid_ceiling: The bid_ceiling of this BiddingStrategyServiceTargetCpaBiddingScheme.  # noqa: E501
        :type: int
        """

        self._bid_ceiling = bid_ceiling

    @property
    def bid_floor(self):
        """Gets the bid_floor of this BiddingStrategyServiceTargetCpaBiddingScheme.  # noqa: E501

        <div lang=\"ja\">入札価格の下限です。<br>※ 設定を解除する場合は「0」を指定します。<br> このフィールドは、いずれの場合でも省略可能となります。</div> <div lang=\"en\">Minimum CPC.<br> * Set &#34;0&#34; to deactivate.<br>This field is optional in any cases.</div>   # noqa: E501

        :return: The bid_floor of this BiddingStrategyServiceTargetCpaBiddingScheme.  # noqa: E501
        :rtype: int
        """
        return self._bid_floor

    @bid_floor.setter
    def bid_floor(self, bid_floor):
        """Sets the bid_floor of this BiddingStrategyServiceTargetCpaBiddingScheme.

        <div lang=\"ja\">入札価格の下限です。<br>※ 設定を解除する場合は「0」を指定します。<br> このフィールドは、いずれの場合でも省略可能となります。</div> <div lang=\"en\">Minimum CPC.<br> * Set &#34;0&#34; to deactivate.<br>This field is optional in any cases.</div>   # noqa: E501

        :param bid_floor: The bid_floor of this BiddingStrategyServiceTargetCpaBiddingScheme.  # noqa: E501
        :type: int
        """

        self._bid_floor = bid_floor

    @property
    def target_cpa(self):
        """Gets the target_cpa of this BiddingStrategyServiceTargetCpaBiddingScheme.  # noqa: E501

        <div lang=\"ja\">コンバージョン単価の目標値です（日本円です）。<br> このフィールドは、ADD時は必須となり、SET時は省略可能となります。</div> <div lang=\"en\">Target CPA (JPY).<br> This field is required in ADD operation, and will be optional in SET operation.</div>   # noqa: E501

        :return: The target_cpa of this BiddingStrategyServiceTargetCpaBiddingScheme.  # noqa: E501
        :rtype: int
        """
        return self._target_cpa

    @target_cpa.setter
    def target_cpa(self, target_cpa):
        """Sets the target_cpa of this BiddingStrategyServiceTargetCpaBiddingScheme.

        <div lang=\"ja\">コンバージョン単価の目標値です（日本円です）。<br> このフィールドは、ADD時は必須となり、SET時は省略可能となります。</div> <div lang=\"en\">Target CPA (JPY).<br> This field is required in ADD operation, and will be optional in SET operation.</div>   # noqa: E501

        :param target_cpa: The target_cpa of this BiddingStrategyServiceTargetCpaBiddingScheme.  # noqa: E501
        :type: int
        """

        self._target_cpa = target_cpa

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
        if not isinstance(other, BiddingStrategyServiceTargetCpaBiddingScheme):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BiddingStrategyServiceTargetCpaBiddingScheme):
            return True

        return self.to_dict() != other.to_dict()

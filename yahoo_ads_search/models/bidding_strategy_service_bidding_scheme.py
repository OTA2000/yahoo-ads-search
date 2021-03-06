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


class BiddingStrategyServiceBiddingScheme(object):
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
        'target_cpa_bidding_scheme': 'BiddingStrategyServiceTargetCpaBiddingScheme',
        'target_roas_bidding_scheme': 'BiddingStrategyServiceTargetRoasBiddingScheme',
        'target_spend_bidding_scheme': 'BiddingStrategyServiceTargetSpendBiddingScheme',
        'type': 'BiddingStrategyServiceType'
    }

    attribute_map = {
        'target_cpa_bidding_scheme': 'targetCpaBiddingScheme',
        'target_roas_bidding_scheme': 'targetRoasBiddingScheme',
        'target_spend_bidding_scheme': 'targetSpendBiddingScheme',
        'type': 'type'
    }

    def __init__(self, target_cpa_bidding_scheme=None, target_roas_bidding_scheme=None, target_spend_bidding_scheme=None, type=None, local_vars_configuration=None):  # noqa: E501
        """BiddingStrategyServiceBiddingScheme - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._target_cpa_bidding_scheme = None
        self._target_roas_bidding_scheme = None
        self._target_spend_bidding_scheme = None
        self._type = None
        self.discriminator = None

        self.target_cpa_bidding_scheme = target_cpa_bidding_scheme
        self.target_roas_bidding_scheme = target_roas_bidding_scheme
        self.target_spend_bidding_scheme = target_spend_bidding_scheme
        self.type = type

    @property
    def target_cpa_bidding_scheme(self):
        """Gets the target_cpa_bidding_scheme of this BiddingStrategyServiceBiddingScheme.  # noqa: E501


        :return: The target_cpa_bidding_scheme of this BiddingStrategyServiceBiddingScheme.  # noqa: E501
        :rtype: BiddingStrategyServiceTargetCpaBiddingScheme
        """
        return self._target_cpa_bidding_scheme

    @target_cpa_bidding_scheme.setter
    def target_cpa_bidding_scheme(self, target_cpa_bidding_scheme):
        """Sets the target_cpa_bidding_scheme of this BiddingStrategyServiceBiddingScheme.


        :param target_cpa_bidding_scheme: The target_cpa_bidding_scheme of this BiddingStrategyServiceBiddingScheme.  # noqa: E501
        :type: BiddingStrategyServiceTargetCpaBiddingScheme
        """

        self._target_cpa_bidding_scheme = target_cpa_bidding_scheme

    @property
    def target_roas_bidding_scheme(self):
        """Gets the target_roas_bidding_scheme of this BiddingStrategyServiceBiddingScheme.  # noqa: E501


        :return: The target_roas_bidding_scheme of this BiddingStrategyServiceBiddingScheme.  # noqa: E501
        :rtype: BiddingStrategyServiceTargetRoasBiddingScheme
        """
        return self._target_roas_bidding_scheme

    @target_roas_bidding_scheme.setter
    def target_roas_bidding_scheme(self, target_roas_bidding_scheme):
        """Sets the target_roas_bidding_scheme of this BiddingStrategyServiceBiddingScheme.


        :param target_roas_bidding_scheme: The target_roas_bidding_scheme of this BiddingStrategyServiceBiddingScheme.  # noqa: E501
        :type: BiddingStrategyServiceTargetRoasBiddingScheme
        """

        self._target_roas_bidding_scheme = target_roas_bidding_scheme

    @property
    def target_spend_bidding_scheme(self):
        """Gets the target_spend_bidding_scheme of this BiddingStrategyServiceBiddingScheme.  # noqa: E501


        :return: The target_spend_bidding_scheme of this BiddingStrategyServiceBiddingScheme.  # noqa: E501
        :rtype: BiddingStrategyServiceTargetSpendBiddingScheme
        """
        return self._target_spend_bidding_scheme

    @target_spend_bidding_scheme.setter
    def target_spend_bidding_scheme(self, target_spend_bidding_scheme):
        """Sets the target_spend_bidding_scheme of this BiddingStrategyServiceBiddingScheme.


        :param target_spend_bidding_scheme: The target_spend_bidding_scheme of this BiddingStrategyServiceBiddingScheme.  # noqa: E501
        :type: BiddingStrategyServiceTargetSpendBiddingScheme
        """

        self._target_spend_bidding_scheme = target_spend_bidding_scheme

    @property
    def type(self):
        """Gets the type of this BiddingStrategyServiceBiddingScheme.  # noqa: E501


        :return: The type of this BiddingStrategyServiceBiddingScheme.  # noqa: E501
        :rtype: BiddingStrategyServiceType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this BiddingStrategyServiceBiddingScheme.


        :param type: The type of this BiddingStrategyServiceBiddingScheme.  # noqa: E501
        :type: BiddingStrategyServiceType
        """

        self._type = type

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
        if not isinstance(other, BiddingStrategyServiceBiddingScheme):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BiddingStrategyServiceBiddingScheme):
            return True

        return self.to_dict() != other.to_dict()

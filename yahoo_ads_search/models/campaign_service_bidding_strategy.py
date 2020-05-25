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


class CampaignServiceBiddingStrategy(object):
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
        'bidding_scheme': 'CampaignServiceBiddingScheme',
        'bidding_strategy_id': 'int',
        'bidding_strategy_name': 'str',
        'bidding_strategy_source': 'CampaignServiceBiddingStrategySource',
        'bidding_strategy_type': 'CampaignServiceBiddingStrategyType'
    }

    attribute_map = {
        'bidding_scheme': 'biddingScheme',
        'bidding_strategy_id': 'biddingStrategyId',
        'bidding_strategy_name': 'biddingStrategyName',
        'bidding_strategy_source': 'biddingStrategySource',
        'bidding_strategy_type': 'biddingStrategyType'
    }

    def __init__(self, bidding_scheme=None, bidding_strategy_id=None, bidding_strategy_name=None, bidding_strategy_source=None, bidding_strategy_type=None, local_vars_configuration=None):  # noqa: E501
        """CampaignServiceBiddingStrategy - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._bidding_scheme = None
        self._bidding_strategy_id = None
        self._bidding_strategy_name = None
        self._bidding_strategy_source = None
        self._bidding_strategy_type = None
        self.discriminator = None

        self.bidding_scheme = bidding_scheme
        self.bidding_strategy_id = bidding_strategy_id
        self.bidding_strategy_name = bidding_strategy_name
        self.bidding_strategy_source = bidding_strategy_source
        self.bidding_strategy_type = bidding_strategy_type

    @property
    def bidding_scheme(self):
        """Gets the bidding_scheme of this CampaignServiceBiddingStrategy.  # noqa: E501


        :return: The bidding_scheme of this CampaignServiceBiddingStrategy.  # noqa: E501
        :rtype: CampaignServiceBiddingScheme
        """
        return self._bidding_scheme

    @bidding_scheme.setter
    def bidding_scheme(self, bidding_scheme):
        """Sets the bidding_scheme of this CampaignServiceBiddingStrategy.


        :param bidding_scheme: The bidding_scheme of this CampaignServiceBiddingStrategy.  # noqa: E501
        :type: CampaignServiceBiddingScheme
        """

        self._bidding_scheme = bidding_scheme

    @property
    def bidding_strategy_id(self):
        """Gets the bidding_strategy_id of this CampaignServiceBiddingStrategy.  # noqa: E501

        <div lang=\"ja\">自動入札IDです。<br> ADD時、標準入札設定の場合、このフィールドは設定不可となり、ポートフォリオ入札設定の場合、必須となります。また、biddingSchemeと同時に設定することはできません。</div> <div lang=\"en\">Auto Bidding ID.<br> This field cannot be specified when Standard bidding is setting, and is required when Portfolio bidding is setting in ADD operation. It cannot be specified at the same times as biddingScheme.</div>   # noqa: E501

        :return: The bidding_strategy_id of this CampaignServiceBiddingStrategy.  # noqa: E501
        :rtype: int
        """
        return self._bidding_strategy_id

    @bidding_strategy_id.setter
    def bidding_strategy_id(self, bidding_strategy_id):
        """Sets the bidding_strategy_id of this CampaignServiceBiddingStrategy.

        <div lang=\"ja\">自動入札IDです。<br> ADD時、標準入札設定の場合、このフィールドは設定不可となり、ポートフォリオ入札設定の場合、必須となります。また、biddingSchemeと同時に設定することはできません。</div> <div lang=\"en\">Auto Bidding ID.<br> This field cannot be specified when Standard bidding is setting, and is required when Portfolio bidding is setting in ADD operation. It cannot be specified at the same times as biddingScheme.</div>   # noqa: E501

        :param bidding_strategy_id: The bidding_strategy_id of this CampaignServiceBiddingStrategy.  # noqa: E501
        :type: int
        """

        self._bidding_strategy_id = bidding_strategy_id

    @property
    def bidding_strategy_name(self):
        """Gets the bidding_strategy_name of this CampaignServiceBiddingStrategy.  # noqa: E501

        <div lang=\"ja\">自動入札名です。<br> ADD時、このフィールドは無視されます。<br> ※50文字以内になります。</div> <div lang=\"en\">Auto Bidding name.<br> This field will be ignored in ADD operation.<br>* Up to 50 characters.</div>   # noqa: E501

        :return: The bidding_strategy_name of this CampaignServiceBiddingStrategy.  # noqa: E501
        :rtype: str
        """
        return self._bidding_strategy_name

    @bidding_strategy_name.setter
    def bidding_strategy_name(self, bidding_strategy_name):
        """Sets the bidding_strategy_name of this CampaignServiceBiddingStrategy.

        <div lang=\"ja\">自動入札名です。<br> ADD時、このフィールドは無視されます。<br> ※50文字以内になります。</div> <div lang=\"en\">Auto Bidding name.<br> This field will be ignored in ADD operation.<br>* Up to 50 characters.</div>   # noqa: E501

        :param bidding_strategy_name: The bidding_strategy_name of this CampaignServiceBiddingStrategy.  # noqa: E501
        :type: str
        """

        self._bidding_strategy_name = bidding_strategy_name

    @property
    def bidding_strategy_source(self):
        """Gets the bidding_strategy_source of this CampaignServiceBiddingStrategy.  # noqa: E501


        :return: The bidding_strategy_source of this CampaignServiceBiddingStrategy.  # noqa: E501
        :rtype: CampaignServiceBiddingStrategySource
        """
        return self._bidding_strategy_source

    @bidding_strategy_source.setter
    def bidding_strategy_source(self, bidding_strategy_source):
        """Sets the bidding_strategy_source of this CampaignServiceBiddingStrategy.


        :param bidding_strategy_source: The bidding_strategy_source of this CampaignServiceBiddingStrategy.  # noqa: E501
        :type: CampaignServiceBiddingStrategySource
        """

        self._bidding_strategy_source = bidding_strategy_source

    @property
    def bidding_strategy_type(self):
        """Gets the bidding_strategy_type of this CampaignServiceBiddingStrategy.  # noqa: E501


        :return: The bidding_strategy_type of this CampaignServiceBiddingStrategy.  # noqa: E501
        :rtype: CampaignServiceBiddingStrategyType
        """
        return self._bidding_strategy_type

    @bidding_strategy_type.setter
    def bidding_strategy_type(self, bidding_strategy_type):
        """Sets the bidding_strategy_type of this CampaignServiceBiddingStrategy.


        :param bidding_strategy_type: The bidding_strategy_type of this CampaignServiceBiddingStrategy.  # noqa: E501
        :type: CampaignServiceBiddingStrategyType
        """

        self._bidding_strategy_type = bidding_strategy_type

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
        if not isinstance(other, CampaignServiceBiddingStrategy):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CampaignServiceBiddingStrategy):
            return True

        return self.to_dict() != other.to_dict()
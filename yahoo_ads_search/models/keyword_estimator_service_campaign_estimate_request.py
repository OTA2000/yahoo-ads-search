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


class KeywordEstimatorServiceCampaignEstimateRequest(object):
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
        'ad_group_estimate_requests': 'list[KeywordEstimatorServiceAdGroupEstimateRequest]',
        'campaign_id': 'int',
        'daily_budget': 'int',
        'provinces': 'list[str]'
    }

    attribute_map = {
        'ad_group_estimate_requests': 'adGroupEstimateRequests',
        'campaign_id': 'campaignId',
        'daily_budget': 'dailyBudget',
        'provinces': 'provinces'
    }

    def __init__(self, ad_group_estimate_requests=None, campaign_id=None, daily_budget=None, provinces=None, local_vars_configuration=None):  # noqa: E501
        """KeywordEstimatorServiceCampaignEstimateRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._ad_group_estimate_requests = None
        self._campaign_id = None
        self._daily_budget = None
        self._provinces = None
        self.discriminator = None

        self.ad_group_estimate_requests = ad_group_estimate_requests
        self.campaign_id = campaign_id
        self.daily_budget = daily_budget
        self.provinces = provinces

    @property
    def ad_group_estimate_requests(self):
        """Gets the ad_group_estimate_requests of this KeywordEstimatorServiceCampaignEstimateRequest.  # noqa: E501

        <div lang=\"ja\">見積もりを行う広告グループを格納するコンテナです。</div> <div lang=\"en\">A container for the Ad Group to estimate</div>   # noqa: E501

        :return: The ad_group_estimate_requests of this KeywordEstimatorServiceCampaignEstimateRequest.  # noqa: E501
        :rtype: list[KeywordEstimatorServiceAdGroupEstimateRequest]
        """
        return self._ad_group_estimate_requests

    @ad_group_estimate_requests.setter
    def ad_group_estimate_requests(self, ad_group_estimate_requests):
        """Sets the ad_group_estimate_requests of this KeywordEstimatorServiceCampaignEstimateRequest.

        <div lang=\"ja\">見積もりを行う広告グループを格納するコンテナです。</div> <div lang=\"en\">A container for the Ad Group to estimate</div>   # noqa: E501

        :param ad_group_estimate_requests: The ad_group_estimate_requests of this KeywordEstimatorServiceCampaignEstimateRequest.  # noqa: E501
        :type: list[KeywordEstimatorServiceAdGroupEstimateRequest]
        """

        self._ad_group_estimate_requests = ad_group_estimate_requests

    @property
    def campaign_id(self):
        """Gets the campaign_id of this KeywordEstimatorServiceCampaignEstimateRequest.  # noqa: E501

        <div lang=\"ja\">キャンペーンIDです。</div> <div lang=\"en\">Campaign ID</div>   # noqa: E501

        :return: The campaign_id of this KeywordEstimatorServiceCampaignEstimateRequest.  # noqa: E501
        :rtype: int
        """
        return self._campaign_id

    @campaign_id.setter
    def campaign_id(self, campaign_id):
        """Sets the campaign_id of this KeywordEstimatorServiceCampaignEstimateRequest.

        <div lang=\"ja\">キャンペーンIDです。</div> <div lang=\"en\">Campaign ID</div>   # noqa: E501

        :param campaign_id: The campaign_id of this KeywordEstimatorServiceCampaignEstimateRequest.  # noqa: E501
        :type: int
        """

        self._campaign_id = campaign_id

    @property
    def daily_budget(self):
        """Gets the daily_budget of this KeywordEstimatorServiceCampaignEstimateRequest.  # noqa: E501

        <div lang=\"ja\">見積もりで使用するキャンペーンの一日あたりの予算です。</div> <div lang=\"en\">Daily campaign budget used to estimate</div>   # noqa: E501

        :return: The daily_budget of this KeywordEstimatorServiceCampaignEstimateRequest.  # noqa: E501
        :rtype: int
        """
        return self._daily_budget

    @daily_budget.setter
    def daily_budget(self, daily_budget):
        """Sets the daily_budget of this KeywordEstimatorServiceCampaignEstimateRequest.

        <div lang=\"ja\">見積もりで使用するキャンペーンの一日あたりの予算です。</div> <div lang=\"en\">Daily campaign budget used to estimate</div>   # noqa: E501

        :param daily_budget: The daily_budget of this KeywordEstimatorServiceCampaignEstimateRequest.  # noqa: E501
        :type: int
        """

        self._daily_budget = daily_budget

    @property
    def provinces(self):
        """Gets the provinces of this KeywordEstimatorServiceCampaignEstimateRequest.  # noqa: E501

        <div lang=\"ja\">見積もりで使用する広告配信する指定地域（都道府県）です。</div> <div lang=\"en\">Province to serve Ads used to estimate</div>   # noqa: E501

        :return: The provinces of this KeywordEstimatorServiceCampaignEstimateRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._provinces

    @provinces.setter
    def provinces(self, provinces):
        """Sets the provinces of this KeywordEstimatorServiceCampaignEstimateRequest.

        <div lang=\"ja\">見積もりで使用する広告配信する指定地域（都道府県）です。</div> <div lang=\"en\">Province to serve Ads used to estimate</div>   # noqa: E501

        :param provinces: The provinces of this KeywordEstimatorServiceCampaignEstimateRequest.  # noqa: E501
        :type: list[str]
        """

        self._provinces = provinces

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
        if not isinstance(other, KeywordEstimatorServiceCampaignEstimateRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, KeywordEstimatorServiceCampaignEstimateRequest):
            return True

        return self.to_dict() != other.to_dict()

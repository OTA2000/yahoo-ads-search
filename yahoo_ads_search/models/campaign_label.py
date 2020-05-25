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


class CampaignLabel(object):
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
        'account_id': 'int',
        'campaign_id': 'int',
        'label_id': 'int'
    }

    attribute_map = {
        'account_id': 'accountId',
        'campaign_id': 'campaignId',
        'label_id': 'labelId'
    }

    def __init__(self, account_id=None, campaign_id=None, label_id=None, local_vars_configuration=None):  # noqa: E501
        """CampaignLabel - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._account_id = None
        self._campaign_id = None
        self._label_id = None
        self.discriminator = None

        self.account_id = account_id
        self.campaign_id = campaign_id
        self.label_id = label_id

    @property
    def account_id(self):
        """Gets the account_id of this CampaignLabel.  # noqa: E501

        <div lang=\"ja\">アカウントIDです。<br> このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。</div> <div lang=\"en\">Account ID.<br> Although this field will be returned in the response, it will be ignored on input.</div>   # noqa: E501

        :return: The account_id of this CampaignLabel.  # noqa: E501
        :rtype: int
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this CampaignLabel.

        <div lang=\"ja\">アカウントIDです。<br> このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。</div> <div lang=\"en\">Account ID.<br> Although this field will be returned in the response, it will be ignored on input.</div>   # noqa: E501

        :param account_id: The account_id of this CampaignLabel.  # noqa: E501
        :type: int
        """

        self._account_id = account_id

    @property
    def campaign_id(self):
        """Gets the campaign_id of this CampaignLabel.  # noqa: E501

        <div lang=\"ja\">キャンペーンIDです。<br> このフィールドは、いずれの場合でも必須です。</div> <div lang=\"en\">Campaign ID.<br> This field is required in any cases.</div>   # noqa: E501

        :return: The campaign_id of this CampaignLabel.  # noqa: E501
        :rtype: int
        """
        return self._campaign_id

    @campaign_id.setter
    def campaign_id(self, campaign_id):
        """Sets the campaign_id of this CampaignLabel.

        <div lang=\"ja\">キャンペーンIDです。<br> このフィールドは、いずれの場合でも必須です。</div> <div lang=\"en\">Campaign ID.<br> This field is required in any cases.</div>   # noqa: E501

        :param campaign_id: The campaign_id of this CampaignLabel.  # noqa: E501
        :type: int
        """

        self._campaign_id = campaign_id

    @property
    def label_id(self):
        """Gets the label_id of this CampaignLabel.  # noqa: E501

        <div lang=\"ja\">ラベルIDです。<br> このフィールドは、いずれの場合でも必須です。</div> <div lang=\"en\">Label ID.<br> This field is required in any cases.</div>   # noqa: E501

        :return: The label_id of this CampaignLabel.  # noqa: E501
        :rtype: int
        """
        return self._label_id

    @label_id.setter
    def label_id(self, label_id):
        """Sets the label_id of this CampaignLabel.

        <div lang=\"ja\">ラベルIDです。<br> このフィールドは、いずれの場合でも必須です。</div> <div lang=\"en\">Label ID.<br> This field is required in any cases.</div>   # noqa: E501

        :param label_id: The label_id of this CampaignLabel.  # noqa: E501
        :type: int
        """

        self._label_id = label_id

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
        if not isinstance(other, CampaignLabel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CampaignLabel):
            return True

        return self.to_dict() != other.to_dict()

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


class AdGroupAd(object):
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
        'ad': 'AdGroupAdServiceAd',
        'ad_group_id': 'int',
        'ad_group_name': 'str',
        'ad_group_track_id': 'int',
        'ad_id': 'int',
        'ad_name': 'str',
        'ad_track_id': 'int',
        'approval_status': 'AdGroupAdServiceApprovalStatus',
        'campaign_id': 'int',
        'campaign_name': 'str',
        'campaign_track_id': 'int',
        'disapproval_reason_codes': 'list[str]',
        'feed_id': 'int',
        'invalided_trademarks': 'list[str]',
        'labels': 'list[AdGroupAdServiceLabel]',
        'trademark_status': 'AdGroupAdServiceTrademarkStatus',
        'user_status': 'AdGroupAdServiceUserStatus'
    }

    attribute_map = {
        'account_id': 'accountId',
        'ad': 'ad',
        'ad_group_id': 'adGroupId',
        'ad_group_name': 'adGroupName',
        'ad_group_track_id': 'adGroupTrackId',
        'ad_id': 'adId',
        'ad_name': 'adName',
        'ad_track_id': 'adTrackId',
        'approval_status': 'approvalStatus',
        'campaign_id': 'campaignId',
        'campaign_name': 'campaignName',
        'campaign_track_id': 'campaignTrackId',
        'disapproval_reason_codes': 'disapprovalReasonCodes',
        'feed_id': 'feedId',
        'invalided_trademarks': 'invalidedTrademarks',
        'labels': 'labels',
        'trademark_status': 'trademarkStatus',
        'user_status': 'userStatus'
    }

    def __init__(self, account_id=None, ad=None, ad_group_id=None, ad_group_name=None, ad_group_track_id=None, ad_id=None, ad_name=None, ad_track_id=None, approval_status=None, campaign_id=None, campaign_name=None, campaign_track_id=None, disapproval_reason_codes=None, feed_id=None, invalided_trademarks=None, labels=None, trademark_status=None, user_status=None, local_vars_configuration=None):  # noqa: E501
        """AdGroupAd - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._account_id = None
        self._ad = None
        self._ad_group_id = None
        self._ad_group_name = None
        self._ad_group_track_id = None
        self._ad_id = None
        self._ad_name = None
        self._ad_track_id = None
        self._approval_status = None
        self._campaign_id = None
        self._campaign_name = None
        self._campaign_track_id = None
        self._disapproval_reason_codes = None
        self._feed_id = None
        self._invalided_trademarks = None
        self._labels = None
        self._trademark_status = None
        self._user_status = None
        self.discriminator = None

        self.account_id = account_id
        self.ad = ad
        self.ad_group_id = ad_group_id
        self.ad_group_name = ad_group_name
        self.ad_group_track_id = ad_group_track_id
        self.ad_id = ad_id
        self.ad_name = ad_name
        self.ad_track_id = ad_track_id
        self.approval_status = approval_status
        self.campaign_id = campaign_id
        self.campaign_name = campaign_name
        self.campaign_track_id = campaign_track_id
        self.disapproval_reason_codes = disapproval_reason_codes
        self.feed_id = feed_id
        self.invalided_trademarks = invalided_trademarks
        self.labels = labels
        self.trademark_status = trademark_status
        self.user_status = user_status

    @property
    def account_id(self):
        """Gets the account_id of this AdGroupAd.  # noqa: E501

        <div lang=\"ja\">アカウントIDです。<br> このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。</div> <div lang=\"en\">Account ID.<br> Although this field will be returned in the response, it will be ignored on input.</div>   # noqa: E501

        :return: The account_id of this AdGroupAd.  # noqa: E501
        :rtype: int
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this AdGroupAd.

        <div lang=\"ja\">アカウントIDです。<br> このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。</div> <div lang=\"en\">Account ID.<br> Although this field will be returned in the response, it will be ignored on input.</div>   # noqa: E501

        :param account_id: The account_id of this AdGroupAd.  # noqa: E501
        :type: int
        """

        self._account_id = account_id

    @property
    def ad(self):
        """Gets the ad of this AdGroupAd.  # noqa: E501


        :return: The ad of this AdGroupAd.  # noqa: E501
        :rtype: AdGroupAdServiceAd
        """
        return self._ad

    @ad.setter
    def ad(self, ad):
        """Sets the ad of this AdGroupAd.


        :param ad: The ad of this AdGroupAd.  # noqa: E501
        :type: AdGroupAdServiceAd
        """

        self._ad = ad

    @property
    def ad_group_id(self):
        """Gets the ad_group_id of this AdGroupAd.  # noqa: E501

        <div lang=\"ja\">広告グループIDです。<br> このフィールドは、いずれの場合でも必須となります。</div> <div lang=\"en\">Ad group ID.<br> This field is required in any cases.</div>   # noqa: E501

        :return: The ad_group_id of this AdGroupAd.  # noqa: E501
        :rtype: int
        """
        return self._ad_group_id

    @ad_group_id.setter
    def ad_group_id(self, ad_group_id):
        """Sets the ad_group_id of this AdGroupAd.

        <div lang=\"ja\">広告グループIDです。<br> このフィールドは、いずれの場合でも必須となります。</div> <div lang=\"en\">Ad group ID.<br> This field is required in any cases.</div>   # noqa: E501

        :param ad_group_id: The ad_group_id of this AdGroupAd.  # noqa: E501
        :type: int
        """

        self._ad_group_id = ad_group_id

    @property
    def ad_group_name(self):
        """Gets the ad_group_name of this AdGroupAd.  # noqa: E501

        <div lang=\"ja\">広告グループ名です。<br> このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。</div> <div lang=\"en\">Ad group name.<br> Although this field will be returned in the response, it will be ignored on input.</div>   # noqa: E501

        :return: The ad_group_name of this AdGroupAd.  # noqa: E501
        :rtype: str
        """
        return self._ad_group_name

    @ad_group_name.setter
    def ad_group_name(self, ad_group_name):
        """Sets the ad_group_name of this AdGroupAd.

        <div lang=\"ja\">広告グループ名です。<br> このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。</div> <div lang=\"en\">Ad group name.<br> Although this field will be returned in the response, it will be ignored on input.</div>   # noqa: E501

        :param ad_group_name: The ad_group_name of this AdGroupAd.  # noqa: E501
        :type: str
        """

        self._ad_group_name = ad_group_name

    @property
    def ad_group_track_id(self):
        """Gets the ad_group_track_id of this AdGroupAd.  # noqa: E501

        <div lang=\"ja\">トラッキング用広告グループIDです。<br> このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。</div> <div lang=\"en\">Ad group ID for tracking.<br> Although this field will be returned in the response, it will be ignored on input.</div>   # noqa: E501

        :return: The ad_group_track_id of this AdGroupAd.  # noqa: E501
        :rtype: int
        """
        return self._ad_group_track_id

    @ad_group_track_id.setter
    def ad_group_track_id(self, ad_group_track_id):
        """Sets the ad_group_track_id of this AdGroupAd.

        <div lang=\"ja\">トラッキング用広告グループIDです。<br> このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。</div> <div lang=\"en\">Ad group ID for tracking.<br> Although this field will be returned in the response, it will be ignored on input.</div>   # noqa: E501

        :param ad_group_track_id: The ad_group_track_id of this AdGroupAd.  # noqa: E501
        :type: int
        """

        self._ad_group_track_id = ad_group_track_id

    @property
    def ad_id(self):
        """Gets the ad_id of this AdGroupAd.  # noqa: E501

        <div lang=\"ja\">広告IDです。<br> SETおよびREMOVE時、このフィールドは必須となります。</div> <div lang=\"en\">Ad ID.<br> This field is required in SET and REMOVE operation.</div>   # noqa: E501

        :return: The ad_id of this AdGroupAd.  # noqa: E501
        :rtype: int
        """
        return self._ad_id

    @ad_id.setter
    def ad_id(self, ad_id):
        """Sets the ad_id of this AdGroupAd.

        <div lang=\"ja\">広告IDです。<br> SETおよびREMOVE時、このフィールドは必須となります。</div> <div lang=\"en\">Ad ID.<br> This field is required in SET and REMOVE operation.</div>   # noqa: E501

        :param ad_id: The ad_id of this AdGroupAd.  # noqa: E501
        :type: int
        """

        self._ad_id = ad_id

    @property
    def ad_name(self):
        """Gets the ad_name of this AdGroupAd.  # noqa: E501

        <div lang=\"ja\">広告名です。<br> このフィールドは、ADD時は必須となり、SET時は省略可能となります。</div> <div lang=\"en\">Ad name.<br> This field is required in ADD operation, and will be optional in SET operation.</div>   # noqa: E501

        :return: The ad_name of this AdGroupAd.  # noqa: E501
        :rtype: str
        """
        return self._ad_name

    @ad_name.setter
    def ad_name(self, ad_name):
        """Sets the ad_name of this AdGroupAd.

        <div lang=\"ja\">広告名です。<br> このフィールドは、ADD時は必須となり、SET時は省略可能となります。</div> <div lang=\"en\">Ad name.<br> This field is required in ADD operation, and will be optional in SET operation.</div>   # noqa: E501

        :param ad_name: The ad_name of this AdGroupAd.  # noqa: E501
        :type: str
        """

        self._ad_name = ad_name

    @property
    def ad_track_id(self):
        """Gets the ad_track_id of this AdGroupAd.  # noqa: E501

        <div lang=\"ja\">トラッキング用広告IDです。<br> このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。</div> <div lang=\"en\">Ad ID for tracking.<br> Although this field will be returned in the response, it will be ignored on input.</div>   # noqa: E501

        :return: The ad_track_id of this AdGroupAd.  # noqa: E501
        :rtype: int
        """
        return self._ad_track_id

    @ad_track_id.setter
    def ad_track_id(self, ad_track_id):
        """Sets the ad_track_id of this AdGroupAd.

        <div lang=\"ja\">トラッキング用広告IDです。<br> このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。</div> <div lang=\"en\">Ad ID for tracking.<br> Although this field will be returned in the response, it will be ignored on input.</div>   # noqa: E501

        :param ad_track_id: The ad_track_id of this AdGroupAd.  # noqa: E501
        :type: int
        """

        self._ad_track_id = ad_track_id

    @property
    def approval_status(self):
        """Gets the approval_status of this AdGroupAd.  # noqa: E501


        :return: The approval_status of this AdGroupAd.  # noqa: E501
        :rtype: AdGroupAdServiceApprovalStatus
        """
        return self._approval_status

    @approval_status.setter
    def approval_status(self, approval_status):
        """Sets the approval_status of this AdGroupAd.


        :param approval_status: The approval_status of this AdGroupAd.  # noqa: E501
        :type: AdGroupAdServiceApprovalStatus
        """

        self._approval_status = approval_status

    @property
    def campaign_id(self):
        """Gets the campaign_id of this AdGroupAd.  # noqa: E501

        <div lang=\"ja\">キャンペーンIDです。<br> このフィールドは、いずれの場合でも必須となります。</div> <div lang=\"en\">Campaign ID.<br> This field is required in any cases.</div>   # noqa: E501

        :return: The campaign_id of this AdGroupAd.  # noqa: E501
        :rtype: int
        """
        return self._campaign_id

    @campaign_id.setter
    def campaign_id(self, campaign_id):
        """Sets the campaign_id of this AdGroupAd.

        <div lang=\"ja\">キャンペーンIDです。<br> このフィールドは、いずれの場合でも必須となります。</div> <div lang=\"en\">Campaign ID.<br> This field is required in any cases.</div>   # noqa: E501

        :param campaign_id: The campaign_id of this AdGroupAd.  # noqa: E501
        :type: int
        """

        self._campaign_id = campaign_id

    @property
    def campaign_name(self):
        """Gets the campaign_name of this AdGroupAd.  # noqa: E501

        <div lang=\"ja\">キャンペーン名です。<br> このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。</div> <div lang=\"en\">Campaign name.<br> Although this field will be returned in the response, it will be ignored on input.</div>   # noqa: E501

        :return: The campaign_name of this AdGroupAd.  # noqa: E501
        :rtype: str
        """
        return self._campaign_name

    @campaign_name.setter
    def campaign_name(self, campaign_name):
        """Sets the campaign_name of this AdGroupAd.

        <div lang=\"ja\">キャンペーン名です。<br> このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。</div> <div lang=\"en\">Campaign name.<br> Although this field will be returned in the response, it will be ignored on input.</div>   # noqa: E501

        :param campaign_name: The campaign_name of this AdGroupAd.  # noqa: E501
        :type: str
        """

        self._campaign_name = campaign_name

    @property
    def campaign_track_id(self):
        """Gets the campaign_track_id of this AdGroupAd.  # noqa: E501

        <div lang=\"ja\">トラッキング用キャンペーンIDです。<br> このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。</div> <div lang=\"en\">Campaign ID for tracking.<br> Although this field will be returned in the response, it will be ignored on input.</div>   # noqa: E501

        :return: The campaign_track_id of this AdGroupAd.  # noqa: E501
        :rtype: int
        """
        return self._campaign_track_id

    @campaign_track_id.setter
    def campaign_track_id(self, campaign_track_id):
        """Sets the campaign_track_id of this AdGroupAd.

        <div lang=\"ja\">トラッキング用キャンペーンIDです。<br> このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。</div> <div lang=\"en\">Campaign ID for tracking.<br> Although this field will be returned in the response, it will be ignored on input.</div>   # noqa: E501

        :param campaign_track_id: The campaign_track_id of this AdGroupAd.  # noqa: E501
        :type: int
        """

        self._campaign_track_id = campaign_track_id

    @property
    def disapproval_reason_codes(self):
        """Gets the disapproval_reason_codes of this AdGroupAd.  # noqa: E501

        <div lang=\"ja\">審査否認の理由コードです。<br> (コード詳細は、DictionaryServiceのgetDisapprovalReasonのレスポンスを参照)<br> このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。</div> <div lang=\"en\">Code of Disapproval reason.<br> (Refer to DictionaryService getDisapprovalReason response for details) <br> Although this field will be returned in the response, it will be ignored on input.</div>   # noqa: E501

        :return: The disapproval_reason_codes of this AdGroupAd.  # noqa: E501
        :rtype: list[str]
        """
        return self._disapproval_reason_codes

    @disapproval_reason_codes.setter
    def disapproval_reason_codes(self, disapproval_reason_codes):
        """Sets the disapproval_reason_codes of this AdGroupAd.

        <div lang=\"ja\">審査否認の理由コードです。<br> (コード詳細は、DictionaryServiceのgetDisapprovalReasonのレスポンスを参照)<br> このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。</div> <div lang=\"en\">Code of Disapproval reason.<br> (Refer to DictionaryService getDisapprovalReason response for details) <br> Although this field will be returned in the response, it will be ignored on input.</div>   # noqa: E501

        :param disapproval_reason_codes: The disapproval_reason_codes of this AdGroupAd.  # noqa: E501
        :type: list[str]
        """

        self._disapproval_reason_codes = disapproval_reason_codes

    @property
    def feed_id(self):
        """Gets the feed_id of this AdGroupAd.  # noqa: E501

        <div lang=\"ja\">フィードIDです。<br> このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。</div> <div lang=\"en\">Feed ID.<br> Although this field will be returned in the response, it will be ignored on input.</div>   # noqa: E501

        :return: The feed_id of this AdGroupAd.  # noqa: E501
        :rtype: int
        """
        return self._feed_id

    @feed_id.setter
    def feed_id(self, feed_id):
        """Sets the feed_id of this AdGroupAd.

        <div lang=\"ja\">フィードIDです。<br> このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。</div> <div lang=\"en\">Feed ID.<br> Although this field will be returned in the response, it will be ignored on input.</div>   # noqa: E501

        :param feed_id: The feed_id of this AdGroupAd.  # noqa: E501
        :type: int
        """

        self._feed_id = feed_id

    @property
    def invalided_trademarks(self):
        """Gets the invalided_trademarks of this AdGroupAd.  # noqa: E501

        <div lang=\"ja\">制限された商標です。<br> このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。</div> <div lang=\"en\">Invalided trademarks.<br> Although this field will be returned in the response, it will be ignored on input.</div>   # noqa: E501

        :return: The invalided_trademarks of this AdGroupAd.  # noqa: E501
        :rtype: list[str]
        """
        return self._invalided_trademarks

    @invalided_trademarks.setter
    def invalided_trademarks(self, invalided_trademarks):
        """Sets the invalided_trademarks of this AdGroupAd.

        <div lang=\"ja\">制限された商標です。<br> このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。</div> <div lang=\"en\">Invalided trademarks.<br> Although this field will be returned in the response, it will be ignored on input.</div>   # noqa: E501

        :param invalided_trademarks: The invalided_trademarks of this AdGroupAd.  # noqa: E501
        :type: list[str]
        """

        self._invalided_trademarks = invalided_trademarks

    @property
    def labels(self):
        """Gets the labels of this AdGroupAd.  # noqa: E501


        :return: The labels of this AdGroupAd.  # noqa: E501
        :rtype: list[AdGroupAdServiceLabel]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this AdGroupAd.


        :param labels: The labels of this AdGroupAd.  # noqa: E501
        :type: list[AdGroupAdServiceLabel]
        """

        self._labels = labels

    @property
    def trademark_status(self):
        """Gets the trademark_status of this AdGroupAd.  # noqa: E501


        :return: The trademark_status of this AdGroupAd.  # noqa: E501
        :rtype: AdGroupAdServiceTrademarkStatus
        """
        return self._trademark_status

    @trademark_status.setter
    def trademark_status(self, trademark_status):
        """Sets the trademark_status of this AdGroupAd.


        :param trademark_status: The trademark_status of this AdGroupAd.  # noqa: E501
        :type: AdGroupAdServiceTrademarkStatus
        """

        self._trademark_status = trademark_status

    @property
    def user_status(self):
        """Gets the user_status of this AdGroupAd.  # noqa: E501


        :return: The user_status of this AdGroupAd.  # noqa: E501
        :rtype: AdGroupAdServiceUserStatus
        """
        return self._user_status

    @user_status.setter
    def user_status(self, user_status):
        """Sets the user_status of this AdGroupAd.


        :param user_status: The user_status of this AdGroupAd.  # noqa: E501
        :type: AdGroupAdServiceUserStatus
        """

        self._user_status = user_status

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
        if not isinstance(other, AdGroupAd):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AdGroupAd):
            return True

        return self.to_dict() != other.to_dict()

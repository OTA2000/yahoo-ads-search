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


class CampaignExportServiceExportSetting(object):
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
        'ad_group_ad_approval_statuses': 'list[CampaignExportServiceApprovalStatus]',
        'ad_group_ad_user_statuses': 'list[CampaignExportServiceUserStatus]',
        'ad_group_criterion_approval_statuses': 'list[CampaignExportServiceApprovalStatus]',
        'ad_group_criterion_ids': 'list[int]',
        'ad_group_criterion_user_statuses': 'list[CampaignExportServiceUserStatus]',
        'ad_group_ids': 'list[int]',
        'ad_group_user_statuses': 'list[CampaignExportServiceUserStatus]',
        'ad_ids': 'list[int]',
        'campaign_criterion_ids': 'list[int]',
        'campaign_ids': 'list[int]',
        'campaign_user_statuses': 'list[CampaignExportServiceUserStatus]',
        'encoding': 'CampaignExportServiceEncoding',
        'entity_types': 'list[CampaignExportServiceEntityType]',
        'export_fields': 'list[str]',
        'job_name': 'str',
        'lang': 'CampaignExportServiceLang',
        'output': 'CampaignExportServiceOutput'
    }

    attribute_map = {
        'account_id': 'accountId',
        'ad_group_ad_approval_statuses': 'adGroupAdApprovalStatuses',
        'ad_group_ad_user_statuses': 'adGroupAdUserStatuses',
        'ad_group_criterion_approval_statuses': 'adGroupCriterionApprovalStatuses',
        'ad_group_criterion_ids': 'adGroupCriterionIds',
        'ad_group_criterion_user_statuses': 'adGroupCriterionUserStatuses',
        'ad_group_ids': 'adGroupIds',
        'ad_group_user_statuses': 'adGroupUserStatuses',
        'ad_ids': 'adIds',
        'campaign_criterion_ids': 'campaignCriterionIds',
        'campaign_ids': 'campaignIds',
        'campaign_user_statuses': 'campaignUserStatuses',
        'encoding': 'encoding',
        'entity_types': 'entityTypes',
        'export_fields': 'exportFields',
        'job_name': 'jobName',
        'lang': 'lang',
        'output': 'output'
    }

    def __init__(self, account_id=None, ad_group_ad_approval_statuses=None, ad_group_ad_user_statuses=None, ad_group_criterion_approval_statuses=None, ad_group_criterion_ids=None, ad_group_criterion_user_statuses=None, ad_group_ids=None, ad_group_user_statuses=None, ad_ids=None, campaign_criterion_ids=None, campaign_ids=None, campaign_user_statuses=None, encoding=None, entity_types=None, export_fields=None, job_name=None, lang=None, output=None, local_vars_configuration=None):  # noqa: E501
        """CampaignExportServiceExportSetting - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._account_id = None
        self._ad_group_ad_approval_statuses = None
        self._ad_group_ad_user_statuses = None
        self._ad_group_criterion_approval_statuses = None
        self._ad_group_criterion_ids = None
        self._ad_group_criterion_user_statuses = None
        self._ad_group_ids = None
        self._ad_group_user_statuses = None
        self._ad_ids = None
        self._campaign_criterion_ids = None
        self._campaign_ids = None
        self._campaign_user_statuses = None
        self._encoding = None
        self._entity_types = None
        self._export_fields = None
        self._job_name = None
        self._lang = None
        self._output = None
        self.discriminator = None

        self.account_id = account_id
        self.ad_group_ad_approval_statuses = ad_group_ad_approval_statuses
        self.ad_group_ad_user_statuses = ad_group_ad_user_statuses
        self.ad_group_criterion_approval_statuses = ad_group_criterion_approval_statuses
        self.ad_group_criterion_ids = ad_group_criterion_ids
        self.ad_group_criterion_user_statuses = ad_group_criterion_user_statuses
        self.ad_group_ids = ad_group_ids
        self.ad_group_user_statuses = ad_group_user_statuses
        self.ad_ids = ad_ids
        self.campaign_criterion_ids = campaign_criterion_ids
        self.campaign_ids = campaign_ids
        self.campaign_user_statuses = campaign_user_statuses
        self.encoding = encoding
        self.entity_types = entity_types
        self.export_fields = export_fields
        self.job_name = job_name
        self.lang = lang
        self.output = output

    @property
    def account_id(self):
        """Gets the account_id of this CampaignExportServiceExportSetting.  # noqa: E501

        <div lang=\"ja\">アカウントIDです。<br>このフィールドは、必須です。</div> <div lang=\"en\">Account ID.<br>This field is required.</div>   # noqa: E501

        :return: The account_id of this CampaignExportServiceExportSetting.  # noqa: E501
        :rtype: int
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this CampaignExportServiceExportSetting.

        <div lang=\"ja\">アカウントIDです。<br>このフィールドは、必須です。</div> <div lang=\"en\">Account ID.<br>This field is required.</div>   # noqa: E501

        :param account_id: The account_id of this CampaignExportServiceExportSetting.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and account_id is None:  # noqa: E501
            raise ValueError("Invalid value for `account_id`, must not be `None`")  # noqa: E501

        self._account_id = account_id

    @property
    def ad_group_ad_approval_statuses(self):
        """Gets the ad_group_ad_approval_statuses of this CampaignExportServiceExportSetting.  # noqa: E501


        :return: The ad_group_ad_approval_statuses of this CampaignExportServiceExportSetting.  # noqa: E501
        :rtype: list[CampaignExportServiceApprovalStatus]
        """
        return self._ad_group_ad_approval_statuses

    @ad_group_ad_approval_statuses.setter
    def ad_group_ad_approval_statuses(self, ad_group_ad_approval_statuses):
        """Sets the ad_group_ad_approval_statuses of this CampaignExportServiceExportSetting.


        :param ad_group_ad_approval_statuses: The ad_group_ad_approval_statuses of this CampaignExportServiceExportSetting.  # noqa: E501
        :type: list[CampaignExportServiceApprovalStatus]
        """

        self._ad_group_ad_approval_statuses = ad_group_ad_approval_statuses

    @property
    def ad_group_ad_user_statuses(self):
        """Gets the ad_group_ad_user_statuses of this CampaignExportServiceExportSetting.  # noqa: E501


        :return: The ad_group_ad_user_statuses of this CampaignExportServiceExportSetting.  # noqa: E501
        :rtype: list[CampaignExportServiceUserStatus]
        """
        return self._ad_group_ad_user_statuses

    @ad_group_ad_user_statuses.setter
    def ad_group_ad_user_statuses(self, ad_group_ad_user_statuses):
        """Sets the ad_group_ad_user_statuses of this CampaignExportServiceExportSetting.


        :param ad_group_ad_user_statuses: The ad_group_ad_user_statuses of this CampaignExportServiceExportSetting.  # noqa: E501
        :type: list[CampaignExportServiceUserStatus]
        """

        self._ad_group_ad_user_statuses = ad_group_ad_user_statuses

    @property
    def ad_group_criterion_approval_statuses(self):
        """Gets the ad_group_criterion_approval_statuses of this CampaignExportServiceExportSetting.  # noqa: E501


        :return: The ad_group_criterion_approval_statuses of this CampaignExportServiceExportSetting.  # noqa: E501
        :rtype: list[CampaignExportServiceApprovalStatus]
        """
        return self._ad_group_criterion_approval_statuses

    @ad_group_criterion_approval_statuses.setter
    def ad_group_criterion_approval_statuses(self, ad_group_criterion_approval_statuses):
        """Sets the ad_group_criterion_approval_statuses of this CampaignExportServiceExportSetting.


        :param ad_group_criterion_approval_statuses: The ad_group_criterion_approval_statuses of this CampaignExportServiceExportSetting.  # noqa: E501
        :type: list[CampaignExportServiceApprovalStatus]
        """

        self._ad_group_criterion_approval_statuses = ad_group_criterion_approval_statuses

    @property
    def ad_group_criterion_ids(self):
        """Gets the ad_group_criterion_ids of this CampaignExportServiceExportSetting.  # noqa: E501

        <div lang=\"ja\">広告グループクライテリアIDです。<br>このフィールドは、省略可能となります。</div> <div lang=\"en\">Ad group criteria ID.<br>This field is optional.</div>   # noqa: E501

        :return: The ad_group_criterion_ids of this CampaignExportServiceExportSetting.  # noqa: E501
        :rtype: list[int]
        """
        return self._ad_group_criterion_ids

    @ad_group_criterion_ids.setter
    def ad_group_criterion_ids(self, ad_group_criterion_ids):
        """Sets the ad_group_criterion_ids of this CampaignExportServiceExportSetting.

        <div lang=\"ja\">広告グループクライテリアIDです。<br>このフィールドは、省略可能となります。</div> <div lang=\"en\">Ad group criteria ID.<br>This field is optional.</div>   # noqa: E501

        :param ad_group_criterion_ids: The ad_group_criterion_ids of this CampaignExportServiceExportSetting.  # noqa: E501
        :type: list[int]
        """

        self._ad_group_criterion_ids = ad_group_criterion_ids

    @property
    def ad_group_criterion_user_statuses(self):
        """Gets the ad_group_criterion_user_statuses of this CampaignExportServiceExportSetting.  # noqa: E501


        :return: The ad_group_criterion_user_statuses of this CampaignExportServiceExportSetting.  # noqa: E501
        :rtype: list[CampaignExportServiceUserStatus]
        """
        return self._ad_group_criterion_user_statuses

    @ad_group_criterion_user_statuses.setter
    def ad_group_criterion_user_statuses(self, ad_group_criterion_user_statuses):
        """Sets the ad_group_criterion_user_statuses of this CampaignExportServiceExportSetting.


        :param ad_group_criterion_user_statuses: The ad_group_criterion_user_statuses of this CampaignExportServiceExportSetting.  # noqa: E501
        :type: list[CampaignExportServiceUserStatus]
        """

        self._ad_group_criterion_user_statuses = ad_group_criterion_user_statuses

    @property
    def ad_group_ids(self):
        """Gets the ad_group_ids of this CampaignExportServiceExportSetting.  # noqa: E501

        <div lang=\"ja\">ダウンロード対象の広告グループIDです。<br> このフィールドは、省略可能となります。</div> <div lang=\"en\">Ad group ID of export objective.<br> This field is optional.</div>   # noqa: E501

        :return: The ad_group_ids of this CampaignExportServiceExportSetting.  # noqa: E501
        :rtype: list[int]
        """
        return self._ad_group_ids

    @ad_group_ids.setter
    def ad_group_ids(self, ad_group_ids):
        """Sets the ad_group_ids of this CampaignExportServiceExportSetting.

        <div lang=\"ja\">ダウンロード対象の広告グループIDです。<br> このフィールドは、省略可能となります。</div> <div lang=\"en\">Ad group ID of export objective.<br> This field is optional.</div>   # noqa: E501

        :param ad_group_ids: The ad_group_ids of this CampaignExportServiceExportSetting.  # noqa: E501
        :type: list[int]
        """

        self._ad_group_ids = ad_group_ids

    @property
    def ad_group_user_statuses(self):
        """Gets the ad_group_user_statuses of this CampaignExportServiceExportSetting.  # noqa: E501


        :return: The ad_group_user_statuses of this CampaignExportServiceExportSetting.  # noqa: E501
        :rtype: list[CampaignExportServiceUserStatus]
        """
        return self._ad_group_user_statuses

    @ad_group_user_statuses.setter
    def ad_group_user_statuses(self, ad_group_user_statuses):
        """Sets the ad_group_user_statuses of this CampaignExportServiceExportSetting.


        :param ad_group_user_statuses: The ad_group_user_statuses of this CampaignExportServiceExportSetting.  # noqa: E501
        :type: list[CampaignExportServiceUserStatus]
        """

        self._ad_group_user_statuses = ad_group_user_statuses

    @property
    def ad_ids(self):
        """Gets the ad_ids of this CampaignExportServiceExportSetting.  # noqa: E501

        <div lang=\"ja\">ダウンロード対象の広告IDです。<br> このフィールドは、省略可能となります。</div> <div lang=\"en\">Ad ID of export objective.<br> This field is optional.</div>   # noqa: E501

        :return: The ad_ids of this CampaignExportServiceExportSetting.  # noqa: E501
        :rtype: list[int]
        """
        return self._ad_ids

    @ad_ids.setter
    def ad_ids(self, ad_ids):
        """Sets the ad_ids of this CampaignExportServiceExportSetting.

        <div lang=\"ja\">ダウンロード対象の広告IDです。<br> このフィールドは、省略可能となります。</div> <div lang=\"en\">Ad ID of export objective.<br> This field is optional.</div>   # noqa: E501

        :param ad_ids: The ad_ids of this CampaignExportServiceExportSetting.  # noqa: E501
        :type: list[int]
        """

        self._ad_ids = ad_ids

    @property
    def campaign_criterion_ids(self):
        """Gets the campaign_criterion_ids of this CampaignExportServiceExportSetting.  # noqa: E501

        <div lang=\"ja\">キャンペーンクライテリアIDです。<br> このフィールドは、省略可能となります。</div> <div lang=\"en\">Campaign criteria ID.<br> This field is optional.</div>   # noqa: E501

        :return: The campaign_criterion_ids of this CampaignExportServiceExportSetting.  # noqa: E501
        :rtype: list[int]
        """
        return self._campaign_criterion_ids

    @campaign_criterion_ids.setter
    def campaign_criterion_ids(self, campaign_criterion_ids):
        """Sets the campaign_criterion_ids of this CampaignExportServiceExportSetting.

        <div lang=\"ja\">キャンペーンクライテリアIDです。<br> このフィールドは、省略可能となります。</div> <div lang=\"en\">Campaign criteria ID.<br> This field is optional.</div>   # noqa: E501

        :param campaign_criterion_ids: The campaign_criterion_ids of this CampaignExportServiceExportSetting.  # noqa: E501
        :type: list[int]
        """

        self._campaign_criterion_ids = campaign_criterion_ids

    @property
    def campaign_ids(self):
        """Gets the campaign_ids of this CampaignExportServiceExportSetting.  # noqa: E501

        <div lang=\"ja\">ダウンロード対象のキャンペーンIDです。<br> このフィールドは、省略可能となります。</div> <div lang=\"en\">Campaign ID of export objective.<br> This field is optional.</div>   # noqa: E501

        :return: The campaign_ids of this CampaignExportServiceExportSetting.  # noqa: E501
        :rtype: list[int]
        """
        return self._campaign_ids

    @campaign_ids.setter
    def campaign_ids(self, campaign_ids):
        """Sets the campaign_ids of this CampaignExportServiceExportSetting.

        <div lang=\"ja\">ダウンロード対象のキャンペーンIDです。<br> このフィールドは、省略可能となります。</div> <div lang=\"en\">Campaign ID of export objective.<br> This field is optional.</div>   # noqa: E501

        :param campaign_ids: The campaign_ids of this CampaignExportServiceExportSetting.  # noqa: E501
        :type: list[int]
        """

        self._campaign_ids = campaign_ids

    @property
    def campaign_user_statuses(self):
        """Gets the campaign_user_statuses of this CampaignExportServiceExportSetting.  # noqa: E501


        :return: The campaign_user_statuses of this CampaignExportServiceExportSetting.  # noqa: E501
        :rtype: list[CampaignExportServiceUserStatus]
        """
        return self._campaign_user_statuses

    @campaign_user_statuses.setter
    def campaign_user_statuses(self, campaign_user_statuses):
        """Sets the campaign_user_statuses of this CampaignExportServiceExportSetting.


        :param campaign_user_statuses: The campaign_user_statuses of this CampaignExportServiceExportSetting.  # noqa: E501
        :type: list[CampaignExportServiceUserStatus]
        """

        self._campaign_user_statuses = campaign_user_statuses

    @property
    def encoding(self):
        """Gets the encoding of this CampaignExportServiceExportSetting.  # noqa: E501


        :return: The encoding of this CampaignExportServiceExportSetting.  # noqa: E501
        :rtype: CampaignExportServiceEncoding
        """
        return self._encoding

    @encoding.setter
    def encoding(self, encoding):
        """Sets the encoding of this CampaignExportServiceExportSetting.


        :param encoding: The encoding of this CampaignExportServiceExportSetting.  # noqa: E501
        :type: CampaignExportServiceEncoding
        """

        self._encoding = encoding

    @property
    def entity_types(self):
        """Gets the entity_types of this CampaignExportServiceExportSetting.  # noqa: E501


        :return: The entity_types of this CampaignExportServiceExportSetting.  # noqa: E501
        :rtype: list[CampaignExportServiceEntityType]
        """
        return self._entity_types

    @entity_types.setter
    def entity_types(self, entity_types):
        """Sets the entity_types of this CampaignExportServiceExportSetting.


        :param entity_types: The entity_types of this CampaignExportServiceExportSetting.  # noqa: E501
        :type: list[CampaignExportServiceEntityType]
        """

        self._entity_types = entity_types

    @property
    def export_fields(self):
        """Gets the export_fields of this CampaignExportServiceExportSetting.  # noqa: E501

        <div lang=\"ja\">エクスポートするフィールドを指定します。<br> このフィールドは、省略可能となります。</div> <div lang=\"en\">Select which field to export.<br> This field is optional.</div>   # noqa: E501

        :return: The export_fields of this CampaignExportServiceExportSetting.  # noqa: E501
        :rtype: list[str]
        """
        return self._export_fields

    @export_fields.setter
    def export_fields(self, export_fields):
        """Sets the export_fields of this CampaignExportServiceExportSetting.

        <div lang=\"ja\">エクスポートするフィールドを指定します。<br> このフィールドは、省略可能となります。</div> <div lang=\"en\">Select which field to export.<br> This field is optional.</div>   # noqa: E501

        :param export_fields: The export_fields of this CampaignExportServiceExportSetting.  # noqa: E501
        :type: list[str]
        """

        self._export_fields = export_fields

    @property
    def job_name(self):
        """Gets the job_name of this CampaignExportServiceExportSetting.  # noqa: E501

        <div lang=\"ja\">ダウンロードするジョブの名称です。<br> このフィールドは、省略可能となります。</div> <div lang=\"en\">Job information for export.<br> This field is optional.</div>   # noqa: E501

        :return: The job_name of this CampaignExportServiceExportSetting.  # noqa: E501
        :rtype: str
        """
        return self._job_name

    @job_name.setter
    def job_name(self, job_name):
        """Sets the job_name of this CampaignExportServiceExportSetting.

        <div lang=\"ja\">ダウンロードするジョブの名称です。<br> このフィールドは、省略可能となります。</div> <div lang=\"en\">Job information for export.<br> This field is optional.</div>   # noqa: E501

        :param job_name: The job_name of this CampaignExportServiceExportSetting.  # noqa: E501
        :type: str
        """

        self._job_name = job_name

    @property
    def lang(self):
        """Gets the lang of this CampaignExportServiceExportSetting.  # noqa: E501


        :return: The lang of this CampaignExportServiceExportSetting.  # noqa: E501
        :rtype: CampaignExportServiceLang
        """
        return self._lang

    @lang.setter
    def lang(self, lang):
        """Sets the lang of this CampaignExportServiceExportSetting.


        :param lang: The lang of this CampaignExportServiceExportSetting.  # noqa: E501
        :type: CampaignExportServiceLang
        """

        self._lang = lang

    @property
    def output(self):
        """Gets the output of this CampaignExportServiceExportSetting.  # noqa: E501


        :return: The output of this CampaignExportServiceExportSetting.  # noqa: E501
        :rtype: CampaignExportServiceOutput
        """
        return self._output

    @output.setter
    def output(self, output):
        """Sets the output of this CampaignExportServiceExportSetting.


        :param output: The output of this CampaignExportServiceExportSetting.  # noqa: E501
        :type: CampaignExportServiceOutput
        """

        self._output = output

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
        if not isinstance(other, CampaignExportServiceExportSetting):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CampaignExportServiceExportSetting):
            return True

        return self.to_dict() != other.to_dict()

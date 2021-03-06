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


class RetargetingListServiceTargetingList(object):
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
        'closing_reason': 'RetargetingListServiceClosingReason',
        'default_target_list': 'RetargetingListServiceDefaultTargetList',
        'logical_target_list': 'RetargetingListServiceLogicalTargetList',
        'reach': 'int',
        'reach_storage_span': 'int',
        'reach_storage_status': 'RetargetingListServiceReachStorageStatus',
        'retargeting_account_status': 'RetargetingListServiceRetargetingAccountStatus',
        'rule_base_target_list': 'RetargetingListServiceRuleBaseTargetList',
        'target_list_description': 'str',
        'target_list_id': 'int',
        'target_list_name': 'str',
        'target_list_owner': 'RetargetingListServiceTargetListOwner',
        'target_list_track_id': 'int',
        'target_list_type': 'RetargetingListServiceTargetListType'
    }

    attribute_map = {
        'account_id': 'accountId',
        'closing_reason': 'closingReason',
        'default_target_list': 'defaultTargetList',
        'logical_target_list': 'logicalTargetList',
        'reach': 'reach',
        'reach_storage_span': 'reachStorageSpan',
        'reach_storage_status': 'reachStorageStatus',
        'retargeting_account_status': 'retargetingAccountStatus',
        'rule_base_target_list': 'ruleBaseTargetList',
        'target_list_description': 'targetListDescription',
        'target_list_id': 'targetListId',
        'target_list_name': 'targetListName',
        'target_list_owner': 'targetListOwner',
        'target_list_track_id': 'targetListTrackId',
        'target_list_type': 'targetListType'
    }

    def __init__(self, account_id=None, closing_reason=None, default_target_list=None, logical_target_list=None, reach=None, reach_storage_span=None, reach_storage_status=None, retargeting_account_status=None, rule_base_target_list=None, target_list_description=None, target_list_id=None, target_list_name=None, target_list_owner=None, target_list_track_id=None, target_list_type=None, local_vars_configuration=None):  # noqa: E501
        """RetargetingListServiceTargetingList - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._account_id = None
        self._closing_reason = None
        self._default_target_list = None
        self._logical_target_list = None
        self._reach = None
        self._reach_storage_span = None
        self._reach_storage_status = None
        self._retargeting_account_status = None
        self._rule_base_target_list = None
        self._target_list_description = None
        self._target_list_id = None
        self._target_list_name = None
        self._target_list_owner = None
        self._target_list_track_id = None
        self._target_list_type = None
        self.discriminator = None

        self.account_id = account_id
        self.closing_reason = closing_reason
        self.default_target_list = default_target_list
        self.logical_target_list = logical_target_list
        self.reach = reach
        self.reach_storage_span = reach_storage_span
        self.reach_storage_status = reach_storage_status
        self.retargeting_account_status = retargeting_account_status
        self.rule_base_target_list = rule_base_target_list
        self.target_list_description = target_list_description
        self.target_list_id = target_list_id
        self.target_list_name = target_list_name
        self.target_list_owner = target_list_owner
        self.target_list_track_id = target_list_track_id
        self.target_list_type = target_list_type

    @property
    def account_id(self):
        """Gets the account_id of this RetargetingListServiceTargetingList.  # noqa: E501

        <div lang=\"ja\">アカウントIDです。<br> このフィールドは、いずれの場合でも必須となります。</div> <div lang=\"en\">Account ID.<br>This field is required in any cases.</div>   # noqa: E501

        :return: The account_id of this RetargetingListServiceTargetingList.  # noqa: E501
        :rtype: int
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this RetargetingListServiceTargetingList.

        <div lang=\"ja\">アカウントIDです。<br> このフィールドは、いずれの場合でも必須となります。</div> <div lang=\"en\">Account ID.<br>This field is required in any cases.</div>   # noqa: E501

        :param account_id: The account_id of this RetargetingListServiceTargetingList.  # noqa: E501
        :type: int
        """

        self._account_id = account_id

    @property
    def closing_reason(self):
        """Gets the closing_reason of this RetargetingListServiceTargetingList.  # noqa: E501


        :return: The closing_reason of this RetargetingListServiceTargetingList.  # noqa: E501
        :rtype: RetargetingListServiceClosingReason
        """
        return self._closing_reason

    @closing_reason.setter
    def closing_reason(self, closing_reason):
        """Sets the closing_reason of this RetargetingListServiceTargetingList.


        :param closing_reason: The closing_reason of this RetargetingListServiceTargetingList.  # noqa: E501
        :type: RetargetingListServiceClosingReason
        """

        self._closing_reason = closing_reason

    @property
    def default_target_list(self):
        """Gets the default_target_list of this RetargetingListServiceTargetingList.  # noqa: E501


        :return: The default_target_list of this RetargetingListServiceTargetingList.  # noqa: E501
        :rtype: RetargetingListServiceDefaultTargetList
        """
        return self._default_target_list

    @default_target_list.setter
    def default_target_list(self, default_target_list):
        """Sets the default_target_list of this RetargetingListServiceTargetingList.


        :param default_target_list: The default_target_list of this RetargetingListServiceTargetingList.  # noqa: E501
        :type: RetargetingListServiceDefaultTargetList
        """

        self._default_target_list = default_target_list

    @property
    def logical_target_list(self):
        """Gets the logical_target_list of this RetargetingListServiceTargetingList.  # noqa: E501


        :return: The logical_target_list of this RetargetingListServiceTargetingList.  # noqa: E501
        :rtype: RetargetingListServiceLogicalTargetList
        """
        return self._logical_target_list

    @logical_target_list.setter
    def logical_target_list(self, logical_target_list):
        """Sets the logical_target_list of this RetargetingListServiceTargetingList.


        :param logical_target_list: The logical_target_list of this RetargetingListServiceTargetingList.  # noqa: E501
        :type: RetargetingListServiceLogicalTargetList
        """

        self._logical_target_list = logical_target_list

    @property
    def reach(self):
        """Gets the reach of this RetargetingListServiceTargetingList.  # noqa: E501

        <div lang=\"ja\">リストに蓄積されているユーザー数です。</div> <div lang=\"en\">Number of users stored to the list.</div>   # noqa: E501

        :return: The reach of this RetargetingListServiceTargetingList.  # noqa: E501
        :rtype: int
        """
        return self._reach

    @reach.setter
    def reach(self, reach):
        """Sets the reach of this RetargetingListServiceTargetingList.

        <div lang=\"ja\">リストに蓄積されているユーザー数です。</div> <div lang=\"en\">Number of users stored to the list.</div>   # noqa: E501

        :param reach: The reach of this RetargetingListServiceTargetingList.  # noqa: E501
        :type: int
        """

        self._reach = reach

    @property
    def reach_storage_span(self):
        """Gets the reach_storage_span of this RetargetingListServiceTargetingList.  # noqa: E501

        <div lang=\"ja\">Cookieを保持する日数です。<br> SET時、このフィールドは省略可能となります。<br>LogicalTargetListの場合、SET時にこのフィールドは無視されます。<br> ※Default：180<br> ※1-540日まで設定可能です。</div> <div lang=\"en\">Days to hold Cookie.<br> This field is optional in SET operation.<br> For LogicalTargetList, this field will be ignored in SET operation.<br> *Default: 180<br> *Can set from 1-540 days.</div>   # noqa: E501

        :return: The reach_storage_span of this RetargetingListServiceTargetingList.  # noqa: E501
        :rtype: int
        """
        return self._reach_storage_span

    @reach_storage_span.setter
    def reach_storage_span(self, reach_storage_span):
        """Sets the reach_storage_span of this RetargetingListServiceTargetingList.

        <div lang=\"ja\">Cookieを保持する日数です。<br> SET時、このフィールドは省略可能となります。<br>LogicalTargetListの場合、SET時にこのフィールドは無視されます。<br> ※Default：180<br> ※1-540日まで設定可能です。</div> <div lang=\"en\">Days to hold Cookie.<br> This field is optional in SET operation.<br> For LogicalTargetList, this field will be ignored in SET operation.<br> *Default: 180<br> *Can set from 1-540 days.</div>   # noqa: E501

        :param reach_storage_span: The reach_storage_span of this RetargetingListServiceTargetingList.  # noqa: E501
        :type: int
        """

        self._reach_storage_span = reach_storage_span

    @property
    def reach_storage_status(self):
        """Gets the reach_storage_status of this RetargetingListServiceTargetingList.  # noqa: E501


        :return: The reach_storage_status of this RetargetingListServiceTargetingList.  # noqa: E501
        :rtype: RetargetingListServiceReachStorageStatus
        """
        return self._reach_storage_status

    @reach_storage_status.setter
    def reach_storage_status(self, reach_storage_status):
        """Sets the reach_storage_status of this RetargetingListServiceTargetingList.


        :param reach_storage_status: The reach_storage_status of this RetargetingListServiceTargetingList.  # noqa: E501
        :type: RetargetingListServiceReachStorageStatus
        """

        self._reach_storage_status = reach_storage_status

    @property
    def retargeting_account_status(self):
        """Gets the retargeting_account_status of this RetargetingListServiceTargetingList.  # noqa: E501


        :return: The retargeting_account_status of this RetargetingListServiceTargetingList.  # noqa: E501
        :rtype: RetargetingListServiceRetargetingAccountStatus
        """
        return self._retargeting_account_status

    @retargeting_account_status.setter
    def retargeting_account_status(self, retargeting_account_status):
        """Sets the retargeting_account_status of this RetargetingListServiceTargetingList.


        :param retargeting_account_status: The retargeting_account_status of this RetargetingListServiceTargetingList.  # noqa: E501
        :type: RetargetingListServiceRetargetingAccountStatus
        """

        self._retargeting_account_status = retargeting_account_status

    @property
    def rule_base_target_list(self):
        """Gets the rule_base_target_list of this RetargetingListServiceTargetingList.  # noqa: E501


        :return: The rule_base_target_list of this RetargetingListServiceTargetingList.  # noqa: E501
        :rtype: RetargetingListServiceRuleBaseTargetList
        """
        return self._rule_base_target_list

    @rule_base_target_list.setter
    def rule_base_target_list(self, rule_base_target_list):
        """Sets the rule_base_target_list of this RetargetingListServiceTargetingList.


        :param rule_base_target_list: The rule_base_target_list of this RetargetingListServiceTargetingList.  # noqa: E501
        :type: RetargetingListServiceRuleBaseTargetList
        """

        self._rule_base_target_list = rule_base_target_list

    @property
    def target_list_description(self):
        """Gets the target_list_description of this RetargetingListServiceTargetingList.  # noqa: E501

        <div lang=\"ja\">ターゲットリストの説明です。<br> このフィールドは、いずれの場合でも省略可能となります。</div> <div lang=\"en\">Description of Target List.<br> This field is optional in any cases.</div>   # noqa: E501

        :return: The target_list_description of this RetargetingListServiceTargetingList.  # noqa: E501
        :rtype: str
        """
        return self._target_list_description

    @target_list_description.setter
    def target_list_description(self, target_list_description):
        """Sets the target_list_description of this RetargetingListServiceTargetingList.

        <div lang=\"ja\">ターゲットリストの説明です。<br> このフィールドは、いずれの場合でも省略可能となります。</div> <div lang=\"en\">Description of Target List.<br> This field is optional in any cases.</div>   # noqa: E501

        :param target_list_description: The target_list_description of this RetargetingListServiceTargetingList.  # noqa: E501
        :type: str
        """

        self._target_list_description = target_list_description

    @property
    def target_list_id(self):
        """Gets the target_list_id of this RetargetingListServiceTargetingList.  # noqa: E501

        <div lang=\"ja\">ターゲットリストIDです。<br> SET時、このフィールドは必須となります。</div> <div lang=\"en\">Target List ID.<br> This field is required in SET operation.</div>   # noqa: E501

        :return: The target_list_id of this RetargetingListServiceTargetingList.  # noqa: E501
        :rtype: int
        """
        return self._target_list_id

    @target_list_id.setter
    def target_list_id(self, target_list_id):
        """Sets the target_list_id of this RetargetingListServiceTargetingList.

        <div lang=\"ja\">ターゲットリストIDです。<br> SET時、このフィールドは必須となります。</div> <div lang=\"en\">Target List ID.<br> This field is required in SET operation.</div>   # noqa: E501

        :param target_list_id: The target_list_id of this RetargetingListServiceTargetingList.  # noqa: E501
        :type: int
        """

        self._target_list_id = target_list_id

    @property
    def target_list_name(self):
        """Gets the target_list_name of this RetargetingListServiceTargetingList.  # noqa: E501

        <div lang=\"ja\">ターゲットリスト名です。<br> ADD時にこのフィールドは必須となり、SET時にこのフィールドは省略可能となります。</div> <div lang=\"en\">Target List name.<br> This field is required in ADD operation, and is optional in SET operation.</div>   # noqa: E501

        :return: The target_list_name of this RetargetingListServiceTargetingList.  # noqa: E501
        :rtype: str
        """
        return self._target_list_name

    @target_list_name.setter
    def target_list_name(self, target_list_name):
        """Sets the target_list_name of this RetargetingListServiceTargetingList.

        <div lang=\"ja\">ターゲットリスト名です。<br> ADD時にこのフィールドは必須となり、SET時にこのフィールドは省略可能となります。</div> <div lang=\"en\">Target List name.<br> This field is required in ADD operation, and is optional in SET operation.</div>   # noqa: E501

        :param target_list_name: The target_list_name of this RetargetingListServiceTargetingList.  # noqa: E501
        :type: str
        """

        self._target_list_name = target_list_name

    @property
    def target_list_owner(self):
        """Gets the target_list_owner of this RetargetingListServiceTargetingList.  # noqa: E501


        :return: The target_list_owner of this RetargetingListServiceTargetingList.  # noqa: E501
        :rtype: RetargetingListServiceTargetListOwner
        """
        return self._target_list_owner

    @target_list_owner.setter
    def target_list_owner(self, target_list_owner):
        """Sets the target_list_owner of this RetargetingListServiceTargetingList.


        :param target_list_owner: The target_list_owner of this RetargetingListServiceTargetingList.  # noqa: E501
        :type: RetargetingListServiceTargetListOwner
        """

        self._target_list_owner = target_list_owner

    @property
    def target_list_track_id(self):
        """Gets the target_list_track_id of this RetargetingListServiceTargetingList.  # noqa: E501

        <div lang=\"ja\">ターゲットリストのトラッキング用IDです。</div> <div lang=\"en\">Tracking ID of Target list.</div>   # noqa: E501

        :return: The target_list_track_id of this RetargetingListServiceTargetingList.  # noqa: E501
        :rtype: int
        """
        return self._target_list_track_id

    @target_list_track_id.setter
    def target_list_track_id(self, target_list_track_id):
        """Sets the target_list_track_id of this RetargetingListServiceTargetingList.

        <div lang=\"ja\">ターゲットリストのトラッキング用IDです。</div> <div lang=\"en\">Tracking ID of Target list.</div>   # noqa: E501

        :param target_list_track_id: The target_list_track_id of this RetargetingListServiceTargetingList.  # noqa: E501
        :type: int
        """

        self._target_list_track_id = target_list_track_id

    @property
    def target_list_type(self):
        """Gets the target_list_type of this RetargetingListServiceTargetingList.  # noqa: E501


        :return: The target_list_type of this RetargetingListServiceTargetingList.  # noqa: E501
        :rtype: RetargetingListServiceTargetListType
        """
        return self._target_list_type

    @target_list_type.setter
    def target_list_type(self, target_list_type):
        """Sets the target_list_type of this RetargetingListServiceTargetingList.


        :param target_list_type: The target_list_type of this RetargetingListServiceTargetingList.  # noqa: E501
        :type: RetargetingListServiceTargetListType
        """

        self._target_list_type = target_list_type

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
        if not isinstance(other, RetargetingListServiceTargetingList):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RetargetingListServiceTargetingList):
            return True

        return self.to_dict() != other.to_dict()

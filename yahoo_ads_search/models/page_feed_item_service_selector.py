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


class PageFeedItemServiceSelector(object):
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
        'approval_statuses': 'list[PageFeedItemServiceApprovalStatus]',
        'feed_ids': 'list[int]',
        'number_results': 'int',
        'page_feed_custom_label': 'list[str]',
        'page_feed_url': 'list[PageFeedItemServicePageFeedUrl]',
        'start_index': 'int'
    }

    attribute_map = {
        'account_id': 'accountId',
        'approval_statuses': 'approvalStatuses',
        'feed_ids': 'feedIds',
        'number_results': 'numberResults',
        'page_feed_custom_label': 'pageFeedCustomLabel',
        'page_feed_url': 'pageFeedUrl',
        'start_index': 'startIndex'
    }

    def __init__(self, account_id=None, approval_statuses=None, feed_ids=None, number_results=500, page_feed_custom_label=None, page_feed_url=None, start_index=1, local_vars_configuration=None):  # noqa: E501
        """PageFeedItemServiceSelector - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._account_id = None
        self._approval_statuses = None
        self._feed_ids = None
        self._number_results = None
        self._page_feed_custom_label = None
        self._page_feed_url = None
        self._start_index = None
        self.discriminator = None

        self.account_id = account_id
        self.approval_statuses = approval_statuses
        self.feed_ids = feed_ids
        self.number_results = number_results
        self.page_feed_custom_label = page_feed_custom_label
        self.page_feed_url = page_feed_url
        self.start_index = start_index

    @property
    def account_id(self):
        """Gets the account_id of this PageFeedItemServiceSelector.  # noqa: E501

        <div lang=\"ja\">アカウントID</div> <div lang=\"en\">Account ID</div>   # noqa: E501

        :return: The account_id of this PageFeedItemServiceSelector.  # noqa: E501
        :rtype: int
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this PageFeedItemServiceSelector.

        <div lang=\"ja\">アカウントID</div> <div lang=\"en\">Account ID</div>   # noqa: E501

        :param account_id: The account_id of this PageFeedItemServiceSelector.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and account_id is None:  # noqa: E501
            raise ValueError("Invalid value for `account_id`, must not be `None`")  # noqa: E501

        self._account_id = account_id

    @property
    def approval_statuses(self):
        """Gets the approval_statuses of this PageFeedItemServiceSelector.  # noqa: E501


        :return: The approval_statuses of this PageFeedItemServiceSelector.  # noqa: E501
        :rtype: list[PageFeedItemServiceApprovalStatus]
        """
        return self._approval_statuses

    @approval_statuses.setter
    def approval_statuses(self, approval_statuses):
        """Sets the approval_statuses of this PageFeedItemServiceSelector.


        :param approval_statuses: The approval_statuses of this PageFeedItemServiceSelector.  # noqa: E501
        :type: list[PageFeedItemServiceApprovalStatus]
        """

        self._approval_statuses = approval_statuses

    @property
    def feed_ids(self):
        """Gets the feed_ids of this PageFeedItemServiceSelector.  # noqa: E501

        <div lang=\"ja\">フィードID</div> <div lang=\"en\">Feed ID</div>   # noqa: E501

        :return: The feed_ids of this PageFeedItemServiceSelector.  # noqa: E501
        :rtype: list[int]
        """
        return self._feed_ids

    @feed_ids.setter
    def feed_ids(self, feed_ids):
        """Sets the feed_ids of this PageFeedItemServiceSelector.

        <div lang=\"ja\">フィードID</div> <div lang=\"en\">Feed ID</div>   # noqa: E501

        :param feed_ids: The feed_ids of this PageFeedItemServiceSelector.  # noqa: E501
        :type: list[int]
        """

        self._feed_ids = feed_ids

    @property
    def number_results(self):
        """Gets the number_results of this PageFeedItemServiceSelector.  # noqa: E501

        <div lang=\"ja\">ページの最大件数です。このフィールドは、1以上を指定する必要があります。</div> <div lang=\"en\">Maximum number of results to return in this page. This field must be greater than or equal to 1. Also see Entity Limits per operation.</div>   # noqa: E501

        :return: The number_results of this PageFeedItemServiceSelector.  # noqa: E501
        :rtype: int
        """
        return self._number_results

    @number_results.setter
    def number_results(self, number_results):
        """Sets the number_results of this PageFeedItemServiceSelector.

        <div lang=\"ja\">ページの最大件数です。このフィールドは、1以上を指定する必要があります。</div> <div lang=\"en\">Maximum number of results to return in this page. This field must be greater than or equal to 1. Also see Entity Limits per operation.</div>   # noqa: E501

        :param number_results: The number_results of this PageFeedItemServiceSelector.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                number_results is not None and number_results > 10000):  # noqa: E501
            raise ValueError("Invalid value for `number_results`, must be a value less than or equal to `10000`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                number_results is not None and number_results < 1):  # noqa: E501
            raise ValueError("Invalid value for `number_results`, must be a value greater than or equal to `1`")  # noqa: E501

        self._number_results = number_results

    @property
    def page_feed_custom_label(self):
        """Gets the page_feed_custom_label of this PageFeedItemServiceSelector.  # noqa: E501

        <div lang=\"ja\">カスタムラベル</div> <div lang=\"en\">Custom label</div>   # noqa: E501

        :return: The page_feed_custom_label of this PageFeedItemServiceSelector.  # noqa: E501
        :rtype: list[str]
        """
        return self._page_feed_custom_label

    @page_feed_custom_label.setter
    def page_feed_custom_label(self, page_feed_custom_label):
        """Sets the page_feed_custom_label of this PageFeedItemServiceSelector.

        <div lang=\"ja\">カスタムラベル</div> <div lang=\"en\">Custom label</div>   # noqa: E501

        :param page_feed_custom_label: The page_feed_custom_label of this PageFeedItemServiceSelector.  # noqa: E501
        :type: list[str]
        """

        self._page_feed_custom_label = page_feed_custom_label

    @property
    def page_feed_url(self):
        """Gets the page_feed_url of this PageFeedItemServiceSelector.  # noqa: E501


        :return: The page_feed_url of this PageFeedItemServiceSelector.  # noqa: E501
        :rtype: list[PageFeedItemServicePageFeedUrl]
        """
        return self._page_feed_url

    @page_feed_url.setter
    def page_feed_url(self, page_feed_url):
        """Sets the page_feed_url of this PageFeedItemServiceSelector.


        :param page_feed_url: The page_feed_url of this PageFeedItemServiceSelector.  # noqa: E501
        :type: list[PageFeedItemServicePageFeedUrl]
        """

        self._page_feed_url = page_feed_url

    @property
    def start_index(self):
        """Gets the start_index of this PageFeedItemServiceSelector.  # noqa: E501

        <div lang=\"ja\">ページの先頭のインデックスです。このフィールドは、1以上を指定する必要があります。</div> <div lang=\"en\">Index of the first result to return in this page. This field must be greater than or equal to 1.</div>   # noqa: E501

        :return: The start_index of this PageFeedItemServiceSelector.  # noqa: E501
        :rtype: int
        """
        return self._start_index

    @start_index.setter
    def start_index(self, start_index):
        """Sets the start_index of this PageFeedItemServiceSelector.

        <div lang=\"ja\">ページの先頭のインデックスです。このフィールドは、1以上を指定する必要があります。</div> <div lang=\"en\">Index of the first result to return in this page. This field must be greater than or equal to 1.</div>   # noqa: E501

        :param start_index: The start_index of this PageFeedItemServiceSelector.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                start_index is not None and start_index < 1):  # noqa: E501
            raise ValueError("Invalid value for `start_index`, must be a value greater than or equal to `1`")  # noqa: E501

        self._start_index = start_index

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
        if not isinstance(other, PageFeedItemServiceSelector):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PageFeedItemServiceSelector):
            return True

        return self.to_dict() != other.to_dict()

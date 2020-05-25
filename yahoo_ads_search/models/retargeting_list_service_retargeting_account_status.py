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


class RetargetingListServiceRetargetingAccountStatus(object):
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
        'agree_date': 'str',
        'review_request_date': 'str',
        'review_status': 'RetargetingListServiceReviewStatus'
    }

    attribute_map = {
        'agree_date': 'agreeDate',
        'review_request_date': 'reviewRequestDate',
        'review_status': 'reviewStatus'
    }

    def __init__(self, agree_date=None, review_request_date=None, review_status=None, local_vars_configuration=None):  # noqa: E501
        """RetargetingListServiceRetargetingAccountStatus - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._agree_date = None
        self._review_request_date = None
        self._review_status = None
        self.discriminator = None

        self.agree_date = agree_date
        self.review_request_date = review_request_date
        self.review_status = review_status

    @property
    def agree_date(self):
        """Gets the agree_date of this RetargetingListServiceRetargetingAccountStatus.  # noqa: E501

        <div lang=\"ja\">規約同意日です。<br> ※YYYYMMDD形式です。</div> <div lang=\"en\">Agreement date.<br> *In YYYYMMDD format.</div>   # noqa: E501

        :return: The agree_date of this RetargetingListServiceRetargetingAccountStatus.  # noqa: E501
        :rtype: str
        """
        return self._agree_date

    @agree_date.setter
    def agree_date(self, agree_date):
        """Sets the agree_date of this RetargetingListServiceRetargetingAccountStatus.

        <div lang=\"ja\">規約同意日です。<br> ※YYYYMMDD形式です。</div> <div lang=\"en\">Agreement date.<br> *In YYYYMMDD format.</div>   # noqa: E501

        :param agree_date: The agree_date of this RetargetingListServiceRetargetingAccountStatus.  # noqa: E501
        :type: str
        """

        self._agree_date = agree_date

    @property
    def review_request_date(self):
        """Gets the review_request_date of this RetargetingListServiceRetargetingAccountStatus.  # noqa: E501

        <div lang=\"ja\">再審査依頼日です。<br> ※YYYYMMDD形式です。</div> <div lang=\"en\">Re-examination review request date.<br> *In YYYYMMDD format.</div>   # noqa: E501

        :return: The review_request_date of this RetargetingListServiceRetargetingAccountStatus.  # noqa: E501
        :rtype: str
        """
        return self._review_request_date

    @review_request_date.setter
    def review_request_date(self, review_request_date):
        """Sets the review_request_date of this RetargetingListServiceRetargetingAccountStatus.

        <div lang=\"ja\">再審査依頼日です。<br> ※YYYYMMDD形式です。</div> <div lang=\"en\">Re-examination review request date.<br> *In YYYYMMDD format.</div>   # noqa: E501

        :param review_request_date: The review_request_date of this RetargetingListServiceRetargetingAccountStatus.  # noqa: E501
        :type: str
        """

        self._review_request_date = review_request_date

    @property
    def review_status(self):
        """Gets the review_status of this RetargetingListServiceRetargetingAccountStatus.  # noqa: E501


        :return: The review_status of this RetargetingListServiceRetargetingAccountStatus.  # noqa: E501
        :rtype: RetargetingListServiceReviewStatus
        """
        return self._review_status

    @review_status.setter
    def review_status(self, review_status):
        """Sets the review_status of this RetargetingListServiceRetargetingAccountStatus.


        :param review_status: The review_status of this RetargetingListServiceRetargetingAccountStatus.  # noqa: E501
        :type: RetargetingListServiceReviewStatus
        """

        self._review_status = review_status

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
        if not isinstance(other, RetargetingListServiceRetargetingAccountStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RetargetingListServiceRetargetingAccountStatus):
            return True

        return self.to_dict() != other.to_dict()

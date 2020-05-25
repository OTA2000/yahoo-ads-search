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


class BidLandscapeServiceCriterionBidLandscape(object):
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
        'criterion_id': 'int'
    }

    attribute_map = {
        'criterion_id': 'criterionId'
    }

    def __init__(self, criterion_id=None, local_vars_configuration=None):  # noqa: E501
        """BidLandscapeServiceCriterionBidLandscape - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._criterion_id = None
        self.discriminator = None

        self.criterion_id = criterion_id

    @property
    def criterion_id(self):
        """Gets the criterion_id of this BidLandscapeServiceCriterionBidLandscape.  # noqa: E501

        <div lang=\"ja\">クライテリアIDです。</div> <div lang=\"en\">Criterion ID.</div>   # noqa: E501

        :return: The criterion_id of this BidLandscapeServiceCriterionBidLandscape.  # noqa: E501
        :rtype: int
        """
        return self._criterion_id

    @criterion_id.setter
    def criterion_id(self, criterion_id):
        """Sets the criterion_id of this BidLandscapeServiceCriterionBidLandscape.

        <div lang=\"ja\">クライテリアIDです。</div> <div lang=\"en\">Criterion ID.</div>   # noqa: E501

        :param criterion_id: The criterion_id of this BidLandscapeServiceCriterionBidLandscape.  # noqa: E501
        :type: int
        """

        self._criterion_id = criterion_id

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
        if not isinstance(other, BidLandscapeServiceCriterionBidLandscape):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BidLandscapeServiceCriterionBidLandscape):
            return True

        return self.to_dict() != other.to_dict()

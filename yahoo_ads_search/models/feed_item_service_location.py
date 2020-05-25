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


class FeedItemServiceLocation(object):
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
        'criterion_type_feed_item': 'FeedItemServiceCriterionTypeFeedItem',
        'geo_restriction': 'FeedItemServiceGeoRestriction',
        'is_remove': 'FeedItemServiceIsRemove',
        'target_id': 'str'
    }

    attribute_map = {
        'criterion_type_feed_item': 'criterionTypeFeedItem',
        'geo_restriction': 'geoRestriction',
        'is_remove': 'isRemove',
        'target_id': 'targetId'
    }

    def __init__(self, criterion_type_feed_item=None, geo_restriction=None, is_remove=None, target_id=None, local_vars_configuration=None):  # noqa: E501
        """FeedItemServiceLocation - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._criterion_type_feed_item = None
        self._geo_restriction = None
        self._is_remove = None
        self._target_id = None
        self.discriminator = None

        self.criterion_type_feed_item = criterion_type_feed_item
        self.geo_restriction = geo_restriction
        self.is_remove = is_remove
        self.target_id = target_id

    @property
    def criterion_type_feed_item(self):
        """Gets the criterion_type_feed_item of this FeedItemServiceLocation.  # noqa: E501


        :return: The criterion_type_feed_item of this FeedItemServiceLocation.  # noqa: E501
        :rtype: FeedItemServiceCriterionTypeFeedItem
        """
        return self._criterion_type_feed_item

    @criterion_type_feed_item.setter
    def criterion_type_feed_item(self, criterion_type_feed_item):
        """Sets the criterion_type_feed_item of this FeedItemServiceLocation.


        :param criterion_type_feed_item: The criterion_type_feed_item of this FeedItemServiceLocation.  # noqa: E501
        :type: FeedItemServiceCriterionTypeFeedItem
        """

        self._criterion_type_feed_item = criterion_type_feed_item

    @property
    def geo_restriction(self):
        """Gets the geo_restriction of this FeedItemServiceLocation.  # noqa: E501


        :return: The geo_restriction of this FeedItemServiceLocation.  # noqa: E501
        :rtype: FeedItemServiceGeoRestriction
        """
        return self._geo_restriction

    @geo_restriction.setter
    def geo_restriction(self, geo_restriction):
        """Sets the geo_restriction of this FeedItemServiceLocation.


        :param geo_restriction: The geo_restriction of this FeedItemServiceLocation.  # noqa: E501
        :type: FeedItemServiceGeoRestriction
        """

        self._geo_restriction = geo_restriction

    @property
    def is_remove(self):
        """Gets the is_remove of this FeedItemServiceLocation.  # noqa: E501


        :return: The is_remove of this FeedItemServiceLocation.  # noqa: E501
        :rtype: FeedItemServiceIsRemove
        """
        return self._is_remove

    @is_remove.setter
    def is_remove(self, is_remove):
        """Sets the is_remove of this FeedItemServiceLocation.


        :param is_remove: The is_remove of this FeedItemServiceLocation.  # noqa: E501
        :type: FeedItemServiceIsRemove
        """

        self._is_remove = is_remove

    @property
    def target_id(self):
        """Gets the target_id of this FeedItemServiceLocation.  # noqa: E501

        <div lang=\"ja\">地域種別コードです。<br> このフィールドは、ADD時に必須となり、SET時に省略可能となり、REMOVE時に無視されます。</div> <div lang=\"en\">FeedItemServiceLocation Type Code.<br> This field is required in ADD operation, is optional in SET operation, and will be ignored in REMOVE operation.</div>   # noqa: E501

        :return: The target_id of this FeedItemServiceLocation.  # noqa: E501
        :rtype: str
        """
        return self._target_id

    @target_id.setter
    def target_id(self, target_id):
        """Sets the target_id of this FeedItemServiceLocation.

        <div lang=\"ja\">地域種別コードです。<br> このフィールドは、ADD時に必須となり、SET時に省略可能となり、REMOVE時に無視されます。</div> <div lang=\"en\">FeedItemServiceLocation Type Code.<br> This field is required in ADD operation, is optional in SET operation, and will be ignored in REMOVE operation.</div>   # noqa: E501

        :param target_id: The target_id of this FeedItemServiceLocation.  # noqa: E501
        :type: str
        """

        self._target_id = target_id

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
        if not isinstance(other, FeedItemServiceLocation):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FeedItemServiceLocation):
            return True

        return self.to_dict() != other.to_dict()

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


class FeedItemServiceAttribute(object):
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
        'feed_attribute_id': 'int',
        'multiple_feed_item_attribute': 'FeedItemServiceMultipleFeedItemAttribute',
        'placeholder_field': 'FeedItemServicePlaceholderField',
        'simple_feed_item_attribute': 'FeedItemServiceSimpleFeedItemAttribute'
    }

    attribute_map = {
        'feed_attribute_id': 'feedAttributeId',
        'multiple_feed_item_attribute': 'multipleFeedItemAttribute',
        'placeholder_field': 'placeholderField',
        'simple_feed_item_attribute': 'simpleFeedItemAttribute'
    }

    def __init__(self, feed_attribute_id=None, multiple_feed_item_attribute=None, placeholder_field=None, simple_feed_item_attribute=None, local_vars_configuration=None):  # noqa: E501
        """FeedItemServiceAttribute - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._feed_attribute_id = None
        self._multiple_feed_item_attribute = None
        self._placeholder_field = None
        self._simple_feed_item_attribute = None
        self.discriminator = None

        self.feed_attribute_id = feed_attribute_id
        self.multiple_feed_item_attribute = multiple_feed_item_attribute
        self.placeholder_field = placeholder_field
        self.simple_feed_item_attribute = simple_feed_item_attribute

    @property
    def feed_attribute_id(self):
        """Gets the feed_attribute_id of this FeedItemServiceAttribute.  # noqa: E501

        <div lang=\"ja\">フィード属性IDです。<br> このフィールドは、ADDおよびSET時に無視されます。<br> ※アドカスタマイザーの場合は、ADDおよびSET時に必須となります。</div> <div lang=\"en\">Feed attribute ID.<br> This field will be ignored in ADD and SET operation.<br> *For AD_CUSTOMIZER, this field is required in ADD and SET operation.</div>   # noqa: E501

        :return: The feed_attribute_id of this FeedItemServiceAttribute.  # noqa: E501
        :rtype: int
        """
        return self._feed_attribute_id

    @feed_attribute_id.setter
    def feed_attribute_id(self, feed_attribute_id):
        """Sets the feed_attribute_id of this FeedItemServiceAttribute.

        <div lang=\"ja\">フィード属性IDです。<br> このフィールドは、ADDおよびSET時に無視されます。<br> ※アドカスタマイザーの場合は、ADDおよびSET時に必須となります。</div> <div lang=\"en\">Feed attribute ID.<br> This field will be ignored in ADD and SET operation.<br> *For AD_CUSTOMIZER, this field is required in ADD and SET operation.</div>   # noqa: E501

        :param feed_attribute_id: The feed_attribute_id of this FeedItemServiceAttribute.  # noqa: E501
        :type: int
        """

        self._feed_attribute_id = feed_attribute_id

    @property
    def multiple_feed_item_attribute(self):
        """Gets the multiple_feed_item_attribute of this FeedItemServiceAttribute.  # noqa: E501


        :return: The multiple_feed_item_attribute of this FeedItemServiceAttribute.  # noqa: E501
        :rtype: FeedItemServiceMultipleFeedItemAttribute
        """
        return self._multiple_feed_item_attribute

    @multiple_feed_item_attribute.setter
    def multiple_feed_item_attribute(self, multiple_feed_item_attribute):
        """Sets the multiple_feed_item_attribute of this FeedItemServiceAttribute.


        :param multiple_feed_item_attribute: The multiple_feed_item_attribute of this FeedItemServiceAttribute.  # noqa: E501
        :type: FeedItemServiceMultipleFeedItemAttribute
        """

        self._multiple_feed_item_attribute = multiple_feed_item_attribute

    @property
    def placeholder_field(self):
        """Gets the placeholder_field of this FeedItemServiceAttribute.  # noqa: E501


        :return: The placeholder_field of this FeedItemServiceAttribute.  # noqa: E501
        :rtype: FeedItemServicePlaceholderField
        """
        return self._placeholder_field

    @placeholder_field.setter
    def placeholder_field(self, placeholder_field):
        """Sets the placeholder_field of this FeedItemServiceAttribute.


        :param placeholder_field: The placeholder_field of this FeedItemServiceAttribute.  # noqa: E501
        :type: FeedItemServicePlaceholderField
        """

        self._placeholder_field = placeholder_field

    @property
    def simple_feed_item_attribute(self):
        """Gets the simple_feed_item_attribute of this FeedItemServiceAttribute.  # noqa: E501


        :return: The simple_feed_item_attribute of this FeedItemServiceAttribute.  # noqa: E501
        :rtype: FeedItemServiceSimpleFeedItemAttribute
        """
        return self._simple_feed_item_attribute

    @simple_feed_item_attribute.setter
    def simple_feed_item_attribute(self, simple_feed_item_attribute):
        """Sets the simple_feed_item_attribute of this FeedItemServiceAttribute.


        :param simple_feed_item_attribute: The simple_feed_item_attribute of this FeedItemServiceAttribute.  # noqa: E501
        :type: FeedItemServiceSimpleFeedItemAttribute
        """

        self._simple_feed_item_attribute = simple_feed_item_attribute

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
        if not isinstance(other, FeedItemServiceAttribute):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FeedItemServiceAttribute):
            return True

        return self.to_dict() != other.to_dict()

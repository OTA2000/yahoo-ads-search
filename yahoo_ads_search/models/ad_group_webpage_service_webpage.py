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


class AdGroupWebpageServiceWebpage(object):
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
        'parameter': 'AdGroupWebpageServiceWebpageParameter',
        'target_id': 'int',
        'target_track_id': 'int'
    }

    attribute_map = {
        'parameter': 'parameter',
        'target_id': 'targetId',
        'target_track_id': 'targetTrackId'
    }

    def __init__(self, parameter=None, target_id=None, target_track_id=None, local_vars_configuration=None):  # noqa: E501
        """AdGroupWebpageServiceWebpage - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._parameter = None
        self._target_id = None
        self._target_track_id = None
        self.discriminator = None

        self.parameter = parameter
        self.target_id = target_id
        self.target_track_id = target_track_id

    @property
    def parameter(self):
        """Gets the parameter of this AdGroupWebpageServiceWebpage.  # noqa: E501


        :return: The parameter of this AdGroupWebpageServiceWebpage.  # noqa: E501
        :rtype: AdGroupWebpageServiceWebpageParameter
        """
        return self._parameter

    @parameter.setter
    def parameter(self, parameter):
        """Sets the parameter of this AdGroupWebpageServiceWebpage.


        :param parameter: The parameter of this AdGroupWebpageServiceWebpage.  # noqa: E501
        :type: AdGroupWebpageServiceWebpageParameter
        """

        self._parameter = parameter

    @property
    def target_id(self):
        """Gets the target_id of this AdGroupWebpageServiceWebpage.  # noqa: E501

        <div lang=\"ja\">AdGroupWebpageServiceWebpageを識別するIDです。<br>このフィールドは、ADD時は無視され、SET時は必須となります。</div> <div lang=\"en\">Unique ID for each identify webpage.<br>This field will be ignored in ADD operation, and is required in SET operation.</div>   # noqa: E501

        :return: The target_id of this AdGroupWebpageServiceWebpage.  # noqa: E501
        :rtype: int
        """
        return self._target_id

    @target_id.setter
    def target_id(self, target_id):
        """Sets the target_id of this AdGroupWebpageServiceWebpage.

        <div lang=\"ja\">AdGroupWebpageServiceWebpageを識別するIDです。<br>このフィールドは、ADD時は無視され、SET時は必須となります。</div> <div lang=\"en\">Unique ID for each identify webpage.<br>This field will be ignored in ADD operation, and is required in SET operation.</div>   # noqa: E501

        :param target_id: The target_id of this AdGroupWebpageServiceWebpage.  # noqa: E501
        :type: int
        """

        self._target_id = target_id

    @property
    def target_track_id(self):
        """Gets the target_track_id of this AdGroupWebpageServiceWebpage.  # noqa: E501

        <div lang=\"ja\">AdGroupWebpageServiceWebpageを識別するトラッキングIDです。<br>このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。</div> <div lang=\"en\">Tracking ID for each identify webpage.<br>Although this field will be returned in the response, it will be ignored on input.</div>   # noqa: E501

        :return: The target_track_id of this AdGroupWebpageServiceWebpage.  # noqa: E501
        :rtype: int
        """
        return self._target_track_id

    @target_track_id.setter
    def target_track_id(self, target_track_id):
        """Sets the target_track_id of this AdGroupWebpageServiceWebpage.

        <div lang=\"ja\">AdGroupWebpageServiceWebpageを識別するトラッキングIDです。<br>このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。</div> <div lang=\"en\">Tracking ID for each identify webpage.<br>Although this field will be returned in the response, it will be ignored on input.</div>   # noqa: E501

        :param target_track_id: The target_track_id of this AdGroupWebpageServiceWebpage.  # noqa: E501
        :type: int
        """

        self._target_track_id = target_track_id

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
        if not isinstance(other, AdGroupWebpageServiceWebpage):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AdGroupWebpageServiceWebpage):
            return True

        return self.to_dict() != other.to_dict()

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


class CampaignTargetServiceScheduleTarget(object):
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
        'day_of_week': 'CampaignTargetServiceDayOfWeek',
        'end_hour': 'int',
        'end_minute': 'CampaignTargetServiceMinuteOfHour',
        'start_hour': 'int',
        'start_minute': 'CampaignTargetServiceMinuteOfHour'
    }

    attribute_map = {
        'day_of_week': 'dayOfWeek',
        'end_hour': 'endHour',
        'end_minute': 'endMinute',
        'start_hour': 'startHour',
        'start_minute': 'startMinute'
    }

    def __init__(self, day_of_week=None, end_hour=None, end_minute=None, start_hour=None, start_minute=None, local_vars_configuration=None):  # noqa: E501
        """CampaignTargetServiceScheduleTarget - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._day_of_week = None
        self._end_hour = None
        self._end_minute = None
        self._start_hour = None
        self._start_minute = None
        self.discriminator = None

        self.day_of_week = day_of_week
        self.end_hour = end_hour
        self.end_minute = end_minute
        self.start_hour = start_hour
        self.start_minute = start_minute

    @property
    def day_of_week(self):
        """Gets the day_of_week of this CampaignTargetServiceScheduleTarget.  # noqa: E501


        :return: The day_of_week of this CampaignTargetServiceScheduleTarget.  # noqa: E501
        :rtype: CampaignTargetServiceDayOfWeek
        """
        return self._day_of_week

    @day_of_week.setter
    def day_of_week(self, day_of_week):
        """Sets the day_of_week of this CampaignTargetServiceScheduleTarget.


        :param day_of_week: The day_of_week of this CampaignTargetServiceScheduleTarget.  # noqa: E501
        :type: CampaignTargetServiceDayOfWeek
        """

        self._day_of_week = day_of_week

    @property
    def end_hour(self):
        """Gets the end_hour of this CampaignTargetServiceScheduleTarget.  # noqa: E501

        <div lang=\"ja\">24時間表示の終了時刻です。<br>このフィールドは、ADD時に必須となります。</div> <div lang=\"en\">Ending hour in 24 hour time.<br>This field is required in ADD operation.</div>   # noqa: E501

        :return: The end_hour of this CampaignTargetServiceScheduleTarget.  # noqa: E501
        :rtype: int
        """
        return self._end_hour

    @end_hour.setter
    def end_hour(self, end_hour):
        """Sets the end_hour of this CampaignTargetServiceScheduleTarget.

        <div lang=\"ja\">24時間表示の終了時刻です。<br>このフィールドは、ADD時に必須となります。</div> <div lang=\"en\">Ending hour in 24 hour time.<br>This field is required in ADD operation.</div>   # noqa: E501

        :param end_hour: The end_hour of this CampaignTargetServiceScheduleTarget.  # noqa: E501
        :type: int
        """

        self._end_hour = end_hour

    @property
    def end_minute(self):
        """Gets the end_minute of this CampaignTargetServiceScheduleTarget.  # noqa: E501


        :return: The end_minute of this CampaignTargetServiceScheduleTarget.  # noqa: E501
        :rtype: CampaignTargetServiceMinuteOfHour
        """
        return self._end_minute

    @end_minute.setter
    def end_minute(self, end_minute):
        """Sets the end_minute of this CampaignTargetServiceScheduleTarget.


        :param end_minute: The end_minute of this CampaignTargetServiceScheduleTarget.  # noqa: E501
        :type: CampaignTargetServiceMinuteOfHour
        """

        self._end_minute = end_minute

    @property
    def start_hour(self):
        """Gets the start_hour of this CampaignTargetServiceScheduleTarget.  # noqa: E501

        <div lang=\"ja\">24時間表示の開始時刻です。<br>このフィールドは、ADD時に必須となります。</div> <div lang=\"en\">Starting hour in 24 hour time.<br>This field is required in ADD operation.</div>   # noqa: E501

        :return: The start_hour of this CampaignTargetServiceScheduleTarget.  # noqa: E501
        :rtype: int
        """
        return self._start_hour

    @start_hour.setter
    def start_hour(self, start_hour):
        """Sets the start_hour of this CampaignTargetServiceScheduleTarget.

        <div lang=\"ja\">24時間表示の開始時刻です。<br>このフィールドは、ADD時に必須となります。</div> <div lang=\"en\">Starting hour in 24 hour time.<br>This field is required in ADD operation.</div>   # noqa: E501

        :param start_hour: The start_hour of this CampaignTargetServiceScheduleTarget.  # noqa: E501
        :type: int
        """

        self._start_hour = start_hour

    @property
    def start_minute(self):
        """Gets the start_minute of this CampaignTargetServiceScheduleTarget.  # noqa: E501


        :return: The start_minute of this CampaignTargetServiceScheduleTarget.  # noqa: E501
        :rtype: CampaignTargetServiceMinuteOfHour
        """
        return self._start_minute

    @start_minute.setter
    def start_minute(self, start_minute):
        """Sets the start_minute of this CampaignTargetServiceScheduleTarget.


        :param start_minute: The start_minute of this CampaignTargetServiceScheduleTarget.  # noqa: E501
        :type: CampaignTargetServiceMinuteOfHour
        """

        self._start_minute = start_minute

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
        if not isinstance(other, CampaignTargetServiceScheduleTarget):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CampaignTargetServiceScheduleTarget):
            return True

        return self.to_dict() != other.to_dict()

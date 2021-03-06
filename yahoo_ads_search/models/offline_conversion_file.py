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


class OfflineConversionFile(object):
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
        'upload_id': 'int',
        'upload_file_name': 'str',
        'upload_type': 'OfflineConversionServiceUploadType',
        'uploaded_date': 'str',
        'upload_source_type': 'OfflineConversionServiceUploadSourceType',
        'process_status': 'OfflineConversionServiceProcessStatus'
    }

    attribute_map = {
        'account_id': 'accountId',
        'upload_id': 'uploadId',
        'upload_file_name': 'uploadFileName',
        'upload_type': 'uploadType',
        'uploaded_date': 'uploadedDate',
        'upload_source_type': 'uploadSourceType',
        'process_status': 'processStatus'
    }

    def __init__(self, account_id=None, upload_id=None, upload_file_name=None, upload_type=None, uploaded_date=None, upload_source_type=None, process_status=None, local_vars_configuration=None):  # noqa: E501
        """OfflineConversionFile - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._account_id = None
        self._upload_id = None
        self._upload_file_name = None
        self._upload_type = None
        self._uploaded_date = None
        self._upload_source_type = None
        self._process_status = None
        self.discriminator = None

        self.account_id = account_id
        self.upload_id = upload_id
        self.upload_file_name = upload_file_name
        self.upload_type = upload_type
        self.uploaded_date = uploaded_date
        self.upload_source_type = upload_source_type
        self.process_status = process_status

    @property
    def account_id(self):
        """Gets the account_id of this OfflineConversionFile.  # noqa: E501

        <div lang=\"ja\">アカウントIDです。</div> <div lang=\"en\">Account ID.</div>   # noqa: E501

        :return: The account_id of this OfflineConversionFile.  # noqa: E501
        :rtype: int
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this OfflineConversionFile.

        <div lang=\"ja\">アカウントIDです。</div> <div lang=\"en\">Account ID.</div>   # noqa: E501

        :param account_id: The account_id of this OfflineConversionFile.  # noqa: E501
        :type: int
        """

        self._account_id = account_id

    @property
    def upload_id(self):
        """Gets the upload_id of this OfflineConversionFile.  # noqa: E501

        <div lang=\"ja\">アップロードIDです。</div> <div lang=\"en\">Upload ID.</div>   # noqa: E501

        :return: The upload_id of this OfflineConversionFile.  # noqa: E501
        :rtype: int
        """
        return self._upload_id

    @upload_id.setter
    def upload_id(self, upload_id):
        """Sets the upload_id of this OfflineConversionFile.

        <div lang=\"ja\">アップロードIDです。</div> <div lang=\"en\">Upload ID.</div>   # noqa: E501

        :param upload_id: The upload_id of this OfflineConversionFile.  # noqa: E501
        :type: int
        """

        self._upload_id = upload_id

    @property
    def upload_file_name(self):
        """Gets the upload_file_name of this OfflineConversionFile.  # noqa: E501

        <div lang=\"ja\">アップロードファイル名です。</div> <div lang=\"en\">Upload file name.</div>   # noqa: E501

        :return: The upload_file_name of this OfflineConversionFile.  # noqa: E501
        :rtype: str
        """
        return self._upload_file_name

    @upload_file_name.setter
    def upload_file_name(self, upload_file_name):
        """Sets the upload_file_name of this OfflineConversionFile.

        <div lang=\"ja\">アップロードファイル名です。</div> <div lang=\"en\">Upload file name.</div>   # noqa: E501

        :param upload_file_name: The upload_file_name of this OfflineConversionFile.  # noqa: E501
        :type: str
        """

        self._upload_file_name = upload_file_name

    @property
    def upload_type(self):
        """Gets the upload_type of this OfflineConversionFile.  # noqa: E501


        :return: The upload_type of this OfflineConversionFile.  # noqa: E501
        :rtype: OfflineConversionServiceUploadType
        """
        return self._upload_type

    @upload_type.setter
    def upload_type(self, upload_type):
        """Sets the upload_type of this OfflineConversionFile.


        :param upload_type: The upload_type of this OfflineConversionFile.  # noqa: E501
        :type: OfflineConversionServiceUploadType
        """

        self._upload_type = upload_type

    @property
    def uploaded_date(self):
        """Gets the uploaded_date of this OfflineConversionFile.  # noqa: E501

        <div lang=\"ja\">アップロード日時です。</div> <div lang=\"en\">Upload date and time.</div>   # noqa: E501

        :return: The uploaded_date of this OfflineConversionFile.  # noqa: E501
        :rtype: str
        """
        return self._uploaded_date

    @uploaded_date.setter
    def uploaded_date(self, uploaded_date):
        """Sets the uploaded_date of this OfflineConversionFile.

        <div lang=\"ja\">アップロード日時です。</div> <div lang=\"en\">Upload date and time.</div>   # noqa: E501

        :param uploaded_date: The uploaded_date of this OfflineConversionFile.  # noqa: E501
        :type: str
        """

        self._uploaded_date = uploaded_date

    @property
    def upload_source_type(self):
        """Gets the upload_source_type of this OfflineConversionFile.  # noqa: E501


        :return: The upload_source_type of this OfflineConversionFile.  # noqa: E501
        :rtype: OfflineConversionServiceUploadSourceType
        """
        return self._upload_source_type

    @upload_source_type.setter
    def upload_source_type(self, upload_source_type):
        """Sets the upload_source_type of this OfflineConversionFile.


        :param upload_source_type: The upload_source_type of this OfflineConversionFile.  # noqa: E501
        :type: OfflineConversionServiceUploadSourceType
        """

        self._upload_source_type = upload_source_type

    @property
    def process_status(self):
        """Gets the process_status of this OfflineConversionFile.  # noqa: E501


        :return: The process_status of this OfflineConversionFile.  # noqa: E501
        :rtype: OfflineConversionServiceProcessStatus
        """
        return self._process_status

    @process_status.setter
    def process_status(self, process_status):
        """Sets the process_status of this OfflineConversionFile.


        :param process_status: The process_status of this OfflineConversionFile.  # noqa: E501
        :type: OfflineConversionServiceProcessStatus
        """

        self._process_status = process_status

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
        if not isinstance(other, OfflineConversionFile):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OfflineConversionFile):
            return True

        return self.to_dict() != other.to_dict()

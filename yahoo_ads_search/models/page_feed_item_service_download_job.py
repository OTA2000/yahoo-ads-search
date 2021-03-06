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


class PageFeedItemServiceDownloadJob(object):
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
        'bulk_encoding': 'PageFeedItemServiceBulkEncoding',
        'bulk_lang': 'PageFeedItemServiceBulkLang',
        'bulk_output': 'PageFeedItemServiceBulkOutput',
        'download_job_status': 'PageFeedItemServiceDownloadJobStatus',
        'end_date': 'str',
        'feed_ids': 'list[int]',
        'job_id': 'int',
        'progress': 'int',
        'start_date': 'str'
    }

    attribute_map = {
        'account_id': 'accountId',
        'bulk_encoding': 'bulkEncoding',
        'bulk_lang': 'bulkLang',
        'bulk_output': 'bulkOutput',
        'download_job_status': 'downloadJobStatus',
        'end_date': 'endDate',
        'feed_ids': 'feedIds',
        'job_id': 'jobId',
        'progress': 'progress',
        'start_date': 'startDate'
    }

    def __init__(self, account_id=None, bulk_encoding=None, bulk_lang=None, bulk_output=None, download_job_status=None, end_date=None, feed_ids=None, job_id=None, progress=None, start_date=None, local_vars_configuration=None):  # noqa: E501
        """PageFeedItemServiceDownloadJob - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._account_id = None
        self._bulk_encoding = None
        self._bulk_lang = None
        self._bulk_output = None
        self._download_job_status = None
        self._end_date = None
        self._feed_ids = None
        self._job_id = None
        self._progress = None
        self._start_date = None
        self.discriminator = None

        self.account_id = account_id
        self.bulk_encoding = bulk_encoding
        self.bulk_lang = bulk_lang
        self.bulk_output = bulk_output
        self.download_job_status = download_job_status
        self.end_date = end_date
        self.feed_ids = feed_ids
        self.job_id = job_id
        self.progress = progress
        self.start_date = start_date

    @property
    def account_id(self):
        """Gets the account_id of this PageFeedItemServiceDownloadJob.  # noqa: E501

        <div lang=\"ja\">アカウントIDです。<br> このフィールドは必須です。</div> <div lang=\"en\">Account ID.<br> This field is required.</div>   # noqa: E501

        :return: The account_id of this PageFeedItemServiceDownloadJob.  # noqa: E501
        :rtype: int
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this PageFeedItemServiceDownloadJob.

        <div lang=\"ja\">アカウントIDです。<br> このフィールドは必須です。</div> <div lang=\"en\">Account ID.<br> This field is required.</div>   # noqa: E501

        :param account_id: The account_id of this PageFeedItemServiceDownloadJob.  # noqa: E501
        :type: int
        """

        self._account_id = account_id

    @property
    def bulk_encoding(self):
        """Gets the bulk_encoding of this PageFeedItemServiceDownloadJob.  # noqa: E501


        :return: The bulk_encoding of this PageFeedItemServiceDownloadJob.  # noqa: E501
        :rtype: PageFeedItemServiceBulkEncoding
        """
        return self._bulk_encoding

    @bulk_encoding.setter
    def bulk_encoding(self, bulk_encoding):
        """Sets the bulk_encoding of this PageFeedItemServiceDownloadJob.


        :param bulk_encoding: The bulk_encoding of this PageFeedItemServiceDownloadJob.  # noqa: E501
        :type: PageFeedItemServiceBulkEncoding
        """

        self._bulk_encoding = bulk_encoding

    @property
    def bulk_lang(self):
        """Gets the bulk_lang of this PageFeedItemServiceDownloadJob.  # noqa: E501


        :return: The bulk_lang of this PageFeedItemServiceDownloadJob.  # noqa: E501
        :rtype: PageFeedItemServiceBulkLang
        """
        return self._bulk_lang

    @bulk_lang.setter
    def bulk_lang(self, bulk_lang):
        """Sets the bulk_lang of this PageFeedItemServiceDownloadJob.


        :param bulk_lang: The bulk_lang of this PageFeedItemServiceDownloadJob.  # noqa: E501
        :type: PageFeedItemServiceBulkLang
        """

        self._bulk_lang = bulk_lang

    @property
    def bulk_output(self):
        """Gets the bulk_output of this PageFeedItemServiceDownloadJob.  # noqa: E501


        :return: The bulk_output of this PageFeedItemServiceDownloadJob.  # noqa: E501
        :rtype: PageFeedItemServiceBulkOutput
        """
        return self._bulk_output

    @bulk_output.setter
    def bulk_output(self, bulk_output):
        """Sets the bulk_output of this PageFeedItemServiceDownloadJob.


        :param bulk_output: The bulk_output of this PageFeedItemServiceDownloadJob.  # noqa: E501
        :type: PageFeedItemServiceBulkOutput
        """

        self._bulk_output = bulk_output

    @property
    def download_job_status(self):
        """Gets the download_job_status of this PageFeedItemServiceDownloadJob.  # noqa: E501


        :return: The download_job_status of this PageFeedItemServiceDownloadJob.  # noqa: E501
        :rtype: PageFeedItemServiceDownloadJobStatus
        """
        return self._download_job_status

    @download_job_status.setter
    def download_job_status(self, download_job_status):
        """Sets the download_job_status of this PageFeedItemServiceDownloadJob.


        :param download_job_status: The download_job_status of this PageFeedItemServiceDownloadJob.  # noqa: E501
        :type: PageFeedItemServiceDownloadJobStatus
        """

        self._download_job_status = download_job_status

    @property
    def end_date(self):
        """Gets the end_date of this PageFeedItemServiceDownloadJob.  # noqa: E501

        <div lang=\"ja\">ジョブの終了日です。<br> このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。<br> 形式：yyyyMMddHHmmss</div><div lang=\"en\">End date of job.<br> Although this field will be returned in the response, it will be ignored on input.  <br> Format:yyyyMMddHHmmss</div>   # noqa: E501

        :return: The end_date of this PageFeedItemServiceDownloadJob.  # noqa: E501
        :rtype: str
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this PageFeedItemServiceDownloadJob.

        <div lang=\"ja\">ジョブの終了日です。<br> このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。<br> 形式：yyyyMMddHHmmss</div><div lang=\"en\">End date of job.<br> Although this field will be returned in the response, it will be ignored on input.  <br> Format:yyyyMMddHHmmss</div>   # noqa: E501

        :param end_date: The end_date of this PageFeedItemServiceDownloadJob.  # noqa: E501
        :type: str
        """

        self._end_date = end_date

    @property
    def feed_ids(self):
        """Gets the feed_ids of this PageFeedItemServiceDownloadJob.  # noqa: E501

        <div lang=\"ja\">フィードIDです。<br> このフィールドは必須です。</div> <div lang=\"en\">Feed ID.<br> This field is required.</div>   # noqa: E501

        :return: The feed_ids of this PageFeedItemServiceDownloadJob.  # noqa: E501
        :rtype: list[int]
        """
        return self._feed_ids

    @feed_ids.setter
    def feed_ids(self, feed_ids):
        """Sets the feed_ids of this PageFeedItemServiceDownloadJob.

        <div lang=\"ja\">フィードIDです。<br> このフィールドは必須です。</div> <div lang=\"en\">Feed ID.<br> This field is required.</div>   # noqa: E501

        :param feed_ids: The feed_ids of this PageFeedItemServiceDownloadJob.  # noqa: E501
        :type: list[int]
        """

        self._feed_ids = feed_ids

    @property
    def job_id(self):
        """Gets the job_id of this PageFeedItemServiceDownloadJob.  # noqa: E501

        <div lang=\"ja\">ジョブIDです。<br> このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。</div> <div lang=\"en\">Job ID.<br> Although this field will be returned in the response, it will be ignored on input.</div>   # noqa: E501

        :return: The job_id of this PageFeedItemServiceDownloadJob.  # noqa: E501
        :rtype: int
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this PageFeedItemServiceDownloadJob.

        <div lang=\"ja\">ジョブIDです。<br> このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。</div> <div lang=\"en\">Job ID.<br> Although this field will be returned in the response, it will be ignored on input.</div>   # noqa: E501

        :param job_id: The job_id of this PageFeedItemServiceDownloadJob.  # noqa: E501
        :type: int
        """

        self._job_id = job_id

    @property
    def progress(self):
        """Gets the progress of this PageFeedItemServiceDownloadJob.  # noqa: E501

        <div lang=\"ja\">ジョブの進捗状況です。<br> このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。</div> <div lang=\"en\">Progress of page feed item job.<br> Although this field will be returned in the response, it will be ignored on input.</div>   # noqa: E501

        :return: The progress of this PageFeedItemServiceDownloadJob.  # noqa: E501
        :rtype: int
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        """Sets the progress of this PageFeedItemServiceDownloadJob.

        <div lang=\"ja\">ジョブの進捗状況です。<br> このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。</div> <div lang=\"en\">Progress of page feed item job.<br> Although this field will be returned in the response, it will be ignored on input.</div>   # noqa: E501

        :param progress: The progress of this PageFeedItemServiceDownloadJob.  # noqa: E501
        :type: int
        """

        self._progress = progress

    @property
    def start_date(self):
        """Gets the start_date of this PageFeedItemServiceDownloadJob.  # noqa: E501

        <div lang=\"ja\">ジョブの開始日です。<br>このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。 <br> 形式：yyyyMMddHHmmss </div> <div lang=\"en\">Start date of job.<br> Although this field will be returned in the response, it will be ignored on input.<br> Format:yyyyMMddHHmmss</div>   # noqa: E501

        :return: The start_date of this PageFeedItemServiceDownloadJob.  # noqa: E501
        :rtype: str
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this PageFeedItemServiceDownloadJob.

        <div lang=\"ja\">ジョブの開始日です。<br>このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。 <br> 形式：yyyyMMddHHmmss </div> <div lang=\"en\">Start date of job.<br> Although this field will be returned in the response, it will be ignored on input.<br> Format:yyyyMMddHHmmss</div>   # noqa: E501

        :param start_date: The start_date of this PageFeedItemServiceDownloadJob.  # noqa: E501
        :type: str
        """

        self._start_date = start_date

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
        if not isinstance(other, PageFeedItemServiceDownloadJob):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PageFeedItemServiceDownloadJob):
            return True

        return self.to_dict() != other.to_dict()

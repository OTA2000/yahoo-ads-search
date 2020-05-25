# coding: utf-8

"""
    Yahoo!広告 検索広告 API リファレンス / Yahoo! Ads Search Ads API Reference

    <div lang=\"ja\">Yahoo!広告 検索広告 APIのWebサービスについて説明します。<br> 「Try it out」のご利用には、事前にアプリケーションの登録が必要です。また、アプリケーションのリダイレクトURIの1つに<br> https://yahoojp-marketing.github.io/ads-search-api-documents/oauth2-redirect.htmlを登録してください。 </div> <div lang=\"en\">Search Ads API Web Services supported in Yahoo! Ads API.<br> When you use \"Try it out\", you need to register your application in advance.<br> As one of redirect URI for application, you need to set \"https://yahoojp-marketing.github.io/ads-search-api-documents/oauth2-redirect.html\". </div>   # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from yahoo_ads_search.api_client import ApiClient
from yahoo_ads_search.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class AdGroupFeedServiceApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def ad_group_feed_service_get_post(self, **kwargs):  # noqa: E501
        """ad_group_feed_service_get_post  # noqa: E501

        <div lang=\"ja\">広告グループに設定されているFeedItem情報を取得します。</div> <div lang=\"en\">Returns FeedItem information of ad groups.</div>   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.ad_group_feed_service_get_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param AdGroupFeedServiceSelector ad_group_feed_service_selector:
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: AdGroupFeedServiceGetResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.ad_group_feed_service_get_post_with_http_info(**kwargs)  # noqa: E501

    def ad_group_feed_service_get_post_with_http_info(self, **kwargs):  # noqa: E501
        """ad_group_feed_service_get_post  # noqa: E501

        <div lang=\"ja\">広告グループに設定されているFeedItem情報を取得します。</div> <div lang=\"en\">Returns FeedItem information of ad groups.</div>   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.ad_group_feed_service_get_post_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param AdGroupFeedServiceSelector ad_group_feed_service_selector:
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(AdGroupFeedServiceGetResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'ad_group_feed_service_selector'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method ad_group_feed_service_get_post" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'ad_group_feed_service_selector' in local_var_params:
            body_params = local_var_params['ad_group_feed_service_selector']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oAuth']  # noqa: E501

        return self.api_client.call_api(
            '/AdGroupFeedService/get', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AdGroupFeedServiceGetResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def ad_group_feed_service_set_post(self, **kwargs):  # noqa: E501
        """ad_group_feed_service_set_post  # noqa: E501

        <div lang=\"ja\">広告グループにFeedItem情報を追加・更新・解除（削除）します。更新は常に上書きされるため追加分を含めて更新する必要があります。<br> ・FeedItem情報を解除するときは空の情報で更新します。<br> ・1リクエストで異なるキャンペーン配下の広告グループに対してFeedItem情報の設定が可能です。<br> ・1つの広告グループに設定できるFeedItem情報は、QUICKLINKS、CALLEXTENSIONでそれぞれ20件までです。<br> ・CALLEXTENSIONについては1広告グループあたり1件の設定をお薦めします。<br> ・1リクエスト内で同一のadGroupIdに複数のFeedItem情報を設定できません。</div> <div lang=\"en\">Add, update or release(remove) FeedItem information of ad group.<br> Update will overwrite the old information, so have to include the additional information on every updates.<br> ・To release FeedItem information, update with blank data.<br> ・It is possible to set FeedItem information to ad groups in different campaigns by single request.<br> ・FeedItem information that can be set for a single ad group is up to 20 for each QUICKLINKS, CALLEXTENSION.<br> ・As for CALLEXTENSION, We recommend setting only one phone number per ad group.<br> ・It is not possible to set multiple FeedItem information to an adGroupId by single request.</div>   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.ad_group_feed_service_set_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param AdGroupFeedServiceOperation ad_group_feed_service_operation:
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: AdGroupFeedServiceMutateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.ad_group_feed_service_set_post_with_http_info(**kwargs)  # noqa: E501

    def ad_group_feed_service_set_post_with_http_info(self, **kwargs):  # noqa: E501
        """ad_group_feed_service_set_post  # noqa: E501

        <div lang=\"ja\">広告グループにFeedItem情報を追加・更新・解除（削除）します。更新は常に上書きされるため追加分を含めて更新する必要があります。<br> ・FeedItem情報を解除するときは空の情報で更新します。<br> ・1リクエストで異なるキャンペーン配下の広告グループに対してFeedItem情報の設定が可能です。<br> ・1つの広告グループに設定できるFeedItem情報は、QUICKLINKS、CALLEXTENSIONでそれぞれ20件までです。<br> ・CALLEXTENSIONについては1広告グループあたり1件の設定をお薦めします。<br> ・1リクエスト内で同一のadGroupIdに複数のFeedItem情報を設定できません。</div> <div lang=\"en\">Add, update or release(remove) FeedItem information of ad group.<br> Update will overwrite the old information, so have to include the additional information on every updates.<br> ・To release FeedItem information, update with blank data.<br> ・It is possible to set FeedItem information to ad groups in different campaigns by single request.<br> ・FeedItem information that can be set for a single ad group is up to 20 for each QUICKLINKS, CALLEXTENSION.<br> ・As for CALLEXTENSION, We recommend setting only one phone number per ad group.<br> ・It is not possible to set multiple FeedItem information to an adGroupId by single request.</div>   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.ad_group_feed_service_set_post_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param AdGroupFeedServiceOperation ad_group_feed_service_operation:
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(AdGroupFeedServiceMutateResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'ad_group_feed_service_operation'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method ad_group_feed_service_set_post" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'ad_group_feed_service_operation' in local_var_params:
            body_params = local_var_params['ad_group_feed_service_operation']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oAuth']  # noqa: E501

        return self.api_client.call_api(
            '/AdGroupFeedService/set', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AdGroupFeedServiceMutateResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

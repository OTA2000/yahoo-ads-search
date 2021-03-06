# coding: utf-8

"""
    Yahoo!広告 検索広告 API リファレンス / Yahoo! Ads Search Ads API Reference

    <div lang=\"ja\">Yahoo!広告 検索広告 APIのWebサービスについて説明します。<br> 「Try it out」のご利用には、事前にアプリケーションの登録が必要です。また、アプリケーションのリダイレクトURIの1つに<br> https://yahoojp-marketing.github.io/ads-search-api-documents/oauth2-redirect.htmlを登録してください。 </div> <div lang=\"en\">Search Ads API Web Services supported in Yahoo! Ads API.<br> When you use \"Try it out\", you need to register your application in advance.<br> As one of redirect URI for application, you need to set \"https://yahoojp-marketing.github.io/ads-search-api-documents/oauth2-redirect.html\". </div>   # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import yahoo_ads_search
from yahoo_ads_search.models.page_feed_item_service_page import PageFeedItemServicePage  # noqa: E501
from yahoo_ads_search.rest import ApiException

class TestPageFeedItemServicePage(unittest.TestCase):
    """PageFeedItemServicePage unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PageFeedItemServicePage
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = yahoo_ads_search.models.page_feed_item_service_page.PageFeedItemServicePage()  # noqa: E501
        if include_optional :
            return PageFeedItemServicePage(
                total_num_entries = 56,
                values = [
                    yahoo_ads_search.models.page_feed_item_service_return_value.PageFeedItemServiceReturnValue(
                        errors = [
                            yahoo_ads_search.models.error.Error(
                                code = '0',
                                message = '0',
                                details = [
                                    yahoo_ads_search.models.error_detail.ErrorDetail(
                                        request_key = '0',
                                        request_value = '0', )
                                    ], )
                            ],
                        operation_succeeded = True,
                        page_feed_item = yahoo_ads_search.models.page_feed_item.PageFeedItem(
                            account_id = 56,
                            approval_status = 'APPROVED',
                            disapproval_reason_codes = [
                                '0'
                                ],
                            disapproval_reason_comment = '0',
                            feed_id = 56,
                            page_feed_custom_label = '0',
                            page_feed_item_id = 56,
                            page_feed_url = '0', ), )
                    ]
            )
        else :
            return PageFeedItemServicePage(
        )

    def testPageFeedItemServicePage(self):
        """Test PageFeedItemServicePage"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()

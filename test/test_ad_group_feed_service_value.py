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
from yahoo_ads_search.models.ad_group_feed_service_value import AdGroupFeedServiceValue  # noqa: E501
from yahoo_ads_search.rest import ApiException

class TestAdGroupFeedServiceValue(unittest.TestCase):
    """AdGroupFeedServiceValue unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AdGroupFeedServiceValue
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = yahoo_ads_search.models.ad_group_feed_service_value.AdGroupFeedServiceValue()  # noqa: E501
        if include_optional :
            return AdGroupFeedServiceValue(
                ad_group_feed_list = yahoo_ads_search.models.ad_group_feed_service_list.AdGroupFeedServiceList(
                    account_id = 56,
                    ad_group_feed = [
                        yahoo_ads_search.models.ad_group_feed.AdGroupFeed(
                            account_id = 56,
                            ad_group_id = 56,
                            campaign_id = 56,
                            feed_item_id = 56,
                            placeholder_type = 'QUICKLINK', )
                        ],
                    ad_group_id = 56,
                    campaign_id = 56,
                    placeholder_type = 'QUICKLINK', ),
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
                operation_succeeded = True
            )
        else :
            return AdGroupFeedServiceValue(
        )

    def testAdGroupFeedServiceValue(self):
        """Test AdGroupFeedServiceValue"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
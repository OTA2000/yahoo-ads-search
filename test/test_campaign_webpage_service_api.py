# coding: utf-8

"""
    Yahoo!広告 検索広告 API リファレンス / Yahoo! Ads Search Ads API Reference

    <div lang=\"ja\">Yahoo!広告 検索広告 APIのWebサービスについて説明します。<br> 「Try it out」のご利用には、事前にアプリケーションの登録が必要です。また、アプリケーションのリダイレクトURIの1つに<br> https://yahoojp-marketing.github.io/ads-search-api-documents/oauth2-redirect.htmlを登録してください。 </div> <div lang=\"en\">Search Ads API Web Services supported in Yahoo! Ads API.<br> When you use \"Try it out\", you need to register your application in advance.<br> As one of redirect URI for application, you need to set \"https://yahoojp-marketing.github.io/ads-search-api-documents/oauth2-redirect.html\". </div>   # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import yahoo_ads_search
from yahoo_ads_search.api.campaign_webpage_service_api import CampaignWebpageServiceApi  # noqa: E501
from yahoo_ads_search.rest import ApiException


class TestCampaignWebpageServiceApi(unittest.TestCase):
    """CampaignWebpageServiceApi unit test stubs"""

    def setUp(self):
        self.api = yahoo_ads_search.api.campaign_webpage_service_api.CampaignWebpageServiceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_campaign_webpage_service_add_post(self):
        """Test case for campaign_webpage_service_add_post

        """
        pass

    def test_campaign_webpage_service_get_post(self):
        """Test case for campaign_webpage_service_get_post

        """
        pass

    def test_campaign_webpage_service_remove_post(self):
        """Test case for campaign_webpage_service_remove_post

        """
        pass


if __name__ == '__main__':
    unittest.main()

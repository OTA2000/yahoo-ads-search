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
from yahoo_ads_search.models.campaign_service_settings import CampaignServiceSettings  # noqa: E501
from yahoo_ads_search.rest import ApiException

class TestCampaignServiceSettings(unittest.TestCase):
    """CampaignServiceSettings unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CampaignServiceSettings
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = yahoo_ads_search.models.campaign_service_settings.CampaignServiceSettings()  # noqa: E501
        if include_optional :
            return CampaignServiceSettings(
                dynamic_ads_for_search_setting = yahoo_ads_search.models.campaign_service_dynamic_ads_for_search_setting.CampaignServiceDynamicAdsForSearchSetting(
                    feed_ids = [
                        56
                        ], ),
                geo_target_type_setting = yahoo_ads_search.models.campaign_service_geo_target_type_setting.CampaignServiceGeoTargetTypeSetting(
                    negative_geo_target_type = 'DONT_CARE',
                    positive_geo_target_type = 'DONT_CARE', ),
                setting_type = 'GEO_TARGET_TYPE_SETTING',
                targeting_setting = yahoo_ads_search.models.campaign_service_targeting_setting.CampaignServiceTargetingSetting(
                    target_all = 'ACTIVE', )
            )
        else :
            return CampaignServiceSettings(
        )

    def testCampaignServiceSettings(self):
        """Test CampaignServiceSettings"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()

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
from yahoo_ads_search.models.ad_group_ad_service_operation import AdGroupAdServiceOperation  # noqa: E501
from yahoo_ads_search.rest import ApiException

class TestAdGroupAdServiceOperation(unittest.TestCase):
    """AdGroupAdServiceOperation unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AdGroupAdServiceOperation
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = yahoo_ads_search.models.ad_group_ad_service_operation.AdGroupAdServiceOperation()  # noqa: E501
        if include_optional :
            return AdGroupAdServiceOperation(
                account_id = 56,
                operand = [
                    yahoo_ads_search.models.ad_group_ad.AdGroupAd(
                        account_id = 56,
                        ad = yahoo_ads_search.models.ad_group_ad_service_ad.AdGroupAdServiceAd(
                            ad_type = 'TEXT_AD2',
                            additional_advanced_mobile_urls = [
                                yahoo_ads_search.models.ad_group_ad_service_additional_advanced_mobile_urls.AdGroupAdServiceAdditionalAdvancedMobileUrls(
                                    advanced_mobile_url = '0',
                                    disapproval_reason_codes = [
                                        '0'
                                        ], )
                                ],
                            additional_advanced_urls = [
                                yahoo_ads_search.models.ad_group_ad_service_additional_advanced_urls.AdGroupAdServiceAdditionalAdvancedUrls(
                                    advanced_url = '0', )
                                ],
                            advanced_mobile_url = '0',
                            advanced_url = '0',
                            app_ad = yahoo_ads_search.models.ad_group_ad_service_app_ad.AdGroupAdServiceAppAd(
                                app_id = '0',
                                app_store = 'IOS',
                                description2 = '0', ),
                            custom_parameters = yahoo_ads_search.models.ad_group_ad_service_custom_parameters.AdGroupAdServiceCustomParameters(
                                is_remove = 'TRUE',
                                parameters = [
                                    yahoo_ads_search.models.ad_group_ad_service_custom_parameter.AdGroupAdServiceCustomParameter(
                                        key = '0',
                                        value = '0', )
                                    ], ),
                            description = '0',
                            device_preference = 'SMART_PHONE',
                            display_url = '0',
                            extended_text_ad = yahoo_ads_search.models.ad_group_ad_service_extended_text_ad.AdGroupAdServiceExtendedTextAd(
                                headline2 = '0',
                                headline3 = '0',
                                description2 = '0',
                                path1 = '0',
                                path2 = '0', ),
                            headline = '0',
                            text_ad2 = yahoo_ads_search.models.ad_group_ad_service_text_ad2.AdGroupAdServiceTextAd2(
                                description2 = '0', ),
                            tracking_url = '0',
                            url = '0', ),
                        ad_group_id = 56,
                        ad_group_name = '0',
                        ad_group_track_id = 56,
                        ad_id = 56,
                        ad_name = '0',
                        ad_track_id = 56,
                        approval_status = 'APPROVED',
                        campaign_id = 56,
                        campaign_name = '0',
                        campaign_track_id = 56,
                        disapproval_reason_codes = [
                            '0'
                            ],
                        feed_id = 56,
                        invalided_trademarks = [
                            '0'
                            ],
                        labels = [
                            yahoo_ads_search.models.ad_group_ad_service_label.AdGroupAdServiceLabel(
                                color = '0',
                                description = '0',
                                label_id = 56,
                                label_name = '0', )
                            ],
                        trademark_status = 'NO_RESTRICTION',
                        user_status = 'ACTIVE', )
                    ]
            )
        else :
            return AdGroupAdServiceOperation(
                account_id = 56,
                operand = [
                    yahoo_ads_search.models.ad_group_ad.AdGroupAd(
                        account_id = 56,
                        ad = yahoo_ads_search.models.ad_group_ad_service_ad.AdGroupAdServiceAd(
                            ad_type = 'TEXT_AD2',
                            additional_advanced_mobile_urls = [
                                yahoo_ads_search.models.ad_group_ad_service_additional_advanced_mobile_urls.AdGroupAdServiceAdditionalAdvancedMobileUrls(
                                    advanced_mobile_url = '0',
                                    disapproval_reason_codes = [
                                        '0'
                                        ], )
                                ],
                            additional_advanced_urls = [
                                yahoo_ads_search.models.ad_group_ad_service_additional_advanced_urls.AdGroupAdServiceAdditionalAdvancedUrls(
                                    advanced_url = '0', )
                                ],
                            advanced_mobile_url = '0',
                            advanced_url = '0',
                            app_ad = yahoo_ads_search.models.ad_group_ad_service_app_ad.AdGroupAdServiceAppAd(
                                app_id = '0',
                                app_store = 'IOS',
                                description2 = '0', ),
                            custom_parameters = yahoo_ads_search.models.ad_group_ad_service_custom_parameters.AdGroupAdServiceCustomParameters(
                                is_remove = 'TRUE',
                                parameters = [
                                    yahoo_ads_search.models.ad_group_ad_service_custom_parameter.AdGroupAdServiceCustomParameter(
                                        key = '0',
                                        value = '0', )
                                    ], ),
                            description = '0',
                            device_preference = 'SMART_PHONE',
                            display_url = '0',
                            extended_text_ad = yahoo_ads_search.models.ad_group_ad_service_extended_text_ad.AdGroupAdServiceExtendedTextAd(
                                headline2 = '0',
                                headline3 = '0',
                                description2 = '0',
                                path1 = '0',
                                path2 = '0', ),
                            headline = '0',
                            text_ad2 = yahoo_ads_search.models.ad_group_ad_service_text_ad2.AdGroupAdServiceTextAd2(
                                description2 = '0', ),
                            tracking_url = '0',
                            url = '0', ),
                        ad_group_id = 56,
                        ad_group_name = '0',
                        ad_group_track_id = 56,
                        ad_id = 56,
                        ad_name = '0',
                        ad_track_id = 56,
                        approval_status = 'APPROVED',
                        campaign_id = 56,
                        campaign_name = '0',
                        campaign_track_id = 56,
                        disapproval_reason_codes = [
                            '0'
                            ],
                        feed_id = 56,
                        invalided_trademarks = [
                            '0'
                            ],
                        labels = [
                            yahoo_ads_search.models.ad_group_ad_service_label.AdGroupAdServiceLabel(
                                color = '0',
                                description = '0',
                                label_id = 56,
                                label_name = '0', )
                            ],
                        trademark_status = 'NO_RESTRICTION',
                        user_status = 'ACTIVE', )
                    ],
        )

    def testAdGroupAdServiceOperation(self):
        """Test AdGroupAdServiceOperation"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()

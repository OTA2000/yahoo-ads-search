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
from yahoo_ads_search.models.ad_group_service_operation import AdGroupServiceOperation  # noqa: E501
from yahoo_ads_search.rest import ApiException

class TestAdGroupServiceOperation(unittest.TestCase):
    """AdGroupServiceOperation unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AdGroupServiceOperation
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = yahoo_ads_search.models.ad_group_service_operation.AdGroupServiceOperation()  # noqa: E501
        if include_optional :
            return AdGroupServiceOperation(
                account_id = 56,
                operand = [
                    yahoo_ads_search.models.ad_group.AdGroup(
                        account_id = 56,
                        ad_group_ad_rotation_mode = yahoo_ads_search.models.ad_group_service_ad_group_ad_rotation_mode.AdGroupServiceAdGroupAdRotationMode(
                            ad_rotation_mode = 'OPTIMIZE', ),
                        ad_group_id = 56,
                        ad_group_name = '0',
                        ad_group_track_id = 56,
                        bid = yahoo_ads_search.models.ad_group_service_bid.AdGroupServiceBid(
                            bid_source = 'ADGROUP',
                            max_cpc = 56, ),
                        campaign_id = 56,
                        campaign_name = '0',
                        campaign_track_id = 56,
                        custom_parameters = yahoo_ads_search.models.ad_group_service_custom_parameters.AdGroupServiceCustomParameters(
                            is_remove = 'TRUE',
                            parameters = [
                                yahoo_ads_search.models.ad_group_service_custom_parameter.AdGroupServiceCustomParameter(
                                    key = '0',
                                    value = '0', )
                                ], ),
                        labels = [
                            yahoo_ads_search.models.ad_group_service_label.AdGroupServiceLabel(
                                color = '0',
                                description = '0',
                                label_id = 56,
                                label_name = '0', )
                            ],
                        settings = yahoo_ads_search.models.ad_group_service_settings.AdGroupServiceSettings(
                            criterion_type = 'TARGET_LIST',
                            targeting_setting = yahoo_ads_search.models.ad_group_service_targeting_setting.AdGroupServiceTargetingSetting(
                                target_all = 'ACTIVE', ), ),
                        tracking_url = '0',
                        url_review_data = yahoo_ads_search.models.ad_group_service_url_review_data.AdGroupServiceUrlReviewData(
                            disapproval_reason_codes = [
                                '0'
                                ],
                            disapproval_review_url = yahoo_ads_search.models.ad_group_service_review_url.AdGroupServiceReviewUrl(
                                tracking_url = '0', ),
                            in_review_url = yahoo_ads_search.models.ad_group_service_review_url.AdGroupServiceReviewUrl(
                                tracking_url = '0', ),
                            url_approval_status = 'NONE', ),
                        user_status = 'ACTIVE', )
                    ]
            )
        else :
            return AdGroupServiceOperation(
                account_id = 56,
                operand = [
                    yahoo_ads_search.models.ad_group.AdGroup(
                        account_id = 56,
                        ad_group_ad_rotation_mode = yahoo_ads_search.models.ad_group_service_ad_group_ad_rotation_mode.AdGroupServiceAdGroupAdRotationMode(
                            ad_rotation_mode = 'OPTIMIZE', ),
                        ad_group_id = 56,
                        ad_group_name = '0',
                        ad_group_track_id = 56,
                        bid = yahoo_ads_search.models.ad_group_service_bid.AdGroupServiceBid(
                            bid_source = 'ADGROUP',
                            max_cpc = 56, ),
                        campaign_id = 56,
                        campaign_name = '0',
                        campaign_track_id = 56,
                        custom_parameters = yahoo_ads_search.models.ad_group_service_custom_parameters.AdGroupServiceCustomParameters(
                            is_remove = 'TRUE',
                            parameters = [
                                yahoo_ads_search.models.ad_group_service_custom_parameter.AdGroupServiceCustomParameter(
                                    key = '0',
                                    value = '0', )
                                ], ),
                        labels = [
                            yahoo_ads_search.models.ad_group_service_label.AdGroupServiceLabel(
                                color = '0',
                                description = '0',
                                label_id = 56,
                                label_name = '0', )
                            ],
                        settings = yahoo_ads_search.models.ad_group_service_settings.AdGroupServiceSettings(
                            criterion_type = 'TARGET_LIST',
                            targeting_setting = yahoo_ads_search.models.ad_group_service_targeting_setting.AdGroupServiceTargetingSetting(
                                target_all = 'ACTIVE', ), ),
                        tracking_url = '0',
                        url_review_data = yahoo_ads_search.models.ad_group_service_url_review_data.AdGroupServiceUrlReviewData(
                            disapproval_reason_codes = [
                                '0'
                                ],
                            disapproval_review_url = yahoo_ads_search.models.ad_group_service_review_url.AdGroupServiceReviewUrl(
                                tracking_url = '0', ),
                            in_review_url = yahoo_ads_search.models.ad_group_service_review_url.AdGroupServiceReviewUrl(
                                tracking_url = '0', ),
                            url_approval_status = 'NONE', ),
                        user_status = 'ACTIVE', )
                    ],
        )

    def testAdGroupServiceOperation(self):
        """Test AdGroupServiceOperation"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()

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
from yahoo_ads_search.models.conversion_tracker_service_return_value import ConversionTrackerServiceReturnValue  # noqa: E501
from yahoo_ads_search.rest import ApiException

class TestConversionTrackerServiceReturnValue(unittest.TestCase):
    """ConversionTrackerServiceReturnValue unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ConversionTrackerServiceReturnValue
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = yahoo_ads_search.models.conversion_tracker_service_return_value.ConversionTrackerServiceReturnValue()  # noqa: E501
        if include_optional :
            return ConversionTrackerServiceReturnValue(
                values = [
                    yahoo_ads_search.models.conversion_tracker_service_value.ConversionTrackerServiceValue(
                        conversion_tracker = yahoo_ads_search.models.conversion_tracker.ConversionTracker(
                            account_id = 56,
                            all_conversion_value = '0',
                            all_conversions = 56,
                            app_conversion = yahoo_ads_search.models.conversion_tracker_service_app_conversion.ConversionTrackerServiceAppConversion(
                                app_conversion_type = 'DOWNLOAD',
                                app_id = '0',
                                app_platform = 'ANDROID_MARKET',
                                app_postback_url = yahoo_ads_search.models.conversion_tracker_service_app_postback_url.ConversionTrackerServiceAppPostbackUrl(
                                    app_postback_url_clear_flag = 'TRUE',
                                    url = '0', ),
                                snippet_id = 56,
                                snippet_label = '0', ),
                            category = 'DEFAULT',
                            conversion_counting_type = 'ONE_PER_CLICK',
                            conversion_tracker_id = 56,
                            conversion_tracker_name = '0',
                            conversion_tracker_type = 'WEB_CONVERSION',
                            conversion_value = '0',
                            conversions = 56,
                            exclude_from_bidding = 'TRUE',
                            measurement_period = 56,
                            most_recent_conversion_date = '0',
                            status = 'ENABLED',
                            user_revenue_value = '0',
                            web_conversion = yahoo_ads_search.models.conversion_tracker_service_web_conversion.ConversionTrackerServiceWebConversion(
                                markup_language = 'HTML',
                                snippet = '0',
                                advanced_snippet = '0',
                                tracking_code_type = 'WEBPAGE', ), ),
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
                        operation_succeeded = True, )
                    ]
            )
        else :
            return ConversionTrackerServiceReturnValue(
        )

    def testConversionTrackerServiceReturnValue(self):
        """Test ConversionTrackerServiceReturnValue"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()

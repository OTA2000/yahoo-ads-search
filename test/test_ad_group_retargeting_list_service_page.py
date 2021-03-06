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
from yahoo_ads_search.models.ad_group_retargeting_list_service_page import AdGroupRetargetingListServicePage  # noqa: E501
from yahoo_ads_search.rest import ApiException

class TestAdGroupRetargetingListServicePage(unittest.TestCase):
    """AdGroupRetargetingListServicePage unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AdGroupRetargetingListServicePage
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = yahoo_ads_search.models.ad_group_retargeting_list_service_page.AdGroupRetargetingListServicePage()  # noqa: E501
        if include_optional :
            return AdGroupRetargetingListServicePage(
                total_num_entries = 56,
                values = [
                    yahoo_ads_search.models.ad_group_retargeting_list_service_value.AdGroupRetargetingListServiceValue(
                        ad_group_retargeting_list = yahoo_ads_search.models.ad_group_retargeting_list.AdGroupRetargetingList(
                            account_id = 56,
                            ad_group_id = 56,
                            ad_group_name = '0',
                            bid_multiplier = 1.337,
                            campaign_id = 56,
                            campaign_name = '0',
                            criterion_target_list = yahoo_ads_search.models.ad_group_retargeting_list_service_criterion_target_list.AdGroupRetargetingListServiceCriterionTargetList(
                                retargeting_track_id = 56,
                                target_list_id = 56,
                                target_list_name = '0', ),
                            excluded_type = 'INCLUDED', ),
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
            return AdGroupRetargetingListServicePage(
        )

    def testAdGroupRetargetingListServicePage(self):
        """Test AdGroupRetargetingListServicePage"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()

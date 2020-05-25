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
from yahoo_ads_search.models.bidding_strategy_service_mutate_response import BiddingStrategyServiceMutateResponse  # noqa: E501
from yahoo_ads_search.rest import ApiException

class TestBiddingStrategyServiceMutateResponse(unittest.TestCase):
    """BiddingStrategyServiceMutateResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test BiddingStrategyServiceMutateResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = yahoo_ads_search.models.bidding_strategy_service_mutate_response.BiddingStrategyServiceMutateResponse()  # noqa: E501
        if include_optional :
            return BiddingStrategyServiceMutateResponse(
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
                rid = '0',
                rval = yahoo_ads_search.models.bidding_strategy_service_return_value.BiddingStrategyServiceReturnValue(
                    values = [
                        yahoo_ads_search.models.bidding_strategy_service_value.BiddingStrategyServiceValue(
                            bidding_strategy = yahoo_ads_search.models.bidding_strategy.BiddingStrategy(
                                account_id = 56,
                                bidding_scheme = yahoo_ads_search.models.bidding_strategy_service_bidding_scheme.BiddingStrategyServiceBiddingScheme(
                                    target_cpa_bidding_scheme = yahoo_ads_search.models.bidding_strategy_service_target_cpa_bidding_scheme.BiddingStrategyServiceTargetCpaBiddingScheme(
                                        bid_ceiling = 56,
                                        bid_floor = 56,
                                        target_cpa = 56, ),
                                    target_roas_bidding_scheme = yahoo_ads_search.models.bidding_strategy_service_target_roas_bidding_scheme.BiddingStrategyServiceTargetRoasBiddingScheme(
                                        bid_ceiling = 56,
                                        bid_floor = 56,
                                        target_roas = 1.337, ),
                                    target_spend_bidding_scheme = yahoo_ads_search.models.bidding_strategy_service_target_spend_bidding_scheme.BiddingStrategyServiceTargetSpendBiddingScheme(
                                        bid_ceiling = 56, ),
                                    type = 'TARGET_ROAS', ),
                                bidding_strategy_id = 56,
                                bidding_strategy_name = '0',
                                type = 'TARGET_ROAS', ),
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
                        ], )
            )
        else :
            return BiddingStrategyServiceMutateResponse(
        )

    def testBiddingStrategyServiceMutateResponse(self):
        """Test BiddingStrategyServiceMutateResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()

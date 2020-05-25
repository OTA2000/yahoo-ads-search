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
from yahoo_ads_search.models.feed_item_service_get_response import FeedItemServiceGetResponse  # noqa: E501
from yahoo_ads_search.rest import ApiException

class TestFeedItemServiceGetResponse(unittest.TestCase):
    """FeedItemServiceGetResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test FeedItemServiceGetResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = yahoo_ads_search.models.feed_item_service_get_response.FeedItemServiceGetResponse()  # noqa: E501
        if include_optional :
            return FeedItemServiceGetResponse(
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
                rval = yahoo_ads_search.models.feed_item_service_page.FeedItemServicePage(
                    total_num_entries = 56,
                    values = [
                        yahoo_ads_search.models.feed_item_service_value.FeedItemServiceValue(
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
                            feed_item = yahoo_ads_search.models.feed_item.FeedItem(
                                account_id = 56,
                                approval_status = 'APPROVED',
                                custom_parameters = yahoo_ads_search.models.feed_item_service_custom_parameters.FeedItemServiceCustomParameters(
                                    is_remove = 'TRUE',
                                    parameters = [
                                        yahoo_ads_search.models.feed_item_service_custom_parameter.FeedItemServiceCustomParameter(
                                            key = '0',
                                            value = '0', )
                                        ], ),
                                device_preference = 'SMART_PHONE',
                                disapproval_reason_codes = [
                                    '0'
                                    ],
                                end_date = '0',
                                feed_id = 56,
                                feed_item_attribute = [
                                    yahoo_ads_search.models.feed_item_service_attribute.FeedItemServiceAttribute(
                                        feed_attribute_id = 56,
                                        multiple_feed_item_attribute = yahoo_ads_search.models.feed_item_service_multiple_feed_item_attribute.FeedItemServiceMultipleFeedItemAttribute(
                                            feed_attribute_values = [
                                                yahoo_ads_search.models.feed_item_service_feed_attribute_value.FeedItemServiceFeedAttributeValue(
                                                    feed_attribute_value = '0',
                                                    review_feed_attribute_value = '0', )
                                                ], ),
                                        placeholder_field = 'LINK_TEXT',
                                        simple_feed_item_attribute = yahoo_ads_search.models.feed_item_service_simple_feed_item_attribute.FeedItemServiceSimpleFeedItemAttribute(
                                            feed_attribute_value = '0',
                                            review_feed_attribute_value = '0', ), )
                                    ],
                                feed_item_id = 56,
                                feed_item_track_id = 56,
                                invalided_trademarks = [
                                    '0'
                                    ],
                                location = yahoo_ads_search.models.feed_item_service_location.FeedItemServiceLocation(
                                    criterion_type_feed_item = 'LOCATION',
                                    geo_restriction = 'NONE',
                                    target_id = '0', ),
                                placeholder_type = 'QUICKLINK',
                                review_custom_parameters = yahoo_ads_search.models.feed_item_service_custom_parameters.FeedItemServiceCustomParameters(),
                                scheduling = yahoo_ads_search.models.feed_item_service_scheduling.FeedItemServiceScheduling(
                                    schedules = [
                                        yahoo_ads_search.models.feed_item_service_schedule.FeedItemServiceSchedule(
                                            day_of_week = 'MONDAY',
                                            end_hour = 56,
                                            end_minute = 'ZERO',
                                            start_hour = 56,
                                            start_minute = 'ZERO', )
                                        ], ),
                                start_date = '0',
                                targeting_ad_group = yahoo_ads_search.models.feed_item_service_targeting_ad_group.FeedItemServiceTargetingAdGroup(
                                    targeting_ad_group_id = 56, ),
                                targeting_campaign = yahoo_ads_search.models.feed_item_service_targeting_campaign.FeedItemServiceTargetingCampaign(
                                    targeting_campaign_id = 56, ),
                                targeting_keyword = yahoo_ads_search.models.feed_item_service_targeting_keyword.FeedItemServiceTargetingKeyword(
                                    keyword_match_type = 'EXACT',
                                    targeting_keyword_id = 56,
                                    text = '0', ),
                                trademark_status = 'NO_RESTRICTION', ),
                            operation_succeeded = True, )
                        ], )
            )
        else :
            return FeedItemServiceGetResponse(
        )

    def testFeedItemServiceGetResponse(self):
        """Test FeedItemServiceGetResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()

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
from yahoo_ads_search.models.audit_log_service_get_response import AuditLogServiceGetResponse  # noqa: E501
from yahoo_ads_search.rest import ApiException

class TestAuditLogServiceGetResponse(unittest.TestCase):
    """AuditLogServiceGetResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AuditLogServiceGetResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = yahoo_ads_search.models.audit_log_service_get_response.AuditLogServiceGetResponse()  # noqa: E501
        if include_optional :
            return AuditLogServiceGetResponse(
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
                rval = yahoo_ads_search.models.audit_log_service_page.AuditLogServicePage(
                    total_num_entries = 56,
                    values = [
                        yahoo_ads_search.models.audit_log_service_value.AuditLogServiceValue(
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
                            job = yahoo_ads_search.models.audit_log_service_job.AuditLogServiceJob(
                                account_id = 56,
                                date_range = yahoo_ads_search.models.audit_log_service_date_range.AuditLogServiceDateRange(
                                    end_date = '0',
                                    start_date = '0', ),
                                encoding = 'SJIS',
                                event_selector = [
                                    yahoo_ads_search.models.audit_log_service_event_selector.AuditLogServiceEventSelector(
                                        entity_type = '0',
                                        event_types = [
                                            'ADD'
                                            ], )
                                    ],
                                job_id = 56,
                                job_name = '0',
                                job_status = 'IN_PROGRESS',
                                lang = 'JA',
                                output = 'CSV',
                                source_type = 'API', ),
                            operation_succeeded = True, )
                        ], )
            )
        else :
            return AuditLogServiceGetResponse(
        )

    def testAuditLogServiceGetResponse(self):
        """Test AuditLogServiceGetResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()

# yahoo_ads_search.CampaignCriterionServiceApi

All URIs are relative to *https://ads-search.yahooapis.jp/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**campaign_criterion_service_add_post**](CampaignCriterionServiceApi.md#campaign_criterion_service_add_post) | **POST** /CampaignCriterionService/add |
[**campaign_criterion_service_get_post**](CampaignCriterionServiceApi.md#campaign_criterion_service_get_post) | **POST** /CampaignCriterionService/get |
[**campaign_criterion_service_remove_post**](CampaignCriterionServiceApi.md#campaign_criterion_service_remove_post) | **POST** /CampaignCriterionService/remove |


# **campaign_criterion_service_add_post**
> CampaignCriterionServiceMutateResponse campaign_criterion_service_add_post(campaign_criterion_service_operation=campaign_criterion_service_operation)



<div lang=\"ja\">キャンペーンの除外クライテリアを追加します。</div> <div lang=\"en\">Add negative criteria in campaign-level.</div>

### Example

* OAuth Authentication (oAuth):
```python
from __future__ import print_function
import time
import yahoo_ads_search
from yahoo_ads_search.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://ads-search.yahooapis.jp/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = yahoo_ads_search.Configuration(
    host = "https://ads-search.yahooapis.jp/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oAuth
configuration = yahoo_ads_search.Configuration(
    host = "https://ads-search.yahooapis.jp/api/v1"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with yahoo_ads_search.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = yahoo_ads_search.CampaignCriterionServiceApi(api_client)
    campaign_criterion_service_operation = yahoo_ads_search.CampaignCriterionServiceOperation() # CampaignCriterionServiceOperation |  (optional)

    try:
        api_response = api_instance.campaign_criterion_service_add_post(campaign_criterion_service_operation=campaign_criterion_service_operation)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CampaignCriterionServiceApi->campaign_criterion_service_add_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_criterion_service_operation** | [**CampaignCriterionServiceOperation**](CampaignCriterionServiceOperation.md)|  | [optional]

### Return type

[**CampaignCriterionServiceMutateResponse**](CampaignCriterionServiceMutateResponse.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**503** | &lt;details&gt; &lt;summary&gt;Error Codes&lt;/summary&gt; &lt;table border&#x3D;\&quot;1\&quot;&gt; &lt;tr&gt;&lt;th&gt;Code&lt;/th&gt;&lt;th&gt;Message&lt;/th&gt;&lt;th&gt;Description&lt;/th&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;0099&lt;/td&gt;&lt;td&gt;Out of service.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;APIがメンテナンス中、またはご利用できません。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;API is under maintenance or not available to use.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;/table&gt; &lt;/details&gt;  |  -  |
**500** | &lt;details&gt; &lt;summary&gt;Error Codes&lt;/summary&gt; &lt;table border&#x3D;\&quot;1\&quot;&gt; &lt;tr&gt;&lt;th&gt;Code&lt;/th&gt;&lt;th&gt;Message&lt;/th&gt;&lt;th&gt;Description&lt;/th&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;0002&lt;/td&gt;&lt;td&gt;An internal error has occurred.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;内部エラーが発生しました。再度操作を実行してください。 &lt;br&gt;もし、問題が解決しない場合は、お問い合わせページをご利用ください。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;An internal error has occurred. Please try again later. &lt;br&gt;If the problem continues, please contact the support team via Inquiry page for assistance. &lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;/table&gt; &lt;/details&gt;  |  -  |
**200** | &lt;details&gt; &lt;summary&gt;Error Codes&lt;/summary&gt; &lt;table border&#x3D;\&quot;1\&quot;&gt; &lt;tr&gt;&lt;th&gt;Code&lt;/th&gt;&lt;th&gt;Message&lt;/th&gt;&lt;th&gt;Description&lt;/th&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;0001&lt;/td&gt;&lt;td&gt;Invalid Request.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;さまざまな要因が考えられます。&lt;br&gt;主な要因は、パラメータの値が不正か、誤りがあるためにオペレーションが完了できません。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;This error can result for a variety of reasons. &lt;br&gt;Typically because one of the parameter values in the request is wrong or invalid and the operation cannot be completed.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;R0001&lt;/td&gt;&lt;td&gt;Require.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;必須です。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;It is missing required parameter.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;F0001&lt;/td&gt;&lt;td&gt;Invalid format.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;値の形式が不正です。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The value format is invalid.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;V0001&lt;/td&gt;&lt;td&gt;Invalid value.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;値が無効です。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The value is invalid.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;S0001&lt;/td&gt;&lt;td&gt;Invalid Status.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;ステータスが無効です。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The status is invalid.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;L0002&lt;/td&gt;&lt;td&gt;Over list size.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;配列の要素数が上限値を超過しています。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The number of elements in the array exceeds the upper limit.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;L0001&lt;/td&gt;&lt;td&gt;Lower list size.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;配列の要素数が下限値を下回っています。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The number of elements in the array is below the lower limit.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;D0001&lt;/td&gt;&lt;td&gt;Duplicate.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;一意な値が重複しています。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The unique value is duplicated.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;RL001&lt;/td&gt;&lt;td&gt;Invalid relation.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;リクエストの関連性が矛盾しています。&lt;br&gt; たとえば、開始＞終了の日付指定を行なっているなど&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The relation of the request is contradictory.&lt;br&gt; For example, you are specifying the date of start &gt; end.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;LT001&lt;/td&gt;&lt;td&gt;Over limit.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;登録できる上限値を超過しています。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The upper limit value that can be registered is exceeded.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;I0001&lt;/td&gt;&lt;td&gt;Deactivated Id.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;IDが無効です。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The ID is Deactivated.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;210110&lt;/td&gt;&lt;td&gt;Invalid target&lt;/td&gt;&lt;td&gt;１日のスケジュール指定が上限値（6件）を超えています。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The daily schedule specification exceeds the upper limit (6 cases).&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;210517&lt;/td&gt;&lt;td&gt;Exceeds maximum word limit.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;キーワードは最大10個までしか指定できません。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;10 keywords can only be specified up to.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;210510&lt;/td&gt;&lt;td&gt;Exists same text with match type.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;指定されたキーワード、マッチタイプはすでにキャンペーン/広告グループ内に存在します。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The specified keyword, match type already exists in the campaign / ad group.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;/table&gt; &lt;/details&gt;  |  -  |
**403** | &lt;details&gt; &lt;summary&gt;Error Codes&lt;/summary&gt; &lt;table border&#x3D;\&quot;1\&quot;&gt; &lt;tr&gt;&lt;th&gt;Code&lt;/th&gt;&lt;th&gt;Message&lt;/th&gt;&lt;th&gt;Description&lt;/th&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;0098&lt;/td&gt;&lt;td&gt;Permission denied.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;権限がありません。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;Permission denied.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;0003&lt;/td&gt;&lt;td&gt;Frequency limit exceeded. Please try your request again later&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;アクセス頻度が上限値に達しました。時間をおいて再度実行してください。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;Frequency limit exceeded. Please try your request again later.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;/table&gt; &lt;/details&gt;  |  -  |
**401** | &lt;details&gt; &lt;summary&gt;Error Codes&lt;/summary&gt; &lt;table border&#x3D;\&quot;1\&quot;&gt; &lt;tr&gt;&lt;th&gt;Code&lt;/th&gt;&lt;th&gt;Message&lt;/th&gt;&lt;th&gt;Description&lt;/th&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;0110&lt;/td&gt;&lt;td&gt;Require access token.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;アクセストークンがリクエストヘッダに存在していません。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;There is no access token in the request header.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;0111&lt;/td&gt;&lt;td&gt;Authentication failed.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;アクセストークンの認証に失敗しました。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The access token authentication failed.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;0112&lt;/td&gt;&lt;td&gt;Account not found.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;アカウントが見つかりませんでした。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The account can not found.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;0113&lt;/td&gt;&lt;td&gt;Deactivated account.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;アカウントが無効です。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The account is deactivated.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;/table&gt; &lt;/details&gt;  |  -  |
**400** | &lt;details&gt; &lt;summary&gt;Error Codes&lt;/summary&gt; &lt;table border&#x3D;\&quot;1\&quot;&gt; &lt;tr&gt;&lt;th&gt;Code&lt;/th&gt;&lt;th&gt;Message&lt;/th&gt;&lt;th&gt;Description&lt;/th&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;0114&lt;/td&gt;&lt;td&gt;Invalid scope.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;アクセストークンが無効です。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The access token is invalid.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;/table&gt; &lt;/details&gt;  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **campaign_criterion_service_get_post**
> CampaignCriterionServiceGetResponse campaign_criterion_service_get_post(campaign_criterion_service_selector=campaign_criterion_service_selector)



<div lang=\"ja\">キャンペーンの除外クライテリアに関する情報を取得します。</div> <div lang=\"en\">Gets negative criteria in campaign-level.</div>

### Example

* OAuth Authentication (oAuth):
```python
from __future__ import print_function
import time
import yahoo_ads_search
from yahoo_ads_search.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://ads-search.yahooapis.jp/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = yahoo_ads_search.Configuration(
    host = "https://ads-search.yahooapis.jp/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oAuth
configuration = yahoo_ads_search.Configuration(
    host = "https://ads-search.yahooapis.jp/api/v1"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with yahoo_ads_search.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = yahoo_ads_search.CampaignCriterionServiceApi(api_client)
    campaign_criterion_service_selector = yahoo_ads_search.CampaignCriterionServiceSelector() # CampaignCriterionServiceSelector |  (optional)

    try:
        api_response = api_instance.campaign_criterion_service_get_post(campaign_criterion_service_selector=campaign_criterion_service_selector)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CampaignCriterionServiceApi->campaign_criterion_service_get_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_criterion_service_selector** | [**CampaignCriterionServiceSelector**](CampaignCriterionServiceSelector.md)|  | [optional]

### Return type

[**CampaignCriterionServiceGetResponse**](CampaignCriterionServiceGetResponse.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**503** | &lt;details&gt; &lt;summary&gt;Error Codes&lt;/summary&gt; &lt;table border&#x3D;\&quot;1\&quot;&gt; &lt;tr&gt;&lt;th&gt;Code&lt;/th&gt;&lt;th&gt;Message&lt;/th&gt;&lt;th&gt;Description&lt;/th&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;0099&lt;/td&gt;&lt;td&gt;Out of service.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;APIがメンテナンス中、またはご利用できません。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;API is under maintenance or not available to use.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;/table&gt; &lt;/details&gt;  |  -  |
**500** | &lt;details&gt; &lt;summary&gt;Error Codes&lt;/summary&gt; &lt;table border&#x3D;\&quot;1\&quot;&gt; &lt;tr&gt;&lt;th&gt;Code&lt;/th&gt;&lt;th&gt;Message&lt;/th&gt;&lt;th&gt;Description&lt;/th&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;0002&lt;/td&gt;&lt;td&gt;An internal error has occurred.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;内部エラーが発生しました。再度操作を実行してください。 &lt;br&gt;もし、問題が解決しない場合は、お問い合わせページをご利用ください。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;An internal error has occurred. Please try again later. &lt;br&gt;If the problem continues, please contact the support team via Inquiry page for assistance. &lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;/table&gt; &lt;/details&gt;  |  -  |
**200** | &lt;details&gt; &lt;summary&gt;Error Codes&lt;/summary&gt; &lt;table border&#x3D;\&quot;1\&quot;&gt; &lt;tr&gt;&lt;th&gt;Code&lt;/th&gt;&lt;th&gt;Message&lt;/th&gt;&lt;th&gt;Description&lt;/th&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;0001&lt;/td&gt;&lt;td&gt;Invalid Request.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;さまざまな要因が考えられます。&lt;br&gt;主な要因は、パラメータの値が不正か、誤りがあるためにオペレーションが完了できません。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;This error can result for a variety of reasons. &lt;br&gt;Typically because one of the parameter values in the request is wrong or invalid and the operation cannot be completed.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;R0001&lt;/td&gt;&lt;td&gt;Require.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;必須です。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;It is missing required parameter.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;F0001&lt;/td&gt;&lt;td&gt;Invalid format.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;値の形式が不正です。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The value format is invalid.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;V0001&lt;/td&gt;&lt;td&gt;Invalid value.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;値が無効です。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The value is invalid.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;S0001&lt;/td&gt;&lt;td&gt;Invalid Status.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;ステータスが無効です。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The status is invalid.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;L0002&lt;/td&gt;&lt;td&gt;Over list size.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;配列の要素数が上限値を超過しています。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The number of elements in the array exceeds the upper limit.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;L0001&lt;/td&gt;&lt;td&gt;Lower list size.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;配列の要素数が下限値を下回っています。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The number of elements in the array is below the lower limit.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;D0001&lt;/td&gt;&lt;td&gt;Duplicate.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;一意な値が重複しています。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The unique value is duplicated.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;RL001&lt;/td&gt;&lt;td&gt;Invalid relation.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;リクエストの関連性が矛盾しています。&lt;br&gt; たとえば、開始＞終了の日付指定を行なっているなど&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The relation of the request is contradictory.&lt;br&gt; For example, you are specifying the date of start &gt; end.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;LT001&lt;/td&gt;&lt;td&gt;Over limit.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;登録できる上限値を超過しています。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The upper limit value that can be registered is exceeded.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;I0001&lt;/td&gt;&lt;td&gt;Deactivated Id.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;IDが無効です。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The ID is Deactivated.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;210110&lt;/td&gt;&lt;td&gt;Invalid target&lt;/td&gt;&lt;td&gt;１日のスケジュール指定が上限値（6件）を超えています。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The daily schedule specification exceeds the upper limit (6 cases).&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;210517&lt;/td&gt;&lt;td&gt;Exceeds maximum word limit.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;キーワードは最大10個までしか指定できません。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;10 keywords can only be specified up to.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;210510&lt;/td&gt;&lt;td&gt;Exists same text with match type.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;指定されたキーワード、マッチタイプはすでにキャンペーン/広告グループ内に存在します。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The specified keyword, match type already exists in the campaign / ad group.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;/table&gt; &lt;/details&gt;  |  -  |
**403** | &lt;details&gt; &lt;summary&gt;Error Codes&lt;/summary&gt; &lt;table border&#x3D;\&quot;1\&quot;&gt; &lt;tr&gt;&lt;th&gt;Code&lt;/th&gt;&lt;th&gt;Message&lt;/th&gt;&lt;th&gt;Description&lt;/th&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;0098&lt;/td&gt;&lt;td&gt;Permission denied.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;権限がありません。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;Permission denied.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;0003&lt;/td&gt;&lt;td&gt;Frequency limit exceeded. Please try your request again later&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;アクセス頻度が上限値に達しました。時間をおいて再度実行してください。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;Frequency limit exceeded. Please try your request again later.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;/table&gt; &lt;/details&gt;  |  -  |
**401** | &lt;details&gt; &lt;summary&gt;Error Codes&lt;/summary&gt; &lt;table border&#x3D;\&quot;1\&quot;&gt; &lt;tr&gt;&lt;th&gt;Code&lt;/th&gt;&lt;th&gt;Message&lt;/th&gt;&lt;th&gt;Description&lt;/th&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;0110&lt;/td&gt;&lt;td&gt;Require access token.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;アクセストークンがリクエストヘッダに存在していません。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;There is no access token in the request header.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;0111&lt;/td&gt;&lt;td&gt;Authentication failed.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;アクセストークンの認証に失敗しました。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The access token authentication failed.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;0112&lt;/td&gt;&lt;td&gt;Account not found.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;アカウントが見つかりませんでした。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The account can not found.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;0113&lt;/td&gt;&lt;td&gt;Deactivated account.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;アカウントが無効です。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The account is deactivated.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;/table&gt; &lt;/details&gt;  |  -  |
**400** | &lt;details&gt; &lt;summary&gt;Error Codes&lt;/summary&gt; &lt;table border&#x3D;\&quot;1\&quot;&gt; &lt;tr&gt;&lt;th&gt;Code&lt;/th&gt;&lt;th&gt;Message&lt;/th&gt;&lt;th&gt;Description&lt;/th&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;0114&lt;/td&gt;&lt;td&gt;Invalid scope.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;アクセストークンが無効です。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The access token is invalid.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;/table&gt; &lt;/details&gt;  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **campaign_criterion_service_remove_post**
> CampaignCriterionServiceMutateResponse campaign_criterion_service_remove_post(campaign_criterion_service_operation=campaign_criterion_service_operation)



<div lang=\"ja\">キャンペーンの除外クライテリアを削除します。</div> <div lang=\"en\">Removed negative criteria in campaign-level.</div>

### Example

* OAuth Authentication (oAuth):
```python
from __future__ import print_function
import time
import yahoo_ads_search
from yahoo_ads_search.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://ads-search.yahooapis.jp/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = yahoo_ads_search.Configuration(
    host = "https://ads-search.yahooapis.jp/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oAuth
configuration = yahoo_ads_search.Configuration(
    host = "https://ads-search.yahooapis.jp/api/v1"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with yahoo_ads_search.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = yahoo_ads_search.CampaignCriterionServiceApi(api_client)
    campaign_criterion_service_operation = yahoo_ads_search.CampaignCriterionServiceOperation() # CampaignCriterionServiceOperation |  (optional)

    try:
        api_response = api_instance.campaign_criterion_service_remove_post(campaign_criterion_service_operation=campaign_criterion_service_operation)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CampaignCriterionServiceApi->campaign_criterion_service_remove_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_criterion_service_operation** | [**CampaignCriterionServiceOperation**](CampaignCriterionServiceOperation.md)|  | [optional]

### Return type

[**CampaignCriterionServiceMutateResponse**](CampaignCriterionServiceMutateResponse.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**503** | &lt;details&gt; &lt;summary&gt;Error Codes&lt;/summary&gt; &lt;table border&#x3D;\&quot;1\&quot;&gt; &lt;tr&gt;&lt;th&gt;Code&lt;/th&gt;&lt;th&gt;Message&lt;/th&gt;&lt;th&gt;Description&lt;/th&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;0099&lt;/td&gt;&lt;td&gt;Out of service.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;APIがメンテナンス中、またはご利用できません。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;API is under maintenance or not available to use.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;/table&gt; &lt;/details&gt;  |  -  |
**500** | &lt;details&gt; &lt;summary&gt;Error Codes&lt;/summary&gt; &lt;table border&#x3D;\&quot;1\&quot;&gt; &lt;tr&gt;&lt;th&gt;Code&lt;/th&gt;&lt;th&gt;Message&lt;/th&gt;&lt;th&gt;Description&lt;/th&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;0002&lt;/td&gt;&lt;td&gt;An internal error has occurred.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;内部エラーが発生しました。再度操作を実行してください。 &lt;br&gt;もし、問題が解決しない場合は、お問い合わせページをご利用ください。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;An internal error has occurred. Please try again later. &lt;br&gt;If the problem continues, please contact the support team via Inquiry page for assistance. &lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;/table&gt; &lt;/details&gt;  |  -  |
**200** | &lt;details&gt; &lt;summary&gt;Error Codes&lt;/summary&gt; &lt;table border&#x3D;\&quot;1\&quot;&gt; &lt;tr&gt;&lt;th&gt;Code&lt;/th&gt;&lt;th&gt;Message&lt;/th&gt;&lt;th&gt;Description&lt;/th&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;0001&lt;/td&gt;&lt;td&gt;Invalid Request.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;さまざまな要因が考えられます。&lt;br&gt;主な要因は、パラメータの値が不正か、誤りがあるためにオペレーションが完了できません。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;This error can result for a variety of reasons. &lt;br&gt;Typically because one of the parameter values in the request is wrong or invalid and the operation cannot be completed.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;R0001&lt;/td&gt;&lt;td&gt;Require.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;必須です。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;It is missing required parameter.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;F0001&lt;/td&gt;&lt;td&gt;Invalid format.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;値の形式が不正です。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The value format is invalid.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;V0001&lt;/td&gt;&lt;td&gt;Invalid value.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;値が無効です。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The value is invalid.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;S0001&lt;/td&gt;&lt;td&gt;Invalid Status.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;ステータスが無効です。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The status is invalid.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;L0002&lt;/td&gt;&lt;td&gt;Over list size.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;配列の要素数が上限値を超過しています。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The number of elements in the array exceeds the upper limit.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;L0001&lt;/td&gt;&lt;td&gt;Lower list size.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;配列の要素数が下限値を下回っています。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The number of elements in the array is below the lower limit.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;D0001&lt;/td&gt;&lt;td&gt;Duplicate.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;一意な値が重複しています。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The unique value is duplicated.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;RL001&lt;/td&gt;&lt;td&gt;Invalid relation.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;リクエストの関連性が矛盾しています。&lt;br&gt; たとえば、開始＞終了の日付指定を行なっているなど&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The relation of the request is contradictory.&lt;br&gt; For example, you are specifying the date of start &gt; end.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;LT001&lt;/td&gt;&lt;td&gt;Over limit.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;登録できる上限値を超過しています。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The upper limit value that can be registered is exceeded.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;I0001&lt;/td&gt;&lt;td&gt;Deactivated Id.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;IDが無効です。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The ID is Deactivated.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;210110&lt;/td&gt;&lt;td&gt;Invalid target&lt;/td&gt;&lt;td&gt;１日のスケジュール指定が上限値（6件）を超えています。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The daily schedule specification exceeds the upper limit (6 cases).&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;210517&lt;/td&gt;&lt;td&gt;Exceeds maximum word limit.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;キーワードは最大10個までしか指定できません。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;10 keywords can only be specified up to.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;210510&lt;/td&gt;&lt;td&gt;Exists same text with match type.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;指定されたキーワード、マッチタイプはすでにキャンペーン/広告グループ内に存在します。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The specified keyword, match type already exists in the campaign / ad group.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;/table&gt; &lt;/details&gt;  |  -  |
**403** | &lt;details&gt; &lt;summary&gt;Error Codes&lt;/summary&gt; &lt;table border&#x3D;\&quot;1\&quot;&gt; &lt;tr&gt;&lt;th&gt;Code&lt;/th&gt;&lt;th&gt;Message&lt;/th&gt;&lt;th&gt;Description&lt;/th&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;0098&lt;/td&gt;&lt;td&gt;Permission denied.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;権限がありません。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;Permission denied.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;0003&lt;/td&gt;&lt;td&gt;Frequency limit exceeded. Please try your request again later&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;アクセス頻度が上限値に達しました。時間をおいて再度実行してください。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;Frequency limit exceeded. Please try your request again later.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;/table&gt; &lt;/details&gt;  |  -  |
**401** | &lt;details&gt; &lt;summary&gt;Error Codes&lt;/summary&gt; &lt;table border&#x3D;\&quot;1\&quot;&gt; &lt;tr&gt;&lt;th&gt;Code&lt;/th&gt;&lt;th&gt;Message&lt;/th&gt;&lt;th&gt;Description&lt;/th&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;0110&lt;/td&gt;&lt;td&gt;Require access token.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;アクセストークンがリクエストヘッダに存在していません。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;There is no access token in the request header.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;0111&lt;/td&gt;&lt;td&gt;Authentication failed.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;アクセストークンの認証に失敗しました。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The access token authentication failed.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;0112&lt;/td&gt;&lt;td&gt;Account not found.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;アカウントが見つかりませんでした。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The account can not found.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;0113&lt;/td&gt;&lt;td&gt;Deactivated account.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;アカウントが無効です。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The account is deactivated.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;/table&gt; &lt;/details&gt;  |  -  |
**400** | &lt;details&gt; &lt;summary&gt;Error Codes&lt;/summary&gt; &lt;table border&#x3D;\&quot;1\&quot;&gt; &lt;tr&gt;&lt;th&gt;Code&lt;/th&gt;&lt;th&gt;Message&lt;/th&gt;&lt;th&gt;Description&lt;/th&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;0114&lt;/td&gt;&lt;td&gt;Invalid scope.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;アクセストークンが無効です。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The access token is invalid.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;/table&gt; &lt;/details&gt;  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


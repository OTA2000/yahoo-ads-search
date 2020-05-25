# yahoo_ads_search.AdGroupServiceApi

All URIs are relative to *https://ads-search.yahooapis.jp/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ad_group_service_add_post**](AdGroupServiceApi.md#ad_group_service_add_post) | **POST** /AdGroupService/add |
[**ad_group_service_get_post**](AdGroupServiceApi.md#ad_group_service_get_post) | **POST** /AdGroupService/get |
[**ad_group_service_remove_post**](AdGroupServiceApi.md#ad_group_service_remove_post) | **POST** /AdGroupService/remove |
[**ad_group_service_set_post**](AdGroupServiceApi.md#ad_group_service_set_post) | **POST** /AdGroupService/set |


# **ad_group_service_add_post**
> AdGroupServiceMutateResponse ad_group_service_add_post(ad_group_service_operation=ad_group_service_operation)



<div lang=\"ja\">広告グループを追加します。</div> <div lang=\"en\">Create Ad group information.</div>

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
    api_instance = yahoo_ads_search.AdGroupServiceApi(api_client)
    ad_group_service_operation = yahoo_ads_search.AdGroupServiceOperation() # AdGroupServiceOperation |  (optional)

    try:
        api_response = api_instance.ad_group_service_add_post(ad_group_service_operation=ad_group_service_operation)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AdGroupServiceApi->ad_group_service_add_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ad_group_service_operation** | [**AdGroupServiceOperation**](AdGroupServiceOperation.md)|  | [optional]

### Return type

[**AdGroupServiceMutateResponse**](AdGroupServiceMutateResponse.md)

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
**200** | &lt;details&gt; &lt;summary&gt;Error Codes&lt;/summary&gt; &lt;table border&#x3D;\&quot;1\&quot;&gt; &lt;tr&gt;&lt;th&gt;Code&lt;/th&gt;&lt;th&gt;Message&lt;/th&gt;&lt;th&gt;Description&lt;/th&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;0001&lt;/td&gt;&lt;td&gt;Invalid Request.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;さまざまな要因が考えられます。&lt;br&gt;主な要因は、パラメータの値が不正か、誤りがあるためにオペレーションが完了できません。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;This error can result for a variety of reasons. &lt;br&gt;Typically because one of the parameter values in the request is wrong or invalid and the operation cannot be completed.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;R0001&lt;/td&gt;&lt;td&gt;Require.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;必須です。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;It is missing required parameter.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;F0001&lt;/td&gt;&lt;td&gt;Invalid format.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;値の形式が不正です。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The value format is invalid.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;V0001&lt;/td&gt;&lt;td&gt;Invalid value.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;値が無効です。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The value is invalid.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;S0001&lt;/td&gt;&lt;td&gt;Invalid Status.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;ステータスが無効です。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The status is invalid.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;L0002&lt;/td&gt;&lt;td&gt;Over list size.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;配列の要素数が上限値を超過しています。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The number of elements in the array exceeds the upper limit.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;L0001&lt;/td&gt;&lt;td&gt;Lower list size.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;配列の要素数が下限値を下回っています。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The number of elements in the array is below the lower limit.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;D0001&lt;/td&gt;&lt;td&gt;Duplicate.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;一意な値が重複しています。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The unique value is duplicated.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;RL001&lt;/td&gt;&lt;td&gt;Invalid relation.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;リクエストの関連性が矛盾しています。&lt;br&gt; たとえば、開始＞終了の日付指定を行なっているなど&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The relation of the request is contradictory.&lt;br&gt; For example, you are specifying the date of start &gt; end.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;LT001&lt;/td&gt;&lt;td&gt;Over limit.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;登録できる上限値を超過しています。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The upper limit value that can be registered is exceeded.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;I0001&lt;/td&gt;&lt;td&gt;Deactivated Id.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;IDが無効です。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The ID is Deactivated.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;210405&lt;/td&gt;&lt;td&gt;Budget has exceeded.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;予算額を超過しています。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The budget amount is exceeded.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;210303&lt;/td&gt;&lt;td&gt;Invalid conversion tracking.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;コンバージョントラッキングが無効です。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;Conversion tracking is Invalid.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;210301&lt;/td&gt;&lt;td&gt;Setting the disabled Auto bidding.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;編集中（削除含む）の自動入札を指定しています。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;Auto bidding in editing (including deletion) is specified.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;210304&lt;/td&gt;&lt;td&gt;Not enough conversions or invalid setting.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;コンバージョン数が不十分です。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;Conversions is not enough.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;210305&lt;/td&gt;&lt;td&gt;Auto bidding is already set.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;キーワードに個別の入札価格や入札設定が指定されている状態で、キャンペーンに「コンバージョン数の最大化」、または「コンバージョン単価の目標値」の自動入札を設定しております。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;Auto bidding of \&quot;Enhanced CPC\&quot; or \&quot;Target conversion spend\&quot; is set for campaigns with individual bidding prices and bidding settings specified for keywords.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;210306&lt;/td&gt;&lt;td&gt;Cannot use conversion optimizer.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;コンバージョンオプティマイザーが利用できません。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;Conversion optimizer cannot be used.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;210308&lt;/td&gt;&lt;td&gt;Set campaign active.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;キャンペーンがACTIVEでないため、入札設定が利用できません。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;Since the campaign is not ACTIVE, the bidding settings can not be used.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;210309&lt;/td&gt;&lt;td&gt;Set campaign to Manual CPC.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;キャンペーンが「MANUAL_CPC」でないため、入札設定が利用できません。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;Since the campaign is not \&quot;Manual CPC\&quot;, bidding settings can not be used.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;210409&lt;/td&gt;&lt;td&gt;AdGroupServiceBid setting limit has exceed.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;キャンペーン配下の広告広告グループに設定した入札金額または自動入札設定数が上限を超えています。&lt;br&gt;※1キャンペーンに設定できる入札金額および自動入札設定は、配下の広告グループ合計で1000件までです。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The bid amount or Auto bidding number set for the ad / ad group under the campaign exceeds the maximum limit. &lt;br&gt; * 1 The maximum bid amount and Auto bidding setting that can be set for the campaign is 1000 in total for the ad group below.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;211000&lt;/td&gt;&lt;td&gt;Cannot operate AdvancedURL.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;アドバンスドURLに移行済みのため、操作できません。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;Since it has already been transferred to AdvancedURL, it can not be operated.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;211001&lt;/td&gt;&lt;td&gt;Cannot set AdvancedMobileURL.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;アプリダウンロードキャンペーンでは、advancedMobileUrlの設定はできません。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;In the app download campaign, AdvancedMobileURL can not be set.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;211003&lt;/td&gt;&lt;td&gt;Domain does not match with DisplayURL.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;表示URLと最終リンク先URLのドメインが一致していません。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;Domain of DisplayURL and AdvancedUrl do not match.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;211004&lt;/td&gt;&lt;td&gt;Cannot set under AndroidCampaign.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;Androidのアプリキャンペーンでは、以下の設定ができません：&lt;br&gt;・キャンペーン、広告グループ、広告、キーワードにTrackingUrlや CustomParameterを設定&lt;br&gt;・キーワードに最終リンク先URLやスマートフォン向けURLを設定&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;In the Android app campaign, the following settings can not be made：&lt;br&gt;・Set TrackingUrl and CustomParameter for campaigns, ad groups, ads, keywords&lt;br&gt;・Set the AdvancedUrl and AdvancedMobileUrl for the keywords&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;/table&gt; &lt;/details&gt;  |  -  |
**403** | &lt;details&gt; &lt;summary&gt;Error Codes&lt;/summary&gt; &lt;table border&#x3D;\&quot;1\&quot;&gt; &lt;tr&gt;&lt;th&gt;Code&lt;/th&gt;&lt;th&gt;Message&lt;/th&gt;&lt;th&gt;Description&lt;/th&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;0098&lt;/td&gt;&lt;td&gt;Permission denied.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;権限がありません。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;Permission denied.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;0003&lt;/td&gt;&lt;td&gt;Frequency limit exceeded. Please try your request again later&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;アクセス頻度が上限値に達しました。時間をおいて再度実行してください。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;Frequency limit exceeded. Please try your request again later.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;/table&gt; &lt;/details&gt;  |  -  |
**401** | &lt;details&gt; &lt;summary&gt;Error Codes&lt;/summary&gt; &lt;table border&#x3D;\&quot;1\&quot;&gt; &lt;tr&gt;&lt;th&gt;Code&lt;/th&gt;&lt;th&gt;Message&lt;/th&gt;&lt;th&gt;Description&lt;/th&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;0110&lt;/td&gt;&lt;td&gt;Require access token.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;アクセストークンがリクエストヘッダに存在していません。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;There is no access token in the request header.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;0111&lt;/td&gt;&lt;td&gt;Authentication failed.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;アクセストークンの認証に失敗しました。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The access token authentication failed.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;0112&lt;/td&gt;&lt;td&gt;Account not found.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;アカウントが見つかりませんでした。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The account can not found.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;0113&lt;/td&gt;&lt;td&gt;Deactivated account.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;アカウントが無効です。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The account is deactivated.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;/table&gt; &lt;/details&gt;  |  -  |
**400** | &lt;details&gt; &lt;summary&gt;Error Codes&lt;/summary&gt; &lt;table border&#x3D;\&quot;1\&quot;&gt; &lt;tr&gt;&lt;th&gt;Code&lt;/th&gt;&lt;th&gt;Message&lt;/th&gt;&lt;th&gt;Description&lt;/th&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;0114&lt;/td&gt;&lt;td&gt;Invalid scope.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;アクセストークンが無効です。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The access token is invalid.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;/table&gt; &lt;/details&gt;  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ad_group_service_get_post**
> AdGroupServiceGetResponse ad_group_service_get_post(ad_group_service_selector=ad_group_service_selector)



<div lang=\"ja\">広告グループに関する情報を取得します。</div> <div lang=\"en\">Gets Ad group information.</div>

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
    api_instance = yahoo_ads_search.AdGroupServiceApi(api_client)
    ad_group_service_selector = yahoo_ads_search.AdGroupServiceSelector() # AdGroupServiceSelector |  (optional)

    try:
        api_response = api_instance.ad_group_service_get_post(ad_group_service_selector=ad_group_service_selector)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AdGroupServiceApi->ad_group_service_get_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ad_group_service_selector** | [**AdGroupServiceSelector**](AdGroupServiceSelector.md)|  | [optional]

### Return type

[**AdGroupServiceGetResponse**](AdGroupServiceGetResponse.md)

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
**200** | &lt;details&gt; &lt;summary&gt;Error Codes&lt;/summary&gt; &lt;table border&#x3D;\&quot;1\&quot;&gt; &lt;tr&gt;&lt;th&gt;Code&lt;/th&gt;&lt;th&gt;Message&lt;/th&gt;&lt;th&gt;Description&lt;/th&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;0001&lt;/td&gt;&lt;td&gt;Invalid Request.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;さまざまな要因が考えられます。&lt;br&gt;主な要因は、パラメータの値が不正か、誤りがあるためにオペレーションが完了できません。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;This error can result for a variety of reasons. &lt;br&gt;Typically because one of the parameter values in the request is wrong or invalid and the operation cannot be completed.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;R0001&lt;/td&gt;&lt;td&gt;Require.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;必須です。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;It is missing required parameter.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;F0001&lt;/td&gt;&lt;td&gt;Invalid format.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;値の形式が不正です。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The value format is invalid.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;V0001&lt;/td&gt;&lt;td&gt;Invalid value.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;値が無効です。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The value is invalid.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;S0001&lt;/td&gt;&lt;td&gt;Invalid Status.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;ステータスが無効です。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The status is invalid.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;L0002&lt;/td&gt;&lt;td&gt;Over list size.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;配列の要素数が上限値を超過しています。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The number of elements in the array exceeds the upper limit.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;L0001&lt;/td&gt;&lt;td&gt;Lower list size.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;配列の要素数が下限値を下回っています。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The number of elements in the array is below the lower limit.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;D0001&lt;/td&gt;&lt;td&gt;Duplicate.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;一意な値が重複しています。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The unique value is duplicated.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;RL001&lt;/td&gt;&lt;td&gt;Invalid relation.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;リクエストの関連性が矛盾しています。&lt;br&gt; たとえば、開始＞終了の日付指定を行なっているなど&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The relation of the request is contradictory.&lt;br&gt; For example, you are specifying the date of start &gt; end.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;LT001&lt;/td&gt;&lt;td&gt;Over limit.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;登録できる上限値を超過しています。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The upper limit value that can be registered is exceeded.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;I0001&lt;/td&gt;&lt;td&gt;Deactivated Id.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;IDが無効です。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The ID is Deactivated.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;210405&lt;/td&gt;&lt;td&gt;Budget has exceeded.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;予算額を超過しています。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The budget amount is exceeded.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;210303&lt;/td&gt;&lt;td&gt;Invalid conversion tracking.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;コンバージョントラッキングが無効です。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;Conversion tracking is Invalid.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;210301&lt;/td&gt;&lt;td&gt;Setting the disabled Auto bidding.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;編集中（削除含む）の自動入札を指定しています。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;Auto bidding in editing (including deletion) is specified.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;210304&lt;/td&gt;&lt;td&gt;Not enough conversions or invalid setting.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;コンバージョン数が不十分です。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;Conversions is not enough.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;210305&lt;/td&gt;&lt;td&gt;Auto bidding is already set.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;キーワードに個別の入札価格や入札設定が指定されている状態で、キャンペーンに「コンバージョン数の最大化」、または「コンバージョン単価の目標値」の自動入札を設定しております。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;Auto bidding of \&quot;Enhanced CPC\&quot; or \&quot;Target conversion spend\&quot; is set for campaigns with individual bidding prices and bidding settings specified for keywords.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;210306&lt;/td&gt;&lt;td&gt;Cannot use conversion optimizer.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;コンバージョンオプティマイザーが利用できません。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;Conversion optimizer cannot be used.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;210308&lt;/td&gt;&lt;td&gt;Set campaign active.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;キャンペーンがACTIVEでないため、入札設定が利用できません。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;Since the campaign is not ACTIVE, the bidding settings can not be used.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;210309&lt;/td&gt;&lt;td&gt;Set campaign to Manual CPC.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;キャンペーンが「MANUAL_CPC」でないため、入札設定が利用できません。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;Since the campaign is not \&quot;Manual CPC\&quot;, bidding settings can not be used.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;210409&lt;/td&gt;&lt;td&gt;AdGroupServiceBid setting limit has exceed.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;キャンペーン配下の広告広告グループに設定した入札金額または自動入札設定数が上限を超えています。&lt;br&gt;※1キャンペーンに設定できる入札金額および自動入札設定は、配下の広告グループ合計で1000件までです。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The bid amount or Auto bidding number set for the ad / ad group under the campaign exceeds the maximum limit. &lt;br&gt; * 1 The maximum bid amount and Auto bidding setting that can be set for the campaign is 1000 in total for the ad group below.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;211000&lt;/td&gt;&lt;td&gt;Cannot operate AdvancedURL.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;アドバンスドURLに移行済みのため、操作できません。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;Since it has already been transferred to AdvancedURL, it can not be operated.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;211001&lt;/td&gt;&lt;td&gt;Cannot set AdvancedMobileURL.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;アプリダウンロードキャンペーンでは、advancedMobileUrlの設定はできません。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;In the app download campaign, AdvancedMobileURL can not be set.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;211003&lt;/td&gt;&lt;td&gt;Domain does not match with DisplayURL.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;表示URLと最終リンク先URLのドメインが一致していません。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;Domain of DisplayURL and AdvancedUrl do not match.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;211004&lt;/td&gt;&lt;td&gt;Cannot set under AndroidCampaign.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;Androidのアプリキャンペーンでは、以下の設定ができません：&lt;br&gt;・キャンペーン、広告グループ、広告、キーワードにTrackingUrlや CustomParameterを設定&lt;br&gt;・キーワードに最終リンク先URLやスマートフォン向けURLを設定&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;In the Android app campaign, the following settings can not be made：&lt;br&gt;・Set TrackingUrl and CustomParameter for campaigns, ad groups, ads, keywords&lt;br&gt;・Set the AdvancedUrl and AdvancedMobileUrl for the keywords&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;/table&gt; &lt;/details&gt;  |  -  |
**403** | &lt;details&gt; &lt;summary&gt;Error Codes&lt;/summary&gt; &lt;table border&#x3D;\&quot;1\&quot;&gt; &lt;tr&gt;&lt;th&gt;Code&lt;/th&gt;&lt;th&gt;Message&lt;/th&gt;&lt;th&gt;Description&lt;/th&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;0098&lt;/td&gt;&lt;td&gt;Permission denied.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;権限がありません。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;Permission denied.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;0003&lt;/td&gt;&lt;td&gt;Frequency limit exceeded. Please try your request again later&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;アクセス頻度が上限値に達しました。時間をおいて再度実行してください。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;Frequency limit exceeded. Please try your request again later.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;/table&gt; &lt;/details&gt;  |  -  |
**401** | &lt;details&gt; &lt;summary&gt;Error Codes&lt;/summary&gt; &lt;table border&#x3D;\&quot;1\&quot;&gt; &lt;tr&gt;&lt;th&gt;Code&lt;/th&gt;&lt;th&gt;Message&lt;/th&gt;&lt;th&gt;Description&lt;/th&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;0110&lt;/td&gt;&lt;td&gt;Require access token.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;アクセストークンがリクエストヘッダに存在していません。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;There is no access token in the request header.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;0111&lt;/td&gt;&lt;td&gt;Authentication failed.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;アクセストークンの認証に失敗しました。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The access token authentication failed.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;0112&lt;/td&gt;&lt;td&gt;Account not found.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;アカウントが見つかりませんでした。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The account can not found.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;0113&lt;/td&gt;&lt;td&gt;Deactivated account.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;アカウントが無効です。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The account is deactivated.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;/table&gt; &lt;/details&gt;  |  -  |
**400** | &lt;details&gt; &lt;summary&gt;Error Codes&lt;/summary&gt; &lt;table border&#x3D;\&quot;1\&quot;&gt; &lt;tr&gt;&lt;th&gt;Code&lt;/th&gt;&lt;th&gt;Message&lt;/th&gt;&lt;th&gt;Description&lt;/th&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;0114&lt;/td&gt;&lt;td&gt;Invalid scope.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;アクセストークンが無効です。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The access token is invalid.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;/table&gt; &lt;/details&gt;  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ad_group_service_remove_post**
> AdGroupServiceMutateResponse ad_group_service_remove_post(ad_group_service_operation=ad_group_service_operation)



<div lang=\"ja\">広告グループを削除します。</div> <div lang=\"en\">Removes Ad group information.</div>

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
    api_instance = yahoo_ads_search.AdGroupServiceApi(api_client)
    ad_group_service_operation = yahoo_ads_search.AdGroupServiceOperation() # AdGroupServiceOperation |  (optional)

    try:
        api_response = api_instance.ad_group_service_remove_post(ad_group_service_operation=ad_group_service_operation)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AdGroupServiceApi->ad_group_service_remove_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ad_group_service_operation** | [**AdGroupServiceOperation**](AdGroupServiceOperation.md)|  | [optional]

### Return type

[**AdGroupServiceMutateResponse**](AdGroupServiceMutateResponse.md)

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
**200** | &lt;details&gt; &lt;summary&gt;Error Codes&lt;/summary&gt; &lt;table border&#x3D;\&quot;1\&quot;&gt; &lt;tr&gt;&lt;th&gt;Code&lt;/th&gt;&lt;th&gt;Message&lt;/th&gt;&lt;th&gt;Description&lt;/th&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;0001&lt;/td&gt;&lt;td&gt;Invalid Request.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;さまざまな要因が考えられます。&lt;br&gt;主な要因は、パラメータの値が不正か、誤りがあるためにオペレーションが完了できません。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;This error can result for a variety of reasons. &lt;br&gt;Typically because one of the parameter values in the request is wrong or invalid and the operation cannot be completed.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;R0001&lt;/td&gt;&lt;td&gt;Require.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;必須です。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;It is missing required parameter.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;F0001&lt;/td&gt;&lt;td&gt;Invalid format.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;値の形式が不正です。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The value format is invalid.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;V0001&lt;/td&gt;&lt;td&gt;Invalid value.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;値が無効です。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The value is invalid.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;S0001&lt;/td&gt;&lt;td&gt;Invalid Status.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;ステータスが無効です。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The status is invalid.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;L0002&lt;/td&gt;&lt;td&gt;Over list size.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;配列の要素数が上限値を超過しています。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The number of elements in the array exceeds the upper limit.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;L0001&lt;/td&gt;&lt;td&gt;Lower list size.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;配列の要素数が下限値を下回っています。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The number of elements in the array is below the lower limit.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;D0001&lt;/td&gt;&lt;td&gt;Duplicate.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;一意な値が重複しています。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The unique value is duplicated.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;RL001&lt;/td&gt;&lt;td&gt;Invalid relation.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;リクエストの関連性が矛盾しています。&lt;br&gt; たとえば、開始＞終了の日付指定を行なっているなど&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The relation of the request is contradictory.&lt;br&gt; For example, you are specifying the date of start &gt; end.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;LT001&lt;/td&gt;&lt;td&gt;Over limit.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;登録できる上限値を超過しています。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The upper limit value that can be registered is exceeded.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;I0001&lt;/td&gt;&lt;td&gt;Deactivated Id.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;IDが無効です。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The ID is Deactivated.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;210405&lt;/td&gt;&lt;td&gt;Budget has exceeded.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;予算額を超過しています。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The budget amount is exceeded.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;210303&lt;/td&gt;&lt;td&gt;Invalid conversion tracking.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;コンバージョントラッキングが無効です。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;Conversion tracking is Invalid.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;210301&lt;/td&gt;&lt;td&gt;Setting the disabled Auto bidding.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;編集中（削除含む）の自動入札を指定しています。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;Auto bidding in editing (including deletion) is specified.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;210304&lt;/td&gt;&lt;td&gt;Not enough conversions or invalid setting.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;コンバージョン数が不十分です。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;Conversions is not enough.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;210305&lt;/td&gt;&lt;td&gt;Auto bidding is already set.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;キーワードに個別の入札価格や入札設定が指定されている状態で、キャンペーンに「コンバージョン数の最大化」、または「コンバージョン単価の目標値」の自動入札を設定しております。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;Auto bidding of \&quot;Enhanced CPC\&quot; or \&quot;Target conversion spend\&quot; is set for campaigns with individual bidding prices and bidding settings specified for keywords.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;210306&lt;/td&gt;&lt;td&gt;Cannot use conversion optimizer.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;コンバージョンオプティマイザーが利用できません。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;Conversion optimizer cannot be used.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;210308&lt;/td&gt;&lt;td&gt;Set campaign active.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;キャンペーンがACTIVEでないため、入札設定が利用できません。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;Since the campaign is not ACTIVE, the bidding settings can not be used.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;210309&lt;/td&gt;&lt;td&gt;Set campaign to Manual CPC.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;キャンペーンが「MANUAL_CPC」でないため、入札設定が利用できません。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;Since the campaign is not \&quot;Manual CPC\&quot;, bidding settings can not be used.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;210409&lt;/td&gt;&lt;td&gt;AdGroupServiceBid setting limit has exceed.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;キャンペーン配下の広告広告グループに設定した入札金額または自動入札設定数が上限を超えています。&lt;br&gt;※1キャンペーンに設定できる入札金額および自動入札設定は、配下の広告グループ合計で1000件までです。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The bid amount or Auto bidding number set for the ad / ad group under the campaign exceeds the maximum limit. &lt;br&gt; * 1 The maximum bid amount and Auto bidding setting that can be set for the campaign is 1000 in total for the ad group below.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;211000&lt;/td&gt;&lt;td&gt;Cannot operate AdvancedURL.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;アドバンスドURLに移行済みのため、操作できません。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;Since it has already been transferred to AdvancedURL, it can not be operated.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;211001&lt;/td&gt;&lt;td&gt;Cannot set AdvancedMobileURL.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;アプリダウンロードキャンペーンでは、advancedMobileUrlの設定はできません。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;In the app download campaign, AdvancedMobileURL can not be set.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;211003&lt;/td&gt;&lt;td&gt;Domain does not match with DisplayURL.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;表示URLと最終リンク先URLのドメインが一致していません。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;Domain of DisplayURL and AdvancedUrl do not match.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;211004&lt;/td&gt;&lt;td&gt;Cannot set under AndroidCampaign.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;Androidのアプリキャンペーンでは、以下の設定ができません：&lt;br&gt;・キャンペーン、広告グループ、広告、キーワードにTrackingUrlや CustomParameterを設定&lt;br&gt;・キーワードに最終リンク先URLやスマートフォン向けURLを設定&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;In the Android app campaign, the following settings can not be made：&lt;br&gt;・Set TrackingUrl and CustomParameter for campaigns, ad groups, ads, keywords&lt;br&gt;・Set the AdvancedUrl and AdvancedMobileUrl for the keywords&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;/table&gt; &lt;/details&gt;  |  -  |
**403** | &lt;details&gt; &lt;summary&gt;Error Codes&lt;/summary&gt; &lt;table border&#x3D;\&quot;1\&quot;&gt; &lt;tr&gt;&lt;th&gt;Code&lt;/th&gt;&lt;th&gt;Message&lt;/th&gt;&lt;th&gt;Description&lt;/th&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;0098&lt;/td&gt;&lt;td&gt;Permission denied.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;権限がありません。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;Permission denied.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;0003&lt;/td&gt;&lt;td&gt;Frequency limit exceeded. Please try your request again later&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;アクセス頻度が上限値に達しました。時間をおいて再度実行してください。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;Frequency limit exceeded. Please try your request again later.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;/table&gt; &lt;/details&gt;  |  -  |
**401** | &lt;details&gt; &lt;summary&gt;Error Codes&lt;/summary&gt; &lt;table border&#x3D;\&quot;1\&quot;&gt; &lt;tr&gt;&lt;th&gt;Code&lt;/th&gt;&lt;th&gt;Message&lt;/th&gt;&lt;th&gt;Description&lt;/th&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;0110&lt;/td&gt;&lt;td&gt;Require access token.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;アクセストークンがリクエストヘッダに存在していません。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;There is no access token in the request header.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;0111&lt;/td&gt;&lt;td&gt;Authentication failed.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;アクセストークンの認証に失敗しました。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The access token authentication failed.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;0112&lt;/td&gt;&lt;td&gt;Account not found.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;アカウントが見つかりませんでした。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The account can not found.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;0113&lt;/td&gt;&lt;td&gt;Deactivated account.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;アカウントが無効です。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The account is deactivated.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;/table&gt; &lt;/details&gt;  |  -  |
**400** | &lt;details&gt; &lt;summary&gt;Error Codes&lt;/summary&gt; &lt;table border&#x3D;\&quot;1\&quot;&gt; &lt;tr&gt;&lt;th&gt;Code&lt;/th&gt;&lt;th&gt;Message&lt;/th&gt;&lt;th&gt;Description&lt;/th&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;0114&lt;/td&gt;&lt;td&gt;Invalid scope.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;アクセストークンが無効です。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The access token is invalid.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;/table&gt; &lt;/details&gt;  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ad_group_service_set_post**
> AdGroupServiceMutateResponse ad_group_service_set_post(ad_group_service_operation=ad_group_service_operation)



<div lang=\"ja\">広告グループを更新します。</div> <div lang=\"en\">Updates Ad group information.</div>

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
    api_instance = yahoo_ads_search.AdGroupServiceApi(api_client)
    ad_group_service_operation = yahoo_ads_search.AdGroupServiceOperation() # AdGroupServiceOperation |  (optional)

    try:
        api_response = api_instance.ad_group_service_set_post(ad_group_service_operation=ad_group_service_operation)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AdGroupServiceApi->ad_group_service_set_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ad_group_service_operation** | [**AdGroupServiceOperation**](AdGroupServiceOperation.md)|  | [optional]

### Return type

[**AdGroupServiceMutateResponse**](AdGroupServiceMutateResponse.md)

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
**200** | &lt;details&gt; &lt;summary&gt;Error Codes&lt;/summary&gt; &lt;table border&#x3D;\&quot;1\&quot;&gt; &lt;tr&gt;&lt;th&gt;Code&lt;/th&gt;&lt;th&gt;Message&lt;/th&gt;&lt;th&gt;Description&lt;/th&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;0001&lt;/td&gt;&lt;td&gt;Invalid Request.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;さまざまな要因が考えられます。&lt;br&gt;主な要因は、パラメータの値が不正か、誤りがあるためにオペレーションが完了できません。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;This error can result for a variety of reasons. &lt;br&gt;Typically because one of the parameter values in the request is wrong or invalid and the operation cannot be completed.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;R0001&lt;/td&gt;&lt;td&gt;Require.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;必須です。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;It is missing required parameter.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;F0001&lt;/td&gt;&lt;td&gt;Invalid format.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;値の形式が不正です。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The value format is invalid.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;V0001&lt;/td&gt;&lt;td&gt;Invalid value.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;値が無効です。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The value is invalid.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;S0001&lt;/td&gt;&lt;td&gt;Invalid Status.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;ステータスが無効です。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The status is invalid.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;L0002&lt;/td&gt;&lt;td&gt;Over list size.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;配列の要素数が上限値を超過しています。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The number of elements in the array exceeds the upper limit.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;L0001&lt;/td&gt;&lt;td&gt;Lower list size.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;配列の要素数が下限値を下回っています。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The number of elements in the array is below the lower limit.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;D0001&lt;/td&gt;&lt;td&gt;Duplicate.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;一意な値が重複しています。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The unique value is duplicated.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;RL001&lt;/td&gt;&lt;td&gt;Invalid relation.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;リクエストの関連性が矛盾しています。&lt;br&gt; たとえば、開始＞終了の日付指定を行なっているなど&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The relation of the request is contradictory.&lt;br&gt; For example, you are specifying the date of start &gt; end.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;LT001&lt;/td&gt;&lt;td&gt;Over limit.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;登録できる上限値を超過しています。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The upper limit value that can be registered is exceeded.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;I0001&lt;/td&gt;&lt;td&gt;Deactivated Id.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;IDが無効です。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The ID is Deactivated.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;210405&lt;/td&gt;&lt;td&gt;Budget has exceeded.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;予算額を超過しています。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The budget amount is exceeded.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;210303&lt;/td&gt;&lt;td&gt;Invalid conversion tracking.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;コンバージョントラッキングが無効です。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;Conversion tracking is Invalid.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;210301&lt;/td&gt;&lt;td&gt;Setting the disabled Auto bidding.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;編集中（削除含む）の自動入札を指定しています。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;Auto bidding in editing (including deletion) is specified.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;210304&lt;/td&gt;&lt;td&gt;Not enough conversions or invalid setting.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;コンバージョン数が不十分です。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;Conversions is not enough.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;210305&lt;/td&gt;&lt;td&gt;Auto bidding is already set.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;キーワードに個別の入札価格や入札設定が指定されている状態で、キャンペーンに「コンバージョン数の最大化」、または「コンバージョン単価の目標値」の自動入札を設定しております。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;Auto bidding of \&quot;Enhanced CPC\&quot; or \&quot;Target conversion spend\&quot; is set for campaigns with individual bidding prices and bidding settings specified for keywords.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;210306&lt;/td&gt;&lt;td&gt;Cannot use conversion optimizer.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;コンバージョンオプティマイザーが利用できません。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;Conversion optimizer cannot be used.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;210308&lt;/td&gt;&lt;td&gt;Set campaign active.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;キャンペーンがACTIVEでないため、入札設定が利用できません。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;Since the campaign is not ACTIVE, the bidding settings can not be used.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;210309&lt;/td&gt;&lt;td&gt;Set campaign to Manual CPC.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;キャンペーンが「MANUAL_CPC」でないため、入札設定が利用できません。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;Since the campaign is not \&quot;Manual CPC\&quot;, bidding settings can not be used.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;210409&lt;/td&gt;&lt;td&gt;AdGroupServiceBid setting limit has exceed.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;キャンペーン配下の広告広告グループに設定した入札金額または自動入札設定数が上限を超えています。&lt;br&gt;※1キャンペーンに設定できる入札金額および自動入札設定は、配下の広告グループ合計で1000件までです。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The bid amount or Auto bidding number set for the ad / ad group under the campaign exceeds the maximum limit. &lt;br&gt; * 1 The maximum bid amount and Auto bidding setting that can be set for the campaign is 1000 in total for the ad group below.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;211000&lt;/td&gt;&lt;td&gt;Cannot operate AdvancedURL.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;アドバンスドURLに移行済みのため、操作できません。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;Since it has already been transferred to AdvancedURL, it can not be operated.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;211001&lt;/td&gt;&lt;td&gt;Cannot set AdvancedMobileURL.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;アプリダウンロードキャンペーンでは、advancedMobileUrlの設定はできません。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;In the app download campaign, AdvancedMobileURL can not be set.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;211003&lt;/td&gt;&lt;td&gt;Domain does not match with DisplayURL.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;表示URLと最終リンク先URLのドメインが一致していません。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;Domain of DisplayURL and AdvancedUrl do not match.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;211004&lt;/td&gt;&lt;td&gt;Cannot set under AndroidCampaign.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;Androidのアプリキャンペーンでは、以下の設定ができません：&lt;br&gt;・キャンペーン、広告グループ、広告、キーワードにTrackingUrlや CustomParameterを設定&lt;br&gt;・キーワードに最終リンク先URLやスマートフォン向けURLを設定&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;In the Android app campaign, the following settings can not be made：&lt;br&gt;・Set TrackingUrl and CustomParameter for campaigns, ad groups, ads, keywords&lt;br&gt;・Set the AdvancedUrl and AdvancedMobileUrl for the keywords&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;/table&gt; &lt;/details&gt;  |  -  |
**403** | &lt;details&gt; &lt;summary&gt;Error Codes&lt;/summary&gt; &lt;table border&#x3D;\&quot;1\&quot;&gt; &lt;tr&gt;&lt;th&gt;Code&lt;/th&gt;&lt;th&gt;Message&lt;/th&gt;&lt;th&gt;Description&lt;/th&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;0098&lt;/td&gt;&lt;td&gt;Permission denied.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;権限がありません。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;Permission denied.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;0003&lt;/td&gt;&lt;td&gt;Frequency limit exceeded. Please try your request again later&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;アクセス頻度が上限値に達しました。時間をおいて再度実行してください。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;Frequency limit exceeded. Please try your request again later.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;/table&gt; &lt;/details&gt;  |  -  |
**401** | &lt;details&gt; &lt;summary&gt;Error Codes&lt;/summary&gt; &lt;table border&#x3D;\&quot;1\&quot;&gt; &lt;tr&gt;&lt;th&gt;Code&lt;/th&gt;&lt;th&gt;Message&lt;/th&gt;&lt;th&gt;Description&lt;/th&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;0110&lt;/td&gt;&lt;td&gt;Require access token.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;アクセストークンがリクエストヘッダに存在していません。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;There is no access token in the request header.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;0111&lt;/td&gt;&lt;td&gt;Authentication failed.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;アクセストークンの認証に失敗しました。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The access token authentication failed.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;0112&lt;/td&gt;&lt;td&gt;Account not found.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;アカウントが見つかりませんでした。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The account can not found.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;0113&lt;/td&gt;&lt;td&gt;Deactivated account.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;アカウントが無効です。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The account is deactivated.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;/table&gt; &lt;/details&gt;  |  -  |
**400** | &lt;details&gt; &lt;summary&gt;Error Codes&lt;/summary&gt; &lt;table border&#x3D;\&quot;1\&quot;&gt; &lt;tr&gt;&lt;th&gt;Code&lt;/th&gt;&lt;th&gt;Message&lt;/th&gt;&lt;th&gt;Description&lt;/th&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;0114&lt;/td&gt;&lt;td&gt;Invalid scope.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;アクセストークンが無効です。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The access token is invalid.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;/table&gt; &lt;/details&gt;  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


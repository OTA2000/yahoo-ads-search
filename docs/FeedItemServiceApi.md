# yahoo_ads_search.FeedItemServiceApi

All URIs are relative to *https://ads-search.yahooapis.jp/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**feed_item_service_add_post**](FeedItemServiceApi.md#feed_item_service_add_post) | **POST** /FeedItemService/add |
[**feed_item_service_get_post**](FeedItemServiceApi.md#feed_item_service_get_post) | **POST** /FeedItemService/get |
[**feed_item_service_remove_post**](FeedItemServiceApi.md#feed_item_service_remove_post) | **POST** /FeedItemService/remove |
[**feed_item_service_set_post**](FeedItemServiceApi.md#feed_item_service_set_post) | **POST** /FeedItemService/set |
[**feed_item_service_set_trademark_status_post**](FeedItemServiceApi.md#feed_item_service_set_trademark_status_post) | **POST** /FeedItemService/setTrademarkStatus |


# **feed_item_service_add_post**
> FeedItemServiceMutateResponse feed_item_service_add_post(feed_item_service_operation=feed_item_service_operation)



<div lang=\"ja\">フィードアイテム情報を追加します。</div> <div lang=\"en\">Add Feed Item information.</div>

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
    api_instance = yahoo_ads_search.FeedItemServiceApi(api_client)
    feed_item_service_operation = yahoo_ads_search.FeedItemServiceOperation() # FeedItemServiceOperation |  (optional)

    try:
        api_response = api_instance.feed_item_service_add_post(feed_item_service_operation=feed_item_service_operation)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FeedItemServiceApi->feed_item_service_add_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **feed_item_service_operation** | [**FeedItemServiceOperation**](FeedItemServiceOperation.md)|  | [optional]

### Return type

[**FeedItemServiceMutateResponse**](FeedItemServiceMutateResponse.md)

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
**200** | &lt;details&gt; &lt;summary&gt;Error Codes&lt;/summary&gt; &lt;table border&#x3D;\&quot;1\&quot;&gt; &lt;tr&gt;&lt;th&gt;Code&lt;/th&gt;&lt;th&gt;Message&lt;/th&gt;&lt;th&gt;Description&lt;/th&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;0001&lt;/td&gt;&lt;td&gt;Invalid Request.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;さまざまな要因が考えられます。&lt;br&gt;主な要因は、パラメータの値が不正か、誤りがあるためにオペレーションが完了できません。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;This error can result for a variety of reasons. &lt;br&gt;Typically because one of the parameter values in the request is wrong or invalid and the operation cannot be completed.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;R0001&lt;/td&gt;&lt;td&gt;Require.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;必須です。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;It is missing required parameter.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;F0001&lt;/td&gt;&lt;td&gt;Invalid format.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;値の形式が不正です。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The value format is invalid.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;V0001&lt;/td&gt;&lt;td&gt;Invalid value.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;値が無効です。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The value is invalid.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;S0001&lt;/td&gt;&lt;td&gt;Invalid Status.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;ステータスが無効です。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The status is invalid.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;L0002&lt;/td&gt;&lt;td&gt;Over list size.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;配列の要素数が上限値を超過しています。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The number of elements in the array exceeds the upper limit.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;L0001&lt;/td&gt;&lt;td&gt;Lower list size.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;配列の要素数が下限値を下回っています。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The number of elements in the array is below the lower limit.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;D0001&lt;/td&gt;&lt;td&gt;Duplicate.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;一意な値が重複しています。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The unique value is duplicated.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;RL001&lt;/td&gt;&lt;td&gt;Invalid relation.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;リクエストの関連性が矛盾しています。&lt;br&gt; たとえば、開始＞終了の日付指定を行なっているなど&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The relation of the request is contradictory.&lt;br&gt; For example, you are specifying the date of start &gt; end.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;LT001&lt;/td&gt;&lt;td&gt;Over limit.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;登録できる上限値を超過しています。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The upper limit value that can be registered is exceeded.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;I0001&lt;/td&gt;&lt;td&gt;Deactivated Id.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;IDが無効です。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The ID is Deactivated.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;210110&lt;/td&gt;&lt;td&gt;Invalid target&lt;/td&gt;&lt;td&gt;１日のスケジュール指定が上限値（6件）を超えています。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The daily schedule specification exceeds the upper limit (6 cases).&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;210517&lt;/td&gt;&lt;td&gt;Exceeds maximum word limit.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;キーワードは最大10個までしか指定できません。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;10 keywords can only be specified up to.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;210126&lt;/td&gt;&lt;td&gt;Mobile app download cannot connect to.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;アプリダウンロードキャンペーンは設定できません。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;Mobile app download cannot connect to.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;210123&lt;/td&gt;&lt;td&gt;Campaign targeting mismatch&lt;/td&gt;&lt;td&gt;targetingCampaignIdで指定したキャンペーンIDと、targetingAdGroupIdで指定した広告グループの上位キャンペーンIDが異なるため、設定できません。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;It can not be set because the campaign ID specified by targetingCampaignId is different from the campaign ID of the ad group specified by targetingAdGroupId.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;211000&lt;/td&gt;&lt;td&gt;Cannot operate AdvancedURL.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;アドバンスドURLに移行済みのため、操作できません。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;Since it has already been transferred to AdvancedURL, it can not be operated.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;211001&lt;/td&gt;&lt;td&gt;Cannot set AdvancedMobileURL.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;アプリダウンロードキャンペーンでは、advancedMobileUrlの設定はできません。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;In the app download campaign, AdvancedMobileURL can not be set.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;211003&lt;/td&gt;&lt;td&gt;Domain does not match with DisplayURL.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;表示URLと最終リンク先URLのドメインが一致していません。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;Domain of DisplayURL and AdvancedUrl do not match.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;211004&lt;/td&gt;&lt;td&gt;Cannot set under AndroidCampaign.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;Androidのアプリキャンペーンでは、以下の設定ができません：&lt;br&gt;・キャンペーン、広告グループ、広告、キーワードにTrackingUrlや CustomParameterを設定&lt;br&gt;・キーワードに最終リンク先URLやスマートフォン向けURLを設定&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;In the Android app campaign, the following settings can not be made：&lt;br&gt;・Set TrackingUrl and CustomParameter for campaigns, ad groups, ads, keywords&lt;br&gt;・Set the AdvancedUrl and AdvancedMobileUrl for the keywords&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;225305&lt;/td&gt;&lt;td&gt;invalid structured snippet header.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;カテゴリ補足オプション（ヘッダ）が不正です。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;Structured snippet header is invalid.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;211019&lt;/td&gt;&lt;td&gt;Request failed because of trademark conflicts.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;商標に抵触している為、登録できません。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;Request failed because of trademark conflicts.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;/table&gt; &lt;/details&gt;  |  -  |
**403** | &lt;details&gt; &lt;summary&gt;Error Codes&lt;/summary&gt; &lt;table border&#x3D;\&quot;1\&quot;&gt; &lt;tr&gt;&lt;th&gt;Code&lt;/th&gt;&lt;th&gt;Message&lt;/th&gt;&lt;th&gt;Description&lt;/th&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;0098&lt;/td&gt;&lt;td&gt;Permission denied.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;権限がありません。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;Permission denied.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;0003&lt;/td&gt;&lt;td&gt;Frequency limit exceeded. Please try your request again later&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;アクセス頻度が上限値に達しました。時間をおいて再度実行してください。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;Frequency limit exceeded. Please try your request again later.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;/table&gt; &lt;/details&gt;  |  -  |
**401** | &lt;details&gt; &lt;summary&gt;Error Codes&lt;/summary&gt; &lt;table border&#x3D;\&quot;1\&quot;&gt; &lt;tr&gt;&lt;th&gt;Code&lt;/th&gt;&lt;th&gt;Message&lt;/th&gt;&lt;th&gt;Description&lt;/th&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;0110&lt;/td&gt;&lt;td&gt;Require access token.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;アクセストークンがリクエストヘッダに存在していません。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;There is no access token in the request header.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;0111&lt;/td&gt;&lt;td&gt;Authentication failed.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;アクセストークンの認証に失敗しました。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The access token authentication failed.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;0112&lt;/td&gt;&lt;td&gt;Account not found.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;アカウントが見つかりませんでした。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The account can not found.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;0113&lt;/td&gt;&lt;td&gt;Deactivated account.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;アカウントが無効です。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The account is deactivated.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;/table&gt; &lt;/details&gt;  |  -  |
**400** | &lt;details&gt; &lt;summary&gt;Error Codes&lt;/summary&gt; &lt;table border&#x3D;\&quot;1\&quot;&gt; &lt;tr&gt;&lt;th&gt;Code&lt;/th&gt;&lt;th&gt;Message&lt;/th&gt;&lt;th&gt;Description&lt;/th&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;0114&lt;/td&gt;&lt;td&gt;Invalid scope.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;アクセストークンが無効です。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The access token is invalid.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;/table&gt; &lt;/details&gt;  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **feed_item_service_get_post**
> FeedItemServiceGetResponse feed_item_service_get_post(feed_item_service_selector=feed_item_service_selector)



<div lang=\"ja\">フィードアイテム情報を取得します。</div> <div lang=\"en\">Get Feed Item information.</div>

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
    api_instance = yahoo_ads_search.FeedItemServiceApi(api_client)
    feed_item_service_selector = yahoo_ads_search.FeedItemServiceSelector() # FeedItemServiceSelector |  (optional)

    try:
        api_response = api_instance.feed_item_service_get_post(feed_item_service_selector=feed_item_service_selector)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FeedItemServiceApi->feed_item_service_get_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **feed_item_service_selector** | [**FeedItemServiceSelector**](FeedItemServiceSelector.md)|  | [optional]

### Return type

[**FeedItemServiceGetResponse**](FeedItemServiceGetResponse.md)

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
**200** | &lt;details&gt; &lt;summary&gt;Error Codes&lt;/summary&gt; &lt;table border&#x3D;\&quot;1\&quot;&gt; &lt;tr&gt;&lt;th&gt;Code&lt;/th&gt;&lt;th&gt;Message&lt;/th&gt;&lt;th&gt;Description&lt;/th&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;0001&lt;/td&gt;&lt;td&gt;Invalid Request.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;さまざまな要因が考えられます。&lt;br&gt;主な要因は、パラメータの値が不正か、誤りがあるためにオペレーションが完了できません。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;This error can result for a variety of reasons. &lt;br&gt;Typically because one of the parameter values in the request is wrong or invalid and the operation cannot be completed.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;R0001&lt;/td&gt;&lt;td&gt;Require.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;必須です。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;It is missing required parameter.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;F0001&lt;/td&gt;&lt;td&gt;Invalid format.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;値の形式が不正です。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The value format is invalid.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;V0001&lt;/td&gt;&lt;td&gt;Invalid value.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;値が無効です。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The value is invalid.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;S0001&lt;/td&gt;&lt;td&gt;Invalid Status.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;ステータスが無効です。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The status is invalid.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;L0002&lt;/td&gt;&lt;td&gt;Over list size.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;配列の要素数が上限値を超過しています。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The number of elements in the array exceeds the upper limit.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;L0001&lt;/td&gt;&lt;td&gt;Lower list size.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;配列の要素数が下限値を下回っています。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The number of elements in the array is below the lower limit.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;D0001&lt;/td&gt;&lt;td&gt;Duplicate.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;一意な値が重複しています。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The unique value is duplicated.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;RL001&lt;/td&gt;&lt;td&gt;Invalid relation.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;リクエストの関連性が矛盾しています。&lt;br&gt; たとえば、開始＞終了の日付指定を行なっているなど&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The relation of the request is contradictory.&lt;br&gt; For example, you are specifying the date of start &gt; end.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;LT001&lt;/td&gt;&lt;td&gt;Over limit.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;登録できる上限値を超過しています。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The upper limit value that can be registered is exceeded.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;I0001&lt;/td&gt;&lt;td&gt;Deactivated Id.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;IDが無効です。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The ID is Deactivated.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;210110&lt;/td&gt;&lt;td&gt;Invalid target&lt;/td&gt;&lt;td&gt;１日のスケジュール指定が上限値（6件）を超えています。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The daily schedule specification exceeds the upper limit (6 cases).&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;210517&lt;/td&gt;&lt;td&gt;Exceeds maximum word limit.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;キーワードは最大10個までしか指定できません。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;10 keywords can only be specified up to.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;210126&lt;/td&gt;&lt;td&gt;Mobile app download cannot connect to.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;アプリダウンロードキャンペーンは設定できません。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;Mobile app download cannot connect to.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;210123&lt;/td&gt;&lt;td&gt;Campaign targeting mismatch&lt;/td&gt;&lt;td&gt;targetingCampaignIdで指定したキャンペーンIDと、targetingAdGroupIdで指定した広告グループの上位キャンペーンIDが異なるため、設定できません。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;It can not be set because the campaign ID specified by targetingCampaignId is different from the campaign ID of the ad group specified by targetingAdGroupId.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;211000&lt;/td&gt;&lt;td&gt;Cannot operate AdvancedURL.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;アドバンスドURLに移行済みのため、操作できません。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;Since it has already been transferred to AdvancedURL, it can not be operated.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;211001&lt;/td&gt;&lt;td&gt;Cannot set AdvancedMobileURL.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;アプリダウンロードキャンペーンでは、advancedMobileUrlの設定はできません。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;In the app download campaign, AdvancedMobileURL can not be set.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;211003&lt;/td&gt;&lt;td&gt;Domain does not match with DisplayURL.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;表示URLと最終リンク先URLのドメインが一致していません。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;Domain of DisplayURL and AdvancedUrl do not match.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;211004&lt;/td&gt;&lt;td&gt;Cannot set under AndroidCampaign.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;Androidのアプリキャンペーンでは、以下の設定ができません：&lt;br&gt;・キャンペーン、広告グループ、広告、キーワードにTrackingUrlや CustomParameterを設定&lt;br&gt;・キーワードに最終リンク先URLやスマートフォン向けURLを設定&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;In the Android app campaign, the following settings can not be made：&lt;br&gt;・Set TrackingUrl and CustomParameter for campaigns, ad groups, ads, keywords&lt;br&gt;・Set the AdvancedUrl and AdvancedMobileUrl for the keywords&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;225305&lt;/td&gt;&lt;td&gt;invalid structured snippet header.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;カテゴリ補足オプション（ヘッダ）が不正です。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;Structured snippet header is invalid.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;211019&lt;/td&gt;&lt;td&gt;Request failed because of trademark conflicts.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;商標に抵触している為、登録できません。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;Request failed because of trademark conflicts.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;/table&gt; &lt;/details&gt;  |  -  |
**403** | &lt;details&gt; &lt;summary&gt;Error Codes&lt;/summary&gt; &lt;table border&#x3D;\&quot;1\&quot;&gt; &lt;tr&gt;&lt;th&gt;Code&lt;/th&gt;&lt;th&gt;Message&lt;/th&gt;&lt;th&gt;Description&lt;/th&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;0098&lt;/td&gt;&lt;td&gt;Permission denied.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;権限がありません。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;Permission denied.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;0003&lt;/td&gt;&lt;td&gt;Frequency limit exceeded. Please try your request again later&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;アクセス頻度が上限値に達しました。時間をおいて再度実行してください。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;Frequency limit exceeded. Please try your request again later.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;/table&gt; &lt;/details&gt;  |  -  |
**401** | &lt;details&gt; &lt;summary&gt;Error Codes&lt;/summary&gt; &lt;table border&#x3D;\&quot;1\&quot;&gt; &lt;tr&gt;&lt;th&gt;Code&lt;/th&gt;&lt;th&gt;Message&lt;/th&gt;&lt;th&gt;Description&lt;/th&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;0110&lt;/td&gt;&lt;td&gt;Require access token.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;アクセストークンがリクエストヘッダに存在していません。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;There is no access token in the request header.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;0111&lt;/td&gt;&lt;td&gt;Authentication failed.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;アクセストークンの認証に失敗しました。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The access token authentication failed.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;0112&lt;/td&gt;&lt;td&gt;Account not found.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;アカウントが見つかりませんでした。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The account can not found.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;0113&lt;/td&gt;&lt;td&gt;Deactivated account.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;アカウントが無効です。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The account is deactivated.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;/table&gt; &lt;/details&gt;  |  -  |
**400** | &lt;details&gt; &lt;summary&gt;Error Codes&lt;/summary&gt; &lt;table border&#x3D;\&quot;1\&quot;&gt; &lt;tr&gt;&lt;th&gt;Code&lt;/th&gt;&lt;th&gt;Message&lt;/th&gt;&lt;th&gt;Description&lt;/th&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;0114&lt;/td&gt;&lt;td&gt;Invalid scope.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;アクセストークンが無効です。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The access token is invalid.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;/table&gt; &lt;/details&gt;  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **feed_item_service_remove_post**
> FeedItemServiceMutateResponse feed_item_service_remove_post(feed_item_service_operation=feed_item_service_operation)



<div lang=\"ja\">フィードアイテム情報を削除します。</div> <div lang=\"en\">Remove the Feed Item details.</div>

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
    api_instance = yahoo_ads_search.FeedItemServiceApi(api_client)
    feed_item_service_operation = yahoo_ads_search.FeedItemServiceOperation() # FeedItemServiceOperation |  (optional)

    try:
        api_response = api_instance.feed_item_service_remove_post(feed_item_service_operation=feed_item_service_operation)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FeedItemServiceApi->feed_item_service_remove_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **feed_item_service_operation** | [**FeedItemServiceOperation**](FeedItemServiceOperation.md)|  | [optional]

### Return type

[**FeedItemServiceMutateResponse**](FeedItemServiceMutateResponse.md)

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
**200** | &lt;details&gt; &lt;summary&gt;Error Codes&lt;/summary&gt; &lt;table border&#x3D;\&quot;1\&quot;&gt; &lt;tr&gt;&lt;th&gt;Code&lt;/th&gt;&lt;th&gt;Message&lt;/th&gt;&lt;th&gt;Description&lt;/th&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;0001&lt;/td&gt;&lt;td&gt;Invalid Request.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;さまざまな要因が考えられます。&lt;br&gt;主な要因は、パラメータの値が不正か、誤りがあるためにオペレーションが完了できません。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;This error can result for a variety of reasons. &lt;br&gt;Typically because one of the parameter values in the request is wrong or invalid and the operation cannot be completed.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;R0001&lt;/td&gt;&lt;td&gt;Require.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;必須です。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;It is missing required parameter.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;F0001&lt;/td&gt;&lt;td&gt;Invalid format.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;値の形式が不正です。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The value format is invalid.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;V0001&lt;/td&gt;&lt;td&gt;Invalid value.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;値が無効です。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The value is invalid.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;S0001&lt;/td&gt;&lt;td&gt;Invalid Status.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;ステータスが無効です。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The status is invalid.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;L0002&lt;/td&gt;&lt;td&gt;Over list size.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;配列の要素数が上限値を超過しています。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The number of elements in the array exceeds the upper limit.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;L0001&lt;/td&gt;&lt;td&gt;Lower list size.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;配列の要素数が下限値を下回っています。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The number of elements in the array is below the lower limit.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;D0001&lt;/td&gt;&lt;td&gt;Duplicate.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;一意な値が重複しています。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The unique value is duplicated.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;RL001&lt;/td&gt;&lt;td&gt;Invalid relation.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;リクエストの関連性が矛盾しています。&lt;br&gt; たとえば、開始＞終了の日付指定を行なっているなど&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The relation of the request is contradictory.&lt;br&gt; For example, you are specifying the date of start &gt; end.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;LT001&lt;/td&gt;&lt;td&gt;Over limit.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;登録できる上限値を超過しています。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The upper limit value that can be registered is exceeded.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;I0001&lt;/td&gt;&lt;td&gt;Deactivated Id.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;IDが無効です。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The ID is Deactivated.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;210110&lt;/td&gt;&lt;td&gt;Invalid target&lt;/td&gt;&lt;td&gt;１日のスケジュール指定が上限値（6件）を超えています。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The daily schedule specification exceeds the upper limit (6 cases).&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;210517&lt;/td&gt;&lt;td&gt;Exceeds maximum word limit.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;キーワードは最大10個までしか指定できません。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;10 keywords can only be specified up to.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;210126&lt;/td&gt;&lt;td&gt;Mobile app download cannot connect to.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;アプリダウンロードキャンペーンは設定できません。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;Mobile app download cannot connect to.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;210123&lt;/td&gt;&lt;td&gt;Campaign targeting mismatch&lt;/td&gt;&lt;td&gt;targetingCampaignIdで指定したキャンペーンIDと、targetingAdGroupIdで指定した広告グループの上位キャンペーンIDが異なるため、設定できません。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;It can not be set because the campaign ID specified by targetingCampaignId is different from the campaign ID of the ad group specified by targetingAdGroupId.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;211000&lt;/td&gt;&lt;td&gt;Cannot operate AdvancedURL.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;アドバンスドURLに移行済みのため、操作できません。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;Since it has already been transferred to AdvancedURL, it can not be operated.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;211001&lt;/td&gt;&lt;td&gt;Cannot set AdvancedMobileURL.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;アプリダウンロードキャンペーンでは、advancedMobileUrlの設定はできません。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;In the app download campaign, AdvancedMobileURL can not be set.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;211003&lt;/td&gt;&lt;td&gt;Domain does not match with DisplayURL.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;表示URLと最終リンク先URLのドメインが一致していません。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;Domain of DisplayURL and AdvancedUrl do not match.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;211004&lt;/td&gt;&lt;td&gt;Cannot set under AndroidCampaign.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;Androidのアプリキャンペーンでは、以下の設定ができません：&lt;br&gt;・キャンペーン、広告グループ、広告、キーワードにTrackingUrlや CustomParameterを設定&lt;br&gt;・キーワードに最終リンク先URLやスマートフォン向けURLを設定&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;In the Android app campaign, the following settings can not be made：&lt;br&gt;・Set TrackingUrl and CustomParameter for campaigns, ad groups, ads, keywords&lt;br&gt;・Set the AdvancedUrl and AdvancedMobileUrl for the keywords&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;225305&lt;/td&gt;&lt;td&gt;invalid structured snippet header.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;カテゴリ補足オプション（ヘッダ）が不正です。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;Structured snippet header is invalid.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;211019&lt;/td&gt;&lt;td&gt;Request failed because of trademark conflicts.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;商標に抵触している為、登録できません。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;Request failed because of trademark conflicts.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;/table&gt; &lt;/details&gt;  |  -  |
**403** | &lt;details&gt; &lt;summary&gt;Error Codes&lt;/summary&gt; &lt;table border&#x3D;\&quot;1\&quot;&gt; &lt;tr&gt;&lt;th&gt;Code&lt;/th&gt;&lt;th&gt;Message&lt;/th&gt;&lt;th&gt;Description&lt;/th&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;0098&lt;/td&gt;&lt;td&gt;Permission denied.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;権限がありません。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;Permission denied.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;0003&lt;/td&gt;&lt;td&gt;Frequency limit exceeded. Please try your request again later&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;アクセス頻度が上限値に達しました。時間をおいて再度実行してください。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;Frequency limit exceeded. Please try your request again later.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;/table&gt; &lt;/details&gt;  |  -  |
**401** | &lt;details&gt; &lt;summary&gt;Error Codes&lt;/summary&gt; &lt;table border&#x3D;\&quot;1\&quot;&gt; &lt;tr&gt;&lt;th&gt;Code&lt;/th&gt;&lt;th&gt;Message&lt;/th&gt;&lt;th&gt;Description&lt;/th&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;0110&lt;/td&gt;&lt;td&gt;Require access token.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;アクセストークンがリクエストヘッダに存在していません。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;There is no access token in the request header.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;0111&lt;/td&gt;&lt;td&gt;Authentication failed.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;アクセストークンの認証に失敗しました。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The access token authentication failed.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;0112&lt;/td&gt;&lt;td&gt;Account not found.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;アカウントが見つかりませんでした。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The account can not found.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;0113&lt;/td&gt;&lt;td&gt;Deactivated account.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;アカウントが無効です。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The account is deactivated.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;/table&gt; &lt;/details&gt;  |  -  |
**400** | &lt;details&gt; &lt;summary&gt;Error Codes&lt;/summary&gt; &lt;table border&#x3D;\&quot;1\&quot;&gt; &lt;tr&gt;&lt;th&gt;Code&lt;/th&gt;&lt;th&gt;Message&lt;/th&gt;&lt;th&gt;Description&lt;/th&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;0114&lt;/td&gt;&lt;td&gt;Invalid scope.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;アクセストークンが無効です。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The access token is invalid.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;/table&gt; &lt;/details&gt;  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **feed_item_service_set_post**
> FeedItemServiceMutateResponse feed_item_service_set_post(feed_item_service_operation=feed_item_service_operation)



<div lang=\"ja\">フィードアイテム情報を更新します。</div> <div lang=\"en\">Updates the Feed Item details.</div>

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
    api_instance = yahoo_ads_search.FeedItemServiceApi(api_client)
    feed_item_service_operation = yahoo_ads_search.FeedItemServiceOperation() # FeedItemServiceOperation |  (optional)

    try:
        api_response = api_instance.feed_item_service_set_post(feed_item_service_operation=feed_item_service_operation)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FeedItemServiceApi->feed_item_service_set_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **feed_item_service_operation** | [**FeedItemServiceOperation**](FeedItemServiceOperation.md)|  | [optional]

### Return type

[**FeedItemServiceMutateResponse**](FeedItemServiceMutateResponse.md)

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
**200** | &lt;details&gt; &lt;summary&gt;Error Codes&lt;/summary&gt; &lt;table border&#x3D;\&quot;1\&quot;&gt; &lt;tr&gt;&lt;th&gt;Code&lt;/th&gt;&lt;th&gt;Message&lt;/th&gt;&lt;th&gt;Description&lt;/th&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;0001&lt;/td&gt;&lt;td&gt;Invalid Request.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;さまざまな要因が考えられます。&lt;br&gt;主な要因は、パラメータの値が不正か、誤りがあるためにオペレーションが完了できません。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;This error can result for a variety of reasons. &lt;br&gt;Typically because one of the parameter values in the request is wrong or invalid and the operation cannot be completed.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;R0001&lt;/td&gt;&lt;td&gt;Require.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;必須です。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;It is missing required parameter.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;F0001&lt;/td&gt;&lt;td&gt;Invalid format.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;値の形式が不正です。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The value format is invalid.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;V0001&lt;/td&gt;&lt;td&gt;Invalid value.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;値が無効です。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The value is invalid.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;S0001&lt;/td&gt;&lt;td&gt;Invalid Status.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;ステータスが無効です。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The status is invalid.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;L0002&lt;/td&gt;&lt;td&gt;Over list size.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;配列の要素数が上限値を超過しています。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The number of elements in the array exceeds the upper limit.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;L0001&lt;/td&gt;&lt;td&gt;Lower list size.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;配列の要素数が下限値を下回っています。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The number of elements in the array is below the lower limit.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;D0001&lt;/td&gt;&lt;td&gt;Duplicate.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;一意な値が重複しています。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The unique value is duplicated.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;RL001&lt;/td&gt;&lt;td&gt;Invalid relation.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;リクエストの関連性が矛盾しています。&lt;br&gt; たとえば、開始＞終了の日付指定を行なっているなど&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The relation of the request is contradictory.&lt;br&gt; For example, you are specifying the date of start &gt; end.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;LT001&lt;/td&gt;&lt;td&gt;Over limit.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;登録できる上限値を超過しています。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The upper limit value that can be registered is exceeded.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;I0001&lt;/td&gt;&lt;td&gt;Deactivated Id.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;IDが無効です。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The ID is Deactivated.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;210110&lt;/td&gt;&lt;td&gt;Invalid target&lt;/td&gt;&lt;td&gt;１日のスケジュール指定が上限値（6件）を超えています。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The daily schedule specification exceeds the upper limit (6 cases).&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;210517&lt;/td&gt;&lt;td&gt;Exceeds maximum word limit.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;キーワードは最大10個までしか指定できません。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;10 keywords can only be specified up to.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;210126&lt;/td&gt;&lt;td&gt;Mobile app download cannot connect to.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;アプリダウンロードキャンペーンは設定できません。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;Mobile app download cannot connect to.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;210123&lt;/td&gt;&lt;td&gt;Campaign targeting mismatch&lt;/td&gt;&lt;td&gt;targetingCampaignIdで指定したキャンペーンIDと、targetingAdGroupIdで指定した広告グループの上位キャンペーンIDが異なるため、設定できません。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;It can not be set because the campaign ID specified by targetingCampaignId is different from the campaign ID of the ad group specified by targetingAdGroupId.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;211000&lt;/td&gt;&lt;td&gt;Cannot operate AdvancedURL.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;アドバンスドURLに移行済みのため、操作できません。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;Since it has already been transferred to AdvancedURL, it can not be operated.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;211001&lt;/td&gt;&lt;td&gt;Cannot set AdvancedMobileURL.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;アプリダウンロードキャンペーンでは、advancedMobileUrlの設定はできません。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;In the app download campaign, AdvancedMobileURL can not be set.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;211003&lt;/td&gt;&lt;td&gt;Domain does not match with DisplayURL.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;表示URLと最終リンク先URLのドメインが一致していません。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;Domain of DisplayURL and AdvancedUrl do not match.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;211004&lt;/td&gt;&lt;td&gt;Cannot set under AndroidCampaign.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;Androidのアプリキャンペーンでは、以下の設定ができません：&lt;br&gt;・キャンペーン、広告グループ、広告、キーワードにTrackingUrlや CustomParameterを設定&lt;br&gt;・キーワードに最終リンク先URLやスマートフォン向けURLを設定&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;In the Android app campaign, the following settings can not be made：&lt;br&gt;・Set TrackingUrl and CustomParameter for campaigns, ad groups, ads, keywords&lt;br&gt;・Set the AdvancedUrl and AdvancedMobileUrl for the keywords&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;225305&lt;/td&gt;&lt;td&gt;invalid structured snippet header.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;カテゴリ補足オプション（ヘッダ）が不正です。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;Structured snippet header is invalid.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;211019&lt;/td&gt;&lt;td&gt;Request failed because of trademark conflicts.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;商標に抵触している為、登録できません。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;Request failed because of trademark conflicts.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;/table&gt; &lt;/details&gt;  |  -  |
**403** | &lt;details&gt; &lt;summary&gt;Error Codes&lt;/summary&gt; &lt;table border&#x3D;\&quot;1\&quot;&gt; &lt;tr&gt;&lt;th&gt;Code&lt;/th&gt;&lt;th&gt;Message&lt;/th&gt;&lt;th&gt;Description&lt;/th&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;0098&lt;/td&gt;&lt;td&gt;Permission denied.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;権限がありません。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;Permission denied.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;0003&lt;/td&gt;&lt;td&gt;Frequency limit exceeded. Please try your request again later&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;アクセス頻度が上限値に達しました。時間をおいて再度実行してください。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;Frequency limit exceeded. Please try your request again later.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;/table&gt; &lt;/details&gt;  |  -  |
**401** | &lt;details&gt; &lt;summary&gt;Error Codes&lt;/summary&gt; &lt;table border&#x3D;\&quot;1\&quot;&gt; &lt;tr&gt;&lt;th&gt;Code&lt;/th&gt;&lt;th&gt;Message&lt;/th&gt;&lt;th&gt;Description&lt;/th&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;0110&lt;/td&gt;&lt;td&gt;Require access token.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;アクセストークンがリクエストヘッダに存在していません。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;There is no access token in the request header.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;0111&lt;/td&gt;&lt;td&gt;Authentication failed.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;アクセストークンの認証に失敗しました。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The access token authentication failed.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;0112&lt;/td&gt;&lt;td&gt;Account not found.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;アカウントが見つかりませんでした。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The account can not found.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;0113&lt;/td&gt;&lt;td&gt;Deactivated account.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;アカウントが無効です。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The account is deactivated.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;/table&gt; &lt;/details&gt;  |  -  |
**400** | &lt;details&gt; &lt;summary&gt;Error Codes&lt;/summary&gt; &lt;table border&#x3D;\&quot;1\&quot;&gt; &lt;tr&gt;&lt;th&gt;Code&lt;/th&gt;&lt;th&gt;Message&lt;/th&gt;&lt;th&gt;Description&lt;/th&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;0114&lt;/td&gt;&lt;td&gt;Invalid scope.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;アクセストークンが無効です。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The access token is invalid.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;/table&gt; &lt;/details&gt;  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **feed_item_service_set_trademark_status_post**
> FeedItemServiceSetTrademarkStatusResponse feed_item_service_set_trademark_status_post(feed_item_service_set_trademark_status_operation=feed_item_service_set_trademark_status_operation)



<div lang=\"ja\">商標の使用制限解除を確認します。</div> <div lang=\"en\">Confirm the status of trademark restriction.</div>

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
    api_instance = yahoo_ads_search.FeedItemServiceApi(api_client)
    feed_item_service_set_trademark_status_operation = yahoo_ads_search.FeedItemServiceSetTrademarkStatusOperation() # FeedItemServiceSetTrademarkStatusOperation |  (optional)

    try:
        api_response = api_instance.feed_item_service_set_trademark_status_post(feed_item_service_set_trademark_status_operation=feed_item_service_set_trademark_status_operation)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FeedItemServiceApi->feed_item_service_set_trademark_status_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **feed_item_service_set_trademark_status_operation** | [**FeedItemServiceSetTrademarkStatusOperation**](FeedItemServiceSetTrademarkStatusOperation.md)|  | [optional]

### Return type

[**FeedItemServiceSetTrademarkStatusResponse**](FeedItemServiceSetTrademarkStatusResponse.md)

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
**200** | &lt;details&gt; &lt;summary&gt;Error Codes&lt;/summary&gt; &lt;table border&#x3D;\&quot;1\&quot;&gt; &lt;tr&gt;&lt;th&gt;Code&lt;/th&gt;&lt;th&gt;Message&lt;/th&gt;&lt;th&gt;Description&lt;/th&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;0001&lt;/td&gt;&lt;td&gt;Invalid Request.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;さまざまな要因が考えられます。&lt;br&gt;主な要因は、パラメータの値が不正か、誤りがあるためにオペレーションが完了できません。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;This error can result for a variety of reasons. &lt;br&gt;Typically because one of the parameter values in the request is wrong or invalid and the operation cannot be completed.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;R0001&lt;/td&gt;&lt;td&gt;Require.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;必須です。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;It is missing required parameter.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;F0001&lt;/td&gt;&lt;td&gt;Invalid format.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;値の形式が不正です。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The value format is invalid.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;V0001&lt;/td&gt;&lt;td&gt;Invalid value.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;値が無効です。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The value is invalid.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;S0001&lt;/td&gt;&lt;td&gt;Invalid Status.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;ステータスが無効です。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The status is invalid.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;L0002&lt;/td&gt;&lt;td&gt;Over list size.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;配列の要素数が上限値を超過しています。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The number of elements in the array exceeds the upper limit.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;L0001&lt;/td&gt;&lt;td&gt;Lower list size.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;配列の要素数が下限値を下回っています。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The number of elements in the array is below the lower limit.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;D0001&lt;/td&gt;&lt;td&gt;Duplicate.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;一意な値が重複しています。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The unique value is duplicated.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;RL001&lt;/td&gt;&lt;td&gt;Invalid relation.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;リクエストの関連性が矛盾しています。&lt;br&gt; たとえば、開始＞終了の日付指定を行なっているなど&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The relation of the request is contradictory.&lt;br&gt; For example, you are specifying the date of start &gt; end.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;LT001&lt;/td&gt;&lt;td&gt;Over limit.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;登録できる上限値を超過しています。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The upper limit value that can be registered is exceeded.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;I0001&lt;/td&gt;&lt;td&gt;Deactivated Id.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;IDが無効です。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The ID is Deactivated.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;210110&lt;/td&gt;&lt;td&gt;Invalid target&lt;/td&gt;&lt;td&gt;１日のスケジュール指定が上限値（6件）を超えています。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The daily schedule specification exceeds the upper limit (6 cases).&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;210517&lt;/td&gt;&lt;td&gt;Exceeds maximum word limit.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;キーワードは最大10個までしか指定できません。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;10 keywords can only be specified up to.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;210126&lt;/td&gt;&lt;td&gt;Mobile app download cannot connect to.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;アプリダウンロードキャンペーンは設定できません。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;Mobile app download cannot connect to.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;210123&lt;/td&gt;&lt;td&gt;Campaign targeting mismatch&lt;/td&gt;&lt;td&gt;targetingCampaignIdで指定したキャンペーンIDと、targetingAdGroupIdで指定した広告グループの上位キャンペーンIDが異なるため、設定できません。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;It can not be set because the campaign ID specified by targetingCampaignId is different from the campaign ID of the ad group specified by targetingAdGroupId.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;211000&lt;/td&gt;&lt;td&gt;Cannot operate AdvancedURL.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;アドバンスドURLに移行済みのため、操作できません。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;Since it has already been transferred to AdvancedURL, it can not be operated.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;211001&lt;/td&gt;&lt;td&gt;Cannot set AdvancedMobileURL.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;アプリダウンロードキャンペーンでは、advancedMobileUrlの設定はできません。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;In the app download campaign, AdvancedMobileURL can not be set.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;211003&lt;/td&gt;&lt;td&gt;Domain does not match with DisplayURL.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;表示URLと最終リンク先URLのドメインが一致していません。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;Domain of DisplayURL and AdvancedUrl do not match.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;211004&lt;/td&gt;&lt;td&gt;Cannot set under AndroidCampaign.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;Androidのアプリキャンペーンでは、以下の設定ができません：&lt;br&gt;・キャンペーン、広告グループ、広告、キーワードにTrackingUrlや CustomParameterを設定&lt;br&gt;・キーワードに最終リンク先URLやスマートフォン向けURLを設定&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;In the Android app campaign, the following settings can not be made：&lt;br&gt;・Set TrackingUrl and CustomParameter for campaigns, ad groups, ads, keywords&lt;br&gt;・Set the AdvancedUrl and AdvancedMobileUrl for the keywords&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;225305&lt;/td&gt;&lt;td&gt;invalid structured snippet header.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;カテゴリ補足オプション（ヘッダ）が不正です。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;Structured snippet header is invalid.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;211019&lt;/td&gt;&lt;td&gt;Request failed because of trademark conflicts.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;商標に抵触している為、登録できません。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;Request failed because of trademark conflicts.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;/table&gt; &lt;/details&gt;  |  -  |
**403** | &lt;details&gt; &lt;summary&gt;Error Codes&lt;/summary&gt; &lt;table border&#x3D;\&quot;1\&quot;&gt; &lt;tr&gt;&lt;th&gt;Code&lt;/th&gt;&lt;th&gt;Message&lt;/th&gt;&lt;th&gt;Description&lt;/th&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;0098&lt;/td&gt;&lt;td&gt;Permission denied.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;権限がありません。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;Permission denied.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;0003&lt;/td&gt;&lt;td&gt;Frequency limit exceeded. Please try your request again later&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;アクセス頻度が上限値に達しました。時間をおいて再度実行してください。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;Frequency limit exceeded. Please try your request again later.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;/table&gt; &lt;/details&gt;  |  -  |
**401** | &lt;details&gt; &lt;summary&gt;Error Codes&lt;/summary&gt; &lt;table border&#x3D;\&quot;1\&quot;&gt; &lt;tr&gt;&lt;th&gt;Code&lt;/th&gt;&lt;th&gt;Message&lt;/th&gt;&lt;th&gt;Description&lt;/th&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;0110&lt;/td&gt;&lt;td&gt;Require access token.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;アクセストークンがリクエストヘッダに存在していません。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;There is no access token in the request header.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;0111&lt;/td&gt;&lt;td&gt;Authentication failed.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;アクセストークンの認証に失敗しました。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The access token authentication failed.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;0112&lt;/td&gt;&lt;td&gt;Account not found.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;アカウントが見つかりませんでした。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The account can not found.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;0113&lt;/td&gt;&lt;td&gt;Deactivated account.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;アカウントが無効です。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The account is deactivated.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;/table&gt; &lt;/details&gt;  |  -  |
**400** | &lt;details&gt; &lt;summary&gt;Error Codes&lt;/summary&gt; &lt;table border&#x3D;\&quot;1\&quot;&gt; &lt;tr&gt;&lt;th&gt;Code&lt;/th&gt;&lt;th&gt;Message&lt;/th&gt;&lt;th&gt;Description&lt;/th&gt;&lt;/tr&gt; &lt;tr&gt;&lt;td&gt;0114&lt;/td&gt;&lt;td&gt;Invalid scope.&lt;/td&gt;&lt;td&gt;&lt;div lang&#x3D;\&quot;ja\&quot;&gt;アクセストークンが無効です。&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;The access token is invalid.&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt; &lt;/table&gt; &lt;/details&gt;  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


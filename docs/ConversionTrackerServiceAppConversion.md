# ConversionTrackerServiceAppConversion

<div lang=\"ja\">ConversionTrackerServiceAppConversionオブジェクトは、アプリコンバージョン測定タグやタグごとのパフォーマンスデータなどのアプリコンバージョントラッカー情報を表します。<br> このフィールドは、ADDおよびSET時に省略可能となります。<br> ※ADD時、conversionTrackerTypeがAPP_CONVERSIONの場合は必須です。</div> <div lang=\"en\">ConversionTrackerServiceAppConversion object describes the App ConversionTracker information such as App ConversionTag and performance data by  tag.<br> This field is optional in ADD and SET operation.<br> *If the conversionTrackerType is APP_CONVERSION, this field will be required in ADD operation.</div> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_conversion_type** | [**ConversionTrackerServiceAppConversionType**](ConversionTrackerServiceAppConversionType.md) |  | [optional] 
**app_id** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;アプリケーションIDです。&lt;br&gt; このフィールドは、いずれの場合でも省略可能となります。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Application ID.&lt;br&gt; This field is optional in any cases.&lt;/div&gt;  | [optional] 
**app_platform** | [**ConversionTrackerServiceAppPlatform**](ConversionTrackerServiceAppPlatform.md) |  | [optional] 
**app_postback_url** | [**ConversionTrackerServiceAppPostbackUrl**](ConversionTrackerServiceAppPostbackUrl.md) |  | [optional] 
**snippet_id** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;コンバージョンIDです。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Converison ID&lt;/div&gt;  | [optional] 
**snippet_label** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;コンバージョントラッカーラベルです。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Converison tracker label&lt;/div&gt;  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



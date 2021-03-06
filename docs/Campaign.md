# Campaign

<div lang=\"ja\">Campaignオブジェクトは、キャンペーンの情報を表します。</div> <div lang=\"en\">Campaign object describes Campaign information.</div> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;アカウントIDです。&lt;br&gt; このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Account ID.&lt;br&gt; Although this field will be returned in the response, it will be ignored on input.&lt;/div&gt;  | [optional] 
**app_id** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;アプリID（iOS）またはパッケージ名（Android）です。&lt;br&gt; ※アプリキャンペーンでiOSの場合、入力は数値のみです。&lt;br&gt; ADD時、campaignTypeがSTANDARD、またはDYNAMIC_ADS_FOR_SEARCH_SETTINGの場合、無視され、MOBILE_APPの場合、必須となります。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;App ID (for iOS) or Package name (for Android).&lt;br&gt; *Input only the numbers for iOS in Mobile App Campaign.&lt;br&gt;  In ADD operation, this field will be ignored when campaignType is &#39;STANDARD&#39; or &#39;DYNAMIC_ADS_FOR_SEARCH_SETTING&#39;, and is required when campaignType is MOBILE_APP.&lt;/div&gt;  | [optional] 
**app_store** | [**CampaignServiceAppStore**](CampaignServiceAppStore.md) |  | [optional] 
**bidding_strategy_configuration** | [**CampaignServiceBiddingStrategy**](CampaignServiceBiddingStrategy.md) |  | [optional] 
**bidding_strategy_failed_reason** | [**CampaignServiceBiddingStrategyFailedReason**](CampaignServiceBiddingStrategyFailedReason.md) |  | [optional] 
**budget** | [**CampaignServiceBudget**](CampaignServiceBudget.md) |  | [optional] 
**campaign_id** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;キャンペーンIDです。&lt;br&gt; SET時およびREMOVE時、このフィールドは必須です。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Campaign ID.&lt;br&gt; This field is required in SET and REMOVE operation.&lt;/div&gt;  | [optional] 
**campaign_name** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;キャンペーン名です。&lt;br&gt;このフィールドは、ADD時に必須となり、SET時に省略可能となります。&lt;br&gt; ※入力制限：50文字以内です。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Campaign name.&lt;br&gt; *Insert limit: Up to 50 characters.&lt;br&gt;This field is required in ADD operation, and will be optional in SET operation.&lt;/div&gt;  | [optional] 
**campaign_track_id** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;トラッキング用キャンペーンIDです。&lt;br&gt; このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Campaign ID for tracking.&lt;br&gt; Although this field will be returned in the response, it will be ignored on input.&lt;/div&gt;  | [optional] 
**conversion_optimizer_eligibility** | [**CampaignServiceConversionOptimizerEligibility**](CampaignServiceConversionOptimizerEligibility.md) |  | [optional] 
**custom_parameters** | [**CampaignServiceCustomParameters**](CampaignServiceCustomParameters.md) |  | [optional] 
**end_date** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;キャンペーンの終了日です。&lt;br&gt; ADD時およびSET時、このフィールドは省略可能となります。ADD時のデフォルト設定値は20371231となります。&lt;br&gt; 過去の日付、開始日以前の日付は指定できません。&lt;br&gt;※YYYYMMDD形式です。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;End date of Campaign.&lt;br&gt; This field is optional in ADD and SET operation. The default value in ADD operation will be 20371231.&lt;br&gt; *Cannot set the past date and date before the start date.&lt;br&gt; *In YYYYMMDD format.&lt;/div&gt;  | [optional] 
**failed_bidding_strategy_configuration** | [**CampaignServiceBiddingStrategy**](CampaignServiceBiddingStrategy.md) |  | [optional] 
**labels** | [**list[CampaignServiceLabel]**](CampaignServiceLabel.md) |  | [optional] 
**serving_status** | [**CampaignServiceServingStatus**](CampaignServiceServingStatus.md) |  | [optional] 
**settings** | [**list[CampaignServiceSettings]**](CampaignServiceSettings.md) |  | [optional] 
**start_date** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;キャンペーンの開始日です。&lt;br&gt; ADD時およびSET時、このフィールドは省略可能となります。ADD時のデフォルト設定値は当日日付となります。&lt;br&gt; 過去の日付は指定できません。&lt;br&gt;※配信開始済みのキャンペーンは変更できません。&lt;br&gt; ※YYYYMMDD形式です。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Start date of Campaign.&lt;br&gt; This field is optional in ADD and SET operation. The default value in ADD operation will be Today&#39;s date.&lt;br&gt; *Cannot set the past date.&lt;br&gt;*Cannot change the date to the campaign that is already active.&lt;br&gt; *In YYYYMMDD format.&lt;/div&gt;  | [optional] 
**tracking_url** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;トラッキングURLです。&lt;br&gt; ADD時およびSET時、このフィールドは省略可能となります。&lt;br&gt; ※アプリキャンペーンがAndroidの場合、設定はできません。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Tracking URL.&lt;br&gt; This field is optional in ADD and SET operation.&lt;br&gt; *Cannot set if Mobile App Campaign is in Android.&lt;/div&gt;  | [optional] 
**type** | [**CampaignServiceType**](CampaignServiceType.md) |  | [optional] 
**url_review_data** | [**CampaignServiceUrlReviewData**](CampaignServiceUrlReviewData.md) |  | [optional] 
**user_status** | [**CampaignServiceUserStatus**](CampaignServiceUserStatus.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# CampaignTargetServiceLocationTarget

<div lang=\"ja\">CampaignTargetServiceLocationTargetオブジェクトは、地域ターゲティング設定です。<br> このフィールドは、ADDおよびSET時に省略可能となります。<br> ※targetTypeがLOCATIONの場合、このフィールドはADD時に必須となります。</div> <div lang=\"en\">CampaignTargetServiceLocationTarget object is a location target setting.<br> This field is optional in ADD and SET operation.<br> *If targetType is LOCATION,  this field is required in ADD operation.</div> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**city_name_en** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;市区町村名（英語）です。&lt;br&gt; このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;City(English).&lt;br&gt; Although this field will be returned in the response, it will be ignored on input.&lt;/div&gt;  | [optional] 
**city_name_ja** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;市区町村名（日本語）です。&lt;br&gt; このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;City(Japanese).&lt;br&gt; Although this field will be returned in the response, it will be ignored on input.&lt;/div&gt;  | [optional] 
**excluded_type** | [**CampaignTargetServiceExcludedType**](CampaignTargetServiceExcludedType.md) |  | [optional] 
**province_name_en** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;都道府県名（英語）です。&lt;br&gt; このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Prefecture(English).&lt;br&gt; Although this field will be returned in the response, it will be ignored on input.&lt;/div&gt;  | [optional] 
**province_name_ja** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;都道府県名（日本語）です。&lt;br&gt; このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Prefecture(Japanese).&lt;br&gt; Although this field will be returned in the response, it will be ignored on input.&lt;/div&gt;  | [optional] 
**targeting_status** | [**CampaignTargetServiceTargetingStatus**](CampaignTargetServiceTargetingStatus.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



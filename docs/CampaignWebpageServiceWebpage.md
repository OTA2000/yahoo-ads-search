# CampaignWebpageServiceWebpage

<div lang=\"ja\">CampaignWebpageServiceWebpageオブジェクトは、除外設定するCampaignWebpageServiceWebpageの条件を保持します。<br> このフィールドは、いずれの場合でも必須となります。</div> <div lang=\"en\">CampaignWebpageServiceWebpage object contains the rules of webpage to be excluded.<br> This field is required in any cases.</div> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parameter** | [**CampaignWebpageServiceWebpageParameter**](CampaignWebpageServiceWebpageParameter.md) |  | [optional] 
**target_id** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;CampaignWebpageServiceWebpageを識別するIDです。 &lt;br&gt; このフィールドは、REMOVE時に必須となり、ADD時は無視されます。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Unique ID for each webpage.&lt;br&gt; This field is required in REMOVE operation, and will be ignored in ADD operation.&lt;/div&gt;  | [optional] 
**target_track_id** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;CampaignWebpageServiceWebpageを識別するトラッキングIDです。&lt;br&gt; このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Unique tracking ID for each CampaignWebpageServiceWebpage.&lt;br&gt; Although this field will be returned in the response, it will be ignored on input.&lt;/div&gt;  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# CampaignWebpage

<div lang=\"ja\">CampaignWebpageオブジェクトは、キャンペーンに関連付けた除外設定の情報を保持します。</div> <div lang=\"en\">CampaignWebpage object contains information of excluded settings setup to campaign.</div> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;アカウントIDです。&lt;br&gt; このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Account ID.&lt;br&gt; Although this field will be returned in the response, it will be ignored on input.&lt;/div&gt;  | [optional] 
**campaign_id** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;キャンペーンIDです。&lt;br&gt; このフィールドは、いずれの場合でも必須となります。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Campaign ID.&lt;br&gt; This field is required in any cases.&lt;/div&gt;  | [optional] 
**campaign_track_id** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;キャンペーントラッキングIDです。&lt;br&gt; このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Campaign Tracking ID.&lt;br&gt; Although this field will be returned in the response, it will be ignored on input.&lt;/div&gt;  | [optional] 
**webpage** | [**CampaignWebpageServiceWebpage**](CampaignWebpageServiceWebpage.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



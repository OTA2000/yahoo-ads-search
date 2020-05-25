# AdGroupWebpage

<div lang=\"ja\">AdGroupWebpageオブジェクトは、広告グループに関連付けた配信/除外設定の情報を保持します。</div> <div lang=\"en\">AdGroupWebpage object contains information of allowed or excluded settings setup to adgroup.</div> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;アカウントIDです。&lt;br&gt;このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Account ID.&lt;br&gt;Although this field will be returned in the response, it will be ignored on input.&lt;/div&gt;  | [optional] 
**ad_group_id** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;広告グループIDです。&lt;br&gt;このフィールドは、いずれの場合でも必須です。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Ad Group ID.&lt;br&gt;This field is required in any cases.&lt;/div&gt;  | [optional] 
**ad_group_track_id** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;広告グループトラッキングIDです。&lt;br&gt;このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Ad Group Tracking ID.&lt;br&gt;Although this field will be returned in the response, it will be ignored on input.&lt;/div&gt;  | [optional] 
**bid** | [**AdGroupWebpageServiceBid**](AdGroupWebpageServiceBid.md) |  | [optional] 
**campaign_id** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;キャンペーンIDです。&lt;br&gt;このフィールドは、いずれの場合でも必須です。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Campaign ID.&lt;br&gt;This field is required in any cases.&lt;/div&gt;  | [optional] 
**campaign_track_id** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;キャンペーントラッキングIDです。&lt;br&gt;このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Campaign Tracking ID.&lt;br&gt;Although this field will be returned in the response, it will be ignored on input.&lt;/div&gt;  | [optional] 
**excluded_type** | [**AdGroupWebpageServiceExcludedType**](AdGroupWebpageServiceExcludedType.md) |  | [optional] 
**user_status** | [**AdGroupWebpageServiceUserStatus**](AdGroupWebpageServiceUserStatus.md) |  | [optional] 
**webpage** | [**AdGroupWebpageServiceWebpage**](AdGroupWebpageServiceWebpage.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# AdGroupWebpageServiceWebpage

<div lang=\"ja\">AdGroupWebpageServiceWebpageオブジェクトは、配信/除外設定するAdGroupWebpageServiceWebpageの条件を保持します。<br> このフィールドは、いずれの場合でも必須です。</div> <div lang=\"en\">AdGroupWebpageServiceWebpage object contains the rules of webpage to be allowed or excluded.<br> This field is required in any cases.</div> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parameter** | [**AdGroupWebpageServiceWebpageParameter**](AdGroupWebpageServiceWebpageParameter.md) |  | [optional] 
**target_id** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;AdGroupWebpageServiceWebpageを識別するIDです。&lt;br&gt;このフィールドは、ADD時は無視され、SET時は必須となります。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Unique ID for each identify webpage.&lt;br&gt;This field will be ignored in ADD operation, and is required in SET operation.&lt;/div&gt;  | [optional] 
**target_track_id** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;AdGroupWebpageServiceWebpageを識別するトラッキングIDです。&lt;br&gt;このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Tracking ID for each identify webpage.&lt;br&gt;Although this field will be returned in the response, it will be ignored on input.&lt;/div&gt;  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



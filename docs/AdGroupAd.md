# AdGroupAd

<div lang=\"ja\">AdGroupAdオブジェクトは、広告に関する操作を行うための情報を表します。</div> <div lang=\"en\">AdGroupAd object describes information for operations on ads.</div> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;アカウントIDです。&lt;br&gt; このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Account ID.&lt;br&gt; Although this field will be returned in the response, it will be ignored on input.&lt;/div&gt;  | [optional] 
**ad** | [**AdGroupAdServiceAd**](AdGroupAdServiceAd.md) |  | [optional] 
**ad_group_id** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;広告グループIDです。&lt;br&gt; このフィールドは、いずれの場合でも必須となります。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Ad group ID.&lt;br&gt; This field is required in any cases.&lt;/div&gt;  | [optional] 
**ad_group_name** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;広告グループ名です。&lt;br&gt; このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Ad group name.&lt;br&gt; Although this field will be returned in the response, it will be ignored on input.&lt;/div&gt;  | [optional] 
**ad_group_track_id** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;トラッキング用広告グループIDです。&lt;br&gt; このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Ad group ID for tracking.&lt;br&gt; Although this field will be returned in the response, it will be ignored on input.&lt;/div&gt;  | [optional] 
**ad_id** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;広告IDです。&lt;br&gt; SETおよびREMOVE時、このフィールドは必須となります。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Ad ID.&lt;br&gt; This field is required in SET and REMOVE operation.&lt;/div&gt;  | [optional] 
**ad_name** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;広告名です。&lt;br&gt; このフィールドは、ADD時は必須となり、SET時は省略可能となります。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Ad name.&lt;br&gt; This field is required in ADD operation, and will be optional in SET operation.&lt;/div&gt;  | [optional] 
**ad_track_id** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;トラッキング用広告IDです。&lt;br&gt; このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Ad ID for tracking.&lt;br&gt; Although this field will be returned in the response, it will be ignored on input.&lt;/div&gt;  | [optional] 
**approval_status** | [**AdGroupAdServiceApprovalStatus**](AdGroupAdServiceApprovalStatus.md) |  | [optional] 
**campaign_id** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;キャンペーンIDです。&lt;br&gt; このフィールドは、いずれの場合でも必須となります。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Campaign ID.&lt;br&gt; This field is required in any cases.&lt;/div&gt;  | [optional] 
**campaign_name** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;キャンペーン名です。&lt;br&gt; このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Campaign name.&lt;br&gt; Although this field will be returned in the response, it will be ignored on input.&lt;/div&gt;  | [optional] 
**campaign_track_id** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;トラッキング用キャンペーンIDです。&lt;br&gt; このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Campaign ID for tracking.&lt;br&gt; Although this field will be returned in the response, it will be ignored on input.&lt;/div&gt;  | [optional] 
**disapproval_reason_codes** | **list[str]** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;審査否認の理由コードです。&lt;br&gt; (コード詳細は、DictionaryServiceのgetDisapprovalReasonのレスポンスを参照)&lt;br&gt; このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Code of Disapproval reason.&lt;br&gt; (Refer to DictionaryService getDisapprovalReason response for details) &lt;br&gt; Although this field will be returned in the response, it will be ignored on input.&lt;/div&gt;  | [optional] 
**feed_id** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;フィードIDです。&lt;br&gt; このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Feed ID.&lt;br&gt; Although this field will be returned in the response, it will be ignored on input.&lt;/div&gt;  | [optional] 
**invalided_trademarks** | **list[str]** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;制限された商標です。&lt;br&gt; このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Invalided trademarks.&lt;br&gt; Although this field will be returned in the response, it will be ignored on input.&lt;/div&gt;  | [optional] 
**labels** | [**list[AdGroupAdServiceLabel]**](AdGroupAdServiceLabel.md) |  | [optional] 
**trademark_status** | [**AdGroupAdServiceTrademarkStatus**](AdGroupAdServiceTrademarkStatus.md) |  | [optional] 
**user_status** | [**AdGroupAdServiceUserStatus**](AdGroupAdServiceUserStatus.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



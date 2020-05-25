# AccountTrackingUrl

<div lang=\"ja\">AccountTrackingUrlオブジェクトは、アカウントトラッキングの情報を表します。</div> <div lang=\"en\">AccountTrackingUrl object describes account tracking information.</div> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;アカウントIDです。&lt;br&gt; SET時、このフィールドは必須となります。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Account ID.&lt;br&gt; This field is required in SET operation.&lt;/div&gt;  | [optional] 
**account_name** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;アカウント名です。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Account name.&lt;/div&gt;  | [optional] 
**disapproval_reason_codes** | **list[str]** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;審査否認理由コードです。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Code of disapproval reason.&lt;/div&gt;  | [optional] 
**disapproval_review_url** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;審査否認されたトラッキングURLです。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Tracking URL that has been disapproved.&lt;/div&gt;  | [optional] 
**in_review_url** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;審査中のトラッキングURLです。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Tracking URL that is in review.&lt;/div&gt;  | [optional] 
**tracking_url** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;トラッキングURLです。&lt;br&gt; SET時、このフィールドは省略可能となります。&lt;br&gt; ※空で設定すると、既存のトラッキングURLは削除されます。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Tracking URL.&lt;br&gt; this field is optional in SET operation.&lt;br&gt; *When tag is set blank, existing Tracking URL will be deleted.&lt;/div&gt;  | [optional] 
**url_approval_status** | [**AccountTrackingUrlServiceUrlApprovalStatus**](AccountTrackingUrlServiceUrlApprovalStatus.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# AdGroupCriterionServiceAdditionalUrl

<div lang=\"ja\">AdGroupCriterionServiceAdditionalUrlオブジェクトは、追加する最終リンク先URLを保持します。<br> このフィールドは、ADD時は必須となり、SET時は省略可能となります。</div> <div lang=\"en\">AdGroupCriterionServiceAdditionalUrl object holds additional Landing Page URLs.<br> This field is required in ADD operation, and will be optional in SET operation.</div> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disapproval_reason_codes** | **list[str]** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;審査否認理由のコードです。&lt;br&gt; (コード詳細は、DictionaryServiceのgetDisapprovalReasonのレスポンスを参照)&lt;br&gt; このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Reject reason code.&lt;br&gt; (Refer to DictionaryService getDisapprovalReason response for details) &lt;br&gt; Although this field will be returned in the response, it will be ignored on input.&lt;/div&gt;  | [optional] 
**review_url** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;審査中の最終リンク先URLです。&lt;br&gt; このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Landing Page URL in editorial review.&lt;br&gt; Although this field will be returned in the response, it will be ignored on input.&lt;/div&gt;  | [optional] 
**url** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;最終リンク先URLです。&lt;br&gt; ADDおよびSET時、このフィールドは必須となります。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Landing Page URL.&lt;br&gt; This field is required in ADD and SET operation.&lt;/div&gt;  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



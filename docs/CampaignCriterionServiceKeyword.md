# CampaignCriterionServiceKeyword

<div lang=\"ja\">CampaignCriterionServiceKeywordオブジェクトは、キーワードに関する情報を表します。<br> ADD時、このフィールドは省略可能です。※criterionTypeがKEYWORDの場合、必須です。</div> <div lang=\"en\">CampaignCriterionServiceKeyword object displays keyword information.<br> This field is optional in ADD operation. *This field is required when criterionType is 'KEYWORD'.</div> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keyword_match_type** | [**CampaignCriterionServiceKeywordMatchType**](CampaignCriterionServiceKeywordMatchType.md) |  | [optional] 
**text** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;キーワードの内容です。&lt;br&gt; ADD時、このフィールドは必須です。&lt;br&gt; ※最大80文字、10ワードです。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;CampaignCriterionServiceKeyword element.&lt;br&gt; This field is required in ADD operation.&lt;br&gt; * Maximum of 80 letters, 10 word.&lt;/div&gt;  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



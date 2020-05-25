# SharedCriterion

<div lang=\"ja\">SharedCriterionオブジェクトは、対象外キーワード情報を保持します。</div> <div lang=\"en\">SharedCriterion object holds negative keyword information.</div> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;アカウントIDです。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Account ID.&lt;/div&gt;  | [optional] 
**criterion_id** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;クライテリオンIDです。&lt;br&gt; REMOVE時、このフィールドは必須となります。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Criterion ID.&lt;br&gt; This field is required in REMOVE operation.&lt;/div&gt;  | [optional] 
**keyword_match_type** | [**SharedCriterionServiceKeywordMatchType**](SharedCriterionServiceKeywordMatchType.md) |  | [optional] 
**shared_list_id** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;アカウント共有リストIDです。&lt;br&gt; ADDおよびREMOVE時、このフィールドは必須となります。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Account shared list ID.&lt;br&gt; This field is required in ADD and REMOVE operation.&lt;/div&gt;  | [optional] 
**text** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;キーワードです。&lt;br&gt; ADD時、このフィールドは必須となります。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Keyword.&lt;br&gt;This field is required in ADD operation.&lt;/div&gt;  | [optional] 
**use** | [**SharedCriterionServiceUse**](SharedCriterionServiceUse.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



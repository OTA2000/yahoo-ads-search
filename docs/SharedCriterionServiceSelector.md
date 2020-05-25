# SharedCriterionServiceSelector

<div lang=\"ja\">SharedCriterionServiceSelectorオブジェクトは、検索条件を保持します。</div> <div lang=\"en\">SharedCriterionServiceSelector object holds search criteria.</div> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;アカウントIDです。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Account ID&lt;/div&gt;  | 
**criterion_ids** | **list[int]** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;クライテリオンIDです。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Criterion ID.&lt;/div&gt;  | [optional] 
**number_results** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;ページの最大件数です。このフィールドは、1以上を指定する必要があります。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Maximum number of results to return in this page. This field must be greater than or equal to 1. Also see Entity Limits per operation.&lt;/div&gt;  | [optional] [default to 1000]
**shared_list_ids** | **list[int]** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;共有リストのIDです。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Share list ID.&lt;/div&gt;  | [optional] 
**start_index** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;ページの先頭のインデックスです。このフィールドは、1以上を指定する必要があります。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Index of the first result to return in this page. This field must be greater than or equal to 1.&lt;/div&gt;  | [optional] [default to 1]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



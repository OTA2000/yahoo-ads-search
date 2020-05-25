# PageFeedItemServiceJobStatusSelector

<div lang=\"ja\">PageFeedItemServiceJobStatusSelectorオブジェクトは、upload、downloadの処理状況を取得するための検索条件を格納します。</div> <div lang=\"en\">PageFeedItemServiceJobStatusSelector object retains search condition for The processing situation upload/download.</div> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;アカウントID&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Account ID&lt;/div&gt;  | 
**job_ids** | **list[int]** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;登録したジョブのID&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Registered job ID&lt;/div&gt;  | [optional] 
**job_type** | [**PageFeedItemServiceJobType**](PageFeedItemServiceJobType.md) |  | 
**number_results** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;ページの最大件数です。このフィールドは、1以上を指定する必要があります。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Maximum number of results to return in this page. This field must be greater than or equal to 1. Also see Entity Limits per operation.&lt;/div&gt;  | [optional] [default to 500]
**start_index** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;ページの先頭のインデックスです。このフィールドは、1以上を指定する必要があります。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Index of the first result to return in this page. This field must be greater than or equal to 1.&lt;/div&gt;  | [optional] [default to 1]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



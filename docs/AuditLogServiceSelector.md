# AuditLogServiceSelector

<div lang=\"ja\">AuditLogServiceSelectorオブジェクトは、登録したジョブを照会するための検索条件を保持します。</div> <div lang=\"en\">AuditLogServiceSelector object retains search criterias to inquire a created job.</div> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;アカウントIDです。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Account ID&lt;/div&gt;  | 
**job_ids** | **list[int]** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;登録したジョブのIDです。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Created job ID&lt;/div&gt;  | [optional] 
**job_statuses** | [**list[AuditLogServiceJobStatus]**](AuditLogServiceJobStatus.md) |  | [optional] 
**number_results** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;ページの最大件数です。このフィールドは、1以上を指定する必要があります。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Maximum number of results to return in this page. This field must be greater than or equal to 1. Also see Entity Limits per operation.&lt;/div&gt;  | [optional] [default to 500]
**start_index** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;ページの先頭のインデックスです。このフィールドは、1以上を指定する必要があります。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Index of the first result to return in this page. This field must be greater than or equal to 1.&lt;/div&gt;  | [optional] [default to 1]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



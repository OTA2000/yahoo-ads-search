# AuditLogServiceJob

<div lang=\"ja\">AuditLogServiceJobオブジェクトは、操作履歴取得で登録するジョブの情報を保持します。</div> <div lang=\"en\">AuditLogServiceJob object retains the job information to be added for getting operation history data.</div> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;アカウントIDです。&lt;br&gt;このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Account ID.&lt;br&gt;Although this field will be returned in the response, it will be ignored on input.&lt;/div&gt;  | [optional] 
**date_range** | [**AuditLogServiceDateRange**](AuditLogServiceDateRange.md) |  | [optional] 
**encoding** | [**AuditLogServiceEncoding**](AuditLogServiceEncoding.md) |  | [optional] 
**event_selector** | [**list[AuditLogServiceEventSelector]**](AuditLogServiceEventSelector.md) |  | 
**job_id** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;ジョブIDです。&lt;br&gt;このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Job ID.&lt;br&gt;Although this field will be returned in the response, it will be ignored on input.&lt;/div&gt;  | [optional] 
**job_name** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;ジョブ名です。&lt;br&gt;このフィールドは、省略可能となります。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Name of job.&lt;br&gt;This field is optional.&lt;/div&gt;  | [optional] 
**job_status** | [**AuditLogServiceJobStatus**](AuditLogServiceJobStatus.md) |  | [optional] 
**lang** | [**AuditLogServiceLang**](AuditLogServiceLang.md) |  | [optional] 
**output** | [**AuditLogServiceOutput**](AuditLogServiceOutput.md) |  | [optional] 
**source_type** | [**AuditLogServiceSourceType**](AuditLogServiceSourceType.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



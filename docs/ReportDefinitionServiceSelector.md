# ReportDefinitionServiceSelector

<div lang=\"ja\">ReportDefinitionServiceSelectorオブジェクトは、操作の対象とするレポートです。</div> <div lang=\"en\">ReportDefinitionServiceSelector is a detail of requested report.</div> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;検索条件： アカウントIDです。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Search condition: Account ID.&lt;/div&gt;  | 
**number_results** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;ページの最大件数です。このフィールドは、1以上を指定する必要があります。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Maximum number of results to return in this page. This field must be greater than or equal to 1. Also see Entity Limits per operation.&lt;/div&gt;  | [optional] [default to 500]
**report_job_ids** | **list[int]** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;検索条件： レポートジョブIDです。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Search condition: Report Job ID.&lt;/div&gt;  | [optional] 
**report_job_statuses** | [**list[ReportDefinitionServiceReportJobStatus]**](ReportDefinitionServiceReportJobStatus.md) |  | [optional] 
**report_types** | [**list[ReportDefinitionServiceReportType]**](ReportDefinitionServiceReportType.md) |  | [optional] 
**start_index** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;ページの先頭のインデックスです。このフィールドは、1以上を指定する必要があります。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Index of the first result to return in this page. This field must be greater than or equal to 1.&lt;/div&gt;  | [optional] [default to 1]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



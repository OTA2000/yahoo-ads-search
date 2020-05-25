# ReportDefinitionServiceReportFilter

<div lang=\"ja\">ReportDefinitionServiceReportFilterオブジェクトは、レポートのフィルタ条件を表します。フィルタ条件は最大6つまで設定が可能です。<br> ADD時、このフィールドは省略可能となります。 </div> <div lang=\"en\">ReportDefinitionServiceReportFilter object displays filtering report conditions. Filter condition can set up to 6.<br> This field is optional in ADD operation.</div> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;フィルタ条件を設定する表示項目です。&lt;br&gt; ADD時、このフィールドは必須となります。 &lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Field which you set filtering.&lt;br&gt; This field is required in ADD operation.&lt;/div&gt;  | [optional] 
**report_operator** | [**ReportDefinitionServiceReportOperator**](ReportDefinitionServiceReportOperator.md) |  | [optional] 
**value** | **list[str]** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;表示項目の条件値です。&lt;br&gt; ADD時、このフィールドは必須となります。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Condition values to filter the field.&lt;br&gt; This field is required in ADD operation.&lt;/div&gt;  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



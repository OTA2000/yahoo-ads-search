# ReportDefinitionServiceReportFieldAttribute

<div lang=\"ja\">ReportDefinitionServiceReportFieldAttributeオブジェクトは、レポート定義の作成に使用できるフィールドを表します。</div> <div lang=\"en\">ReportDefinitionServiceReportFieldAttribute object describes the available field to create report definition.</div> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**can_filter** | **bool** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;ユーザーがこのフィールドにフィルタを 適用できるかどうかを示します。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Indicate if use can filter the fields.&lt;/div&gt;  | [optional] 
**can_select** | **bool** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;ユーザーがこのフィールドを 選択できるかどうかを示します。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Indicate if user can select the fields.&lt;/div&gt;  | [optional] 
**display_field_name_en** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;ダウンロードされたレポートに 表示される英語名です。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Field name displayed in downloaded report (in English).&lt;/div&gt;  | [optional] 
**display_field_name_ja** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;ダウンロードされたレポートに 表示される日本語名です。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Field name displayed in downloaded report (in Japanese).&lt;/div&gt;  | [optional] 
**field_name** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;フィールド名です。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Field name.&lt;/div&gt;  | [optional] 
**field_type** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;フィールドの種類です。&lt;br&gt; 数字、文字列、Enum値等を表します。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Type of field.&lt;br&gt; Displays int, string, Enum, etc.&lt;/div&gt;  | [optional] 
**impossible_combination_fields** | **list[str]** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;組み合わせができないレポートフィールドです。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Report fields which cannot be combined.&lt;/div&gt;  | [optional] 
**xml_attribute_name** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;ダウンロードしたレポートの XMLアトリビュートです。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;XML attribute name displayed in downloaded report.&lt;/div&gt;  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



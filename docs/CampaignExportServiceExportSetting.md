# CampaignExportServiceExportSetting

<div lang=\"ja\">CampaignExportServiceExportSetting オブジェクトは、エクスポートする条件を表します。</div> <div lang=\"en\">CampaignExportServiceExportSetting object describes the condition for exports.</div> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;アカウントIDです。&lt;br&gt;このフィールドは、必須です。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Account ID.&lt;br&gt;This field is required.&lt;/div&gt;  | 
**ad_group_ad_approval_statuses** | [**list[CampaignExportServiceApprovalStatus]**](CampaignExportServiceApprovalStatus.md) |  | [optional] 
**ad_group_ad_user_statuses** | [**list[CampaignExportServiceUserStatus]**](CampaignExportServiceUserStatus.md) |  | [optional] 
**ad_group_criterion_approval_statuses** | [**list[CampaignExportServiceApprovalStatus]**](CampaignExportServiceApprovalStatus.md) |  | [optional] 
**ad_group_criterion_ids** | **list[int]** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;広告グループクライテリアIDです。&lt;br&gt;このフィールドは、省略可能となります。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Ad group criteria ID.&lt;br&gt;This field is optional.&lt;/div&gt;  | [optional] 
**ad_group_criterion_user_statuses** | [**list[CampaignExportServiceUserStatus]**](CampaignExportServiceUserStatus.md) |  | [optional] 
**ad_group_ids** | **list[int]** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;ダウンロード対象の広告グループIDです。&lt;br&gt; このフィールドは、省略可能となります。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Ad group ID of export objective.&lt;br&gt; This field is optional.&lt;/div&gt;  | [optional] 
**ad_group_user_statuses** | [**list[CampaignExportServiceUserStatus]**](CampaignExportServiceUserStatus.md) |  | [optional] 
**ad_ids** | **list[int]** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;ダウンロード対象の広告IDです。&lt;br&gt; このフィールドは、省略可能となります。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Ad ID of export objective.&lt;br&gt; This field is optional.&lt;/div&gt;  | [optional] 
**campaign_criterion_ids** | **list[int]** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;キャンペーンクライテリアIDです。&lt;br&gt; このフィールドは、省略可能となります。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Campaign criteria ID.&lt;br&gt; This field is optional.&lt;/div&gt;  | [optional] 
**campaign_ids** | **list[int]** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;ダウンロード対象のキャンペーンIDです。&lt;br&gt; このフィールドは、省略可能となります。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Campaign ID of export objective.&lt;br&gt; This field is optional.&lt;/div&gt;  | [optional] 
**campaign_user_statuses** | [**list[CampaignExportServiceUserStatus]**](CampaignExportServiceUserStatus.md) |  | [optional] 
**encoding** | [**CampaignExportServiceEncoding**](CampaignExportServiceEncoding.md) |  | [optional] 
**entity_types** | [**list[CampaignExportServiceEntityType]**](CampaignExportServiceEntityType.md) |  | [optional] 
**export_fields** | **list[str]** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;エクスポートするフィールドを指定します。&lt;br&gt; このフィールドは、省略可能となります。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Select which field to export.&lt;br&gt; This field is optional.&lt;/div&gt;  | [optional] 
**job_name** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;ダウンロードするジョブの名称です。&lt;br&gt; このフィールドは、省略可能となります。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Job information for export.&lt;br&gt; This field is optional.&lt;/div&gt;  | [optional] 
**lang** | [**CampaignExportServiceLang**](CampaignExportServiceLang.md) |  | [optional] 
**output** | [**CampaignExportServiceOutput**](CampaignExportServiceOutput.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



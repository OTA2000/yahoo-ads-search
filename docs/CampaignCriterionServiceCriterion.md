# CampaignCriterionServiceCriterion

<div lang=\"ja\">CampaignCriterionServiceCriterionオブジェクトは、クライテリアを表します。※キャンペーン用クライテリアです。<br> ADD時およびREMOVE時、このフィールドは必須です。</div> <div lang=\"en\">CampaignCriterionServiceCriterion object describes criteria information. *This is a criteria for campaign.<br> This field is required in ADD and REMOVE operation.</div> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**criterion_id** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;クライテリアIDです。&lt;br&gt; REMOVE時、このフィールドは必須です。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;CampaignCriterionServiceCriterion ID.&lt;br&gt; This field is required in REMOVE operation.&lt;/div&gt;  | [optional] 
**criterion_track_id** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;クライテリオントラックIDです。&lt;br&gt; 対象外キーワードでは返却されません。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;CampaignCriterionServiceCriterion Track ID.&lt;br&gt; This is not returned for Negative keyword.&lt;/div&gt;  | [optional] 
**criterion_type** | [**CampaignCriterionServiceCriterionType**](CampaignCriterionServiceCriterionType.md) |  | [optional] 
**keyword** | [**CampaignCriterionServiceKeyword**](CampaignCriterionServiceKeyword.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# CampaignTargetServiceTarget

<div lang=\"ja\">CampaignTargetServiceTargetオブジェクトは、ターゲティング設定を表します。<br> このフィールドは、いずれの場合でも必須となります。</div> <div lang=\"en\">CampaignTargetServiceTarget object describes CampaignTargetServiceTarget information.<br> This field is required in any cases.</div> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**location_target** | [**CampaignTargetServiceLocationTarget**](CampaignTargetServiceLocationTarget.md) |  | [optional] 
**network_target** | [**CampaignTargetServiceNetworkTarget**](CampaignTargetServiceNetworkTarget.md) |  | [optional] 
**platform_target** | [**CampaignTargetServicePlatformTarget**](CampaignTargetServicePlatformTarget.md) |  | [optional] 
**schedule_target** | [**CampaignTargetServiceScheduleTarget**](CampaignTargetServiceScheduleTarget.md) |  | [optional] 
**target_id** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;ターゲットIDです。&lt;br&gt; このフィールドは、ADD時は無視され、SETおよびREMOVE時は必須となります。&lt;br&gt; ※LocationCampaignTargetServiceTargetの場合、ADD時に必須となります。&lt;br&gt; ※PlatformCampaignTargetServiceTargetの場合、SET時に無視されます。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;CampaignTargetServiceTarget ID.&lt;br&gt; This field will be ignored in ADD operation, and is required in ADD and REMOVE operation.&lt;br&gt; *For LocationCampaignTargetServiceTarget, this is required in ADD operation.&lt;br&gt; *For PlatformCampaignTargetServiceTarget, this will be ignored in SET operation.&lt;/div&gt;  | [optional] 
**target_type** | [**CampaignTargetServiceTargetType**](CampaignTargetServiceTargetType.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



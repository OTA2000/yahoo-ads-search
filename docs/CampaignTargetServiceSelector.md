# CampaignTargetServiceSelector

<div lang=\"ja\">CampaignTargetServiceSelectorオブジェクトは、操作の対象とするキャンペーンのターゲティング設定を表します。</div> <div lang=\"en\">CampaignTargetSelector object describes the targeting settings on the campaign to be operated.</div> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;アカウントIDです。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Account ID.&lt;/div&gt;  | 
**campaign_ids** | **list[int]** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;キャンペーンIDです。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Campaign ID.&lt;/div&gt;  | [optional] 
**excluded_type** | [**CampaignTargetServiceExcludedType**](CampaignTargetServiceExcludedType.md) |  | [optional] 
**number_results** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;ページの最大件数です。このフィールドは、1以上を指定する必要があります。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Maximum number of results to return in this page. This field must be greater than or equal to 1. Also see Entity Limits per operation.&lt;/div&gt;  | [optional] [default to 500]
**platform_types** | [**list[CampaignTargetServicePlatformType]**](CampaignTargetServicePlatformType.md) |  | [optional] 
**start_index** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;ページの先頭のインデックスです。このフィールドは、1以上を指定する必要があります。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Index of the first result to return in this page. This field must be greater than or equal to 1.&lt;/div&gt;  | [optional] [default to 1]
**target_ids** | **list[str]** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;ターゲットIDです。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Target ID.&lt;/div&gt;  | [optional] 
**target_types** | [**list[CampaignTargetServiceTargetType]**](CampaignTargetServiceTargetType.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



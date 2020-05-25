# CampaignRetargetingList

<div lang=\"ja\">CampaignRetargetingListオブジェクトは、キャンペーン階層におけるターゲットリストの設定情報を保持するオブジェクトです。</div> <div lang=\"en\">CampaignRetargetingList object holds the setting information of Target List on campaign level.</div> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;アカウントIDです。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Account ID.&lt;/div&gt;  | [optional] 
**bid_multiplier** | **float** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;入札価格調整率です。&lt;br&gt;このフィールドは、いずれの場合でも省略可能となります。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Bid adjustment rate.&lt;br&gt;This field is optional in any cases.&lt;/div&gt;  | [optional] 
**campaign_id** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;キャンペーンIDです。&lt;br&gt;このフィールドは、いずれの場合でも必須です。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Campaign ID.&lt;br&gt;This field is required in any cases.&lt;/div&gt;  | [optional] 
**campaign_name** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;キャンペーン名称です。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Name of campaign.&lt;/div&gt;  | [optional] 
**criterion_target_list** | [**CampaignRetargetingListServiceCriterionTargetList**](CampaignRetargetingListServiceCriterionTargetList.md) |  | [optional] 
**excluded_type** | [**CampaignRetargetingListServiceExcludedType**](CampaignRetargetingListServiceExcludedType.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



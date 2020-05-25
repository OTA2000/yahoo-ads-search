# CampaignTarget

<div lang=\"ja\">CampaignTargetオブジェクトは、キャンペーンの各種ターゲティング設定を表します。</div> <div lang=\"en\">CampaignTarget describes each type of targeting setting of Campaign.</div> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;アカウントIDです。&lt;br&gt; このフィールドは、いずれの場合でも必須となります。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Account ID.&lt;br&gt; This field is required in any cases.&lt;/div&gt;  | [optional] 
**bid_multiplier** | **float** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;入札価格調整率です。&lt;br&gt; ADDおよびSET時、このフィールドは省略可能となります。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Bid multiplier.&lt;br&gt; This field is optional in ADD and SET operation.&lt;/div&gt;  | [optional] 
**campaign_id** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;キャンペーンIDです。&lt;br&gt; このフィールドは、いずれの場合でも必須となります。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Campaign ID.&lt;br&gt; This field is required in any cases.&lt;/div&gt;  | [optional] 
**campaign_name** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;キャンペーン名です。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Campaign Name.&lt;/div&gt;  | [optional] 
**target** | [**CampaignTargetServiceTarget**](CampaignTargetServiceTarget.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# AdGroupCriterion

<div lang=\"ja\">AdGroupCriterionオブジェクトは、広告グループのクライテリアを表します。</div> <div lang=\"en\">AdGroupCriterion object describes ad group criteria information.</div> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;アカウントIDです。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Account ID.&lt;/div&gt;  | [optional] 
**ad_group_id** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;広告グループIDです。&lt;br&gt; このフィールドは、いずれの場合でも必須となります。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Ad group ID.&lt;br&gt; This field is required in any cases.&lt;/div&gt;  | [optional] 
**ad_group_name** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;広告グループ名です。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Ad group name.&lt;/div&gt;  | [optional] 
**ad_group_track_id** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;トラッキング用広告グループIDです。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Ad group ID for tracking.&lt;/div&gt;  | [optional] 
**biddable_ad_group_criterion** | [**AdGroupCriterionServiceBiddableAdGroupCriterion**](AdGroupCriterionServiceBiddableAdGroupCriterion.md) |  | [optional] 
**campaign_id** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;キャンペーンIDです。&lt;br&gt; このフィールドは、いずれの場合でも必須となります。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Campaign ID.&lt;br&gt; This field is required in any cases.&lt;/div&gt;  | [optional] 
**campaign_name** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;キャンペーン名です。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Campaign name.&lt;/div&gt;  | [optional] 
**campaign_track_id** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;トラッキング用キャンペーンIDです。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Campaign ID for tracking.&lt;/div&gt;  | [optional] 
**criterion** | [**AdGroupCriterionServiceCriterion**](AdGroupCriterionServiceCriterion.md) |  | [optional] 
**labels** | [**list[AdGroupCriterionServiceLabel]**](AdGroupCriterionServiceLabel.md) |  | [optional] 
**use** | [**AdGroupCriterionServiceUse**](AdGroupCriterionServiceUse.md) |  | [optional] 
**trademark_status** | [**AdGroupCriterionServiceTrademarkStatus**](AdGroupCriterionServiceTrademarkStatus.md) |  | [optional] 
**invalided_trademarks** | **list[str]** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;制限された商標です。&lt;br&gt; このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。 &lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Invalided trademarks.&lt;br&gt; Although this field will be returned in the response, it will be ignored on input.&lt;/div&gt;  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# CampaignServiceTargetRoasBiddingScheme

<div lang=\"ja\">CampaignServiceTargetRoasBiddingSchemeオブジェクトは、広告費用対効果の目標値の自動入札設定情報を表します。 （BiddingStrategyService以外用のオブジェクトです。）<br> ADD時、BiddingStrategyTypeがTARGET_ROASの場合、必須となり、それ以外では省略可能となります。</div> <div lang=\"en\">CampaignServiceTargetRoasBiddingScheme object displays Auto Bidding setting for Target ROAS. *This is an object for anything other than BiddingStrategyService.<br> This field is required when BiddingStrategyType is 'TARGET_ROAS' in ADD operation. For other BiddingStrategyType, this field is optional in ADD operation.</div> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bid_ceiling** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;入札価格の上限です。&lt;br&gt;このフィールドは省略可能となります。その際、デフォルト設定値は0となります。&lt;br&gt; ※「0」が設定された場合、上限設定はありません。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Limit of bid (CPC).&lt;br&gt;This field is optional. The default value will be 0.&lt;br&gt; * No limits if &amp;#34;0&amp;#34; is set.&lt;/div&gt;  | [optional] 
**bid_floor** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;入札価格の下限です。&lt;br&gt;このフィールドは省略可能となります。その際、デフォルト設定値は0となります。&lt;br&gt; ※ 設定を解除する場合は「0」を指定します。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Minimum CPC.&lt;br&gt;This field is optional. The default value will be 0.&lt;br&gt; * Set &amp;#34;0&amp;#34; to deactivate.&lt;/div&gt;  | [optional] 
**target_roas** | **float** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;広告費用対効果の目標値です。&lt;br&gt; 0.01 ～ 1000.00（1% ～ 100000%）の範囲内のみ 許容します。&lt;br&gt; ADD時およびSET時、このフィールドは必須となります。&lt;br&gt; ※ROAS:Return On Advertising Spend&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Target ROAS (Return On Advertising Spend)&lt;br&gt; * Limit range: 0.01 - 1000.00 (1% - 100000%)&lt;br&gt; This field is required in ADD and SET operation.&lt;/div&gt;  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



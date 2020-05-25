# CampaignServiceTargetSpendBiddingScheme

<div lang=\"ja\">CampaignServiceTargetSpendBiddingSchemeオブジェクトは、クリック数の最大化の自動入札設定情報を表します。（BiddingStrategyService以外用のオブジェクトです。）<br> ADD時、BiddingStrategyTypeがTARGET_SPENDの場合、必須となり、それ以外では省略可能となります。</div> <div lang=\"en\">CampaignServiceTargetSpendBiddingScheme object describes auto bidding setting for Maximize Clicks. *This is an object for anything other than BiddingStrategyService.<br> This field is required when BiddingStrategyType is 'TARGET_SPEND' in ADD operation. For other BiddingStrategyType, this field is optional in ADD operation.</div> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bid_ceiling** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;入札価格の上限です。&lt;br&gt;※「0」が設定された 場合、上限設定は ありません。&lt;br&gt; このフィールドは省略可能となります。その際、デフォルト設定値は0となります。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Bid amount limit.&lt;br&gt;* If &amp;#34;0&amp;#34; is set, no bid limit.&lt;br&gt; This field is optional. The default value will be 0.&lt;/div&gt;  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



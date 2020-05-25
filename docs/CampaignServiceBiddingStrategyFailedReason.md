# CampaignServiceBiddingStrategyFailedReason

<div lang=\"ja\">CampaignServiceBiddingStrategyFailedReasonは、自動入札設定の結果（失敗原因）です。<br> このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。</div> <div lang=\"en\">CampaignServiceBiddingStrategyFailedReason object displays the failure reason of Auto Bidding setting.<br> Although this field will be returned in the response, it will be ignored on input.</div> <hr> <p>* <code>FAILURE</code> - <span lang=\"ja\">原因不明です。</span><span lang=\"en\">Failed [Cause unknown]</span></p> <p>* <code>CONVERSION_TRACKING_NOT_ENABLED</code> - <span lang=\"ja\">コンバージョン測定タグが発行されていません。</span><span lang=\"en\">Failed [Invalid conversion tracking]</span></p> <p>* <code>NOT_ENOUGH_CONVERSIONS</code> - <span lang=\"ja\">コンバージョンの情報が十分でありません。</span><span lang=\"en\">Failed [Not enough conversion information]</span></p> <p>* <code>CANNOT_CREATE_CAMPAIGN_WITH_CONVERSION_OPTIMIZER</code> - <span lang=\"ja\">コンバージョンオプティマイザーの情報は作成不可です。</span><span lang=\"en\">Failed [Cannot create conversion optimizer information]</span></p> <p>* <code>BIDDING_STRATEGY_CANNOT_BE_OVERRIDDEN</code> - <span lang=\"ja\">自動入札設定の上書きができません。</span><span lang=\"en\">Failed [Cannot override Auto bidding]</span></p> <p>* <code>NOT_CPC_CAMPAIGN</code> - <span lang=\"ja\">手動入札ではありません。</span><span lang=\"en\">Failed [Not CPC Campaign]</span></p> <p>* <code>UNKNOWN</code> - <span lang=\"ja\">未知の値です。</span><span lang=\"en\">Unknown Value</span></p> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



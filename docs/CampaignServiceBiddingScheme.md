# CampaignServiceBiddingScheme

<div lang=\"ja\">CampaignServiceBiddingSchemeオブジェクトは、自動入札設定の詳細情報を表します。 （BiddingStrategyService以外用のオブジェクトです。）<br> ADD時、標準入札設定の場合、このフィールドは必須となり、ポートフォリオ入札設定の場合、設定不可となります。また、biddingStrategyIdと同時に設定することはできません。</div> <div lang=\"en\">CampaignServiceBiddingScheme object displays the details of Auto Bidding setting.<br> This field is required when Standard bidding is setting, and cannot be specified when Portfolio bidding is setting in ADD operation. It cannot be specified at the same times as biddingStrategyId.</div> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bidding_strategy_type** | [**CampaignServiceBiddingStrategyType**](CampaignServiceBiddingStrategyType.md) |  | [optional] 
**manual_cpc_bidding_scheme** | [**CampaignServiceManualCpcBiddingScheme**](CampaignServiceManualCpcBiddingScheme.md) |  | [optional] 
**target_cpa_bidding_scheme** | [**CampaignServiceTargetCpaBiddingScheme**](CampaignServiceTargetCpaBiddingScheme.md) |  | [optional] 
**target_roas_bidding_scheme** | [**CampaignServiceTargetRoasBiddingScheme**](CampaignServiceTargetRoasBiddingScheme.md) |  | [optional] 
**target_spend_bidding_scheme** | [**CampaignServiceTargetSpendBiddingScheme**](CampaignServiceTargetSpendBiddingScheme.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



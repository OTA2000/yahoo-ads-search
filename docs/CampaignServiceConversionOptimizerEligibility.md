# CampaignServiceConversionOptimizerEligibility

<div lang=\"ja\">CampaignServiceConversionOptimizerEligibilityは、コンバージョンオプティマイザーが利用可能であるか判定します。<br> このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。</div> <div lang=\"en\">CampaignServiceConversionOptimizerEligibility object is to determine if it is possible to use conversion optimizer.<br> Although this field will be returned in the response, it will be ignored on input.</div> <hr> <p>* <code>ENABLE</code> - <span lang=\"ja\">利用可能です。</span><span lang=\"en\">Can use conversion optimizer.</span></p> <p>* <code>DISABLE</code> - <span lang=\"ja\">利用できません。</span><span lang=\"en\">Cannot use conversion optimizer.</span></p> <p>* <code>CAMPAIGN_IS_NOT_ACTIVE</code> - <span lang=\"ja\">キャンペーンがアクティブではありません。</span><span lang=\"en\">Campaign is not active.</span></p> <p>* <code>NOT_CPC_CAMPAIGN</code> - <span lang=\"ja\">コンバージョンオプティマイザーは、手動入札の場合にのみ有効です。</span><span lang=\"en\">Valid when it is in manual bidding.</span></p> <p>* <code>CONVERSION_TRACKING_NOT_ENABLED</code> - <span lang=\"ja\">コンバージョン測定タグが発行されていません。</span><span lang=\"en\">Conversion tracking tag is not enabled yet.</span></p> <p>* <code>NOT_ENOUGH_CONVERSIONS</code> - <span lang=\"ja\">コンバージョンの実績が十分ではありません。</span><span lang=\"en\">Conversion performance is not enough.</span></p> <p>* <code>UNKNOWN</code> - <span lang=\"ja\">未知の値です。</span><span lang=\"en\">Unknown Value</span></p> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



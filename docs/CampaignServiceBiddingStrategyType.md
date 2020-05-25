# CampaignServiceBiddingStrategyType

<div lang=\"ja\">CampaignServiceBiddingStrategyTypeは、自動入札タイプを表します。<br> ADD時、標準入札設定の場合、このフィールドは必須となり、ポートフォリオ入札設定の場合、省略可能となります。</div> <div lang=\"en\">CampaignServiceBiddingStrategyType displays the Auto Bidding type.<br> This field is required when Standard bidding is setting, and is optional when Portfolio bidding is setting in ADD operation.</div> <hr> <p>* <code>MANUAL_CPC</code> - <span lang=\"ja\">手動で入札を行います。<br>※キャンペーンに適用可能です。広告グループには現在設定できません。</span><span lang=\"en\">Manual CPC settings<br>* Available in campaign level. Currently not available for ad group.</span></p> <p>* <code>TARGET_ROAS</code> - <span lang=\"ja\">広告費用対効果の目標値です。<br>※キャンペーンの更新時のみ適用可能です。広告グループには現在設定できません。</span><span lang=\"en\">Target ROAS.<br>* Available on updating campaign process. Currently not available for ad group.</span></p> <p>* <code>TARGET_SPEND</code> - <span lang=\"ja\">クリック数を最大化します。<br>※キャンペーンに適用可能です。広告グループには現在設定できません。</span><span lang=\"en\">Maximize Clicks.<br>* Applicable for campaign. Currently not available for ad group.</span></p> <p>* <code>TARGET_CPA</code> - <span lang=\"ja\">コンバージョン単価の目標値です。<br>※キャンペーンに適用可能です。広告グループには現在設定できません。</span><span lang=\"en\">Target conversion spend (CPA).<br>* Applicable for campaign. Currently not available for ad group.</span></p> <p>* <code>MAXIMIZE_CONVERSIONS</code> - <span lang=\"ja\">コンバージョン数を最大化します。<br>※キャンペーンに適用可能です。広告グループには現在設定できません。</span><span lang=\"en\">Maximize Conversions.<br>* Applicable for campaign. Currently not available for ad group.</span></p> <p>* <code>UNKNOWN</code> - <span lang=\"ja\">未知の値です。</span><span lang=\"en\">Unknown Value</span></p> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



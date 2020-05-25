# CampaignServiceSettings

<div lang=\"ja\">CampaignServiceSettingsオブジェクトは、キャンペーンの地域ターゲットを格納するコンテナです。<br> ADD時、このフィールドは、campaignTypeがDYNAMIC_ADS_FOR_SEARCH_SETTINGの場合、必須となり、それ以外では省略可能となります。また、TargetingSettingが未設定の場合、デフォルト設定値は[SettingType:TARGET_LIST_SETTING, TargetAll:ACTIVE]となります。</div> <div lang=\"en\">CampaignServiceSettings object is container for geographic targeting  of campaign.<br> This field is required when campaignType is 'DYNAMIC_ADS_FOR_SEARCH_SETTING' in ADD operation. For other campaignType, this field is optional in ADD operation. The default value will be TARGET_LIST_SETTING for SettingType or ACTIVE for TargetAll when TargetingSetting is not setting.</div> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dynamic_ads_for_search_setting** | [**CampaignServiceDynamicAdsForSearchSetting**](CampaignServiceDynamicAdsForSearchSetting.md) |  | [optional] 
**geo_target_type_setting** | [**CampaignServiceGeoTargetTypeSetting**](CampaignServiceGeoTargetTypeSetting.md) |  | [optional] 
**setting_type** | [**CampaignServiceSettingType**](CampaignServiceSettingType.md) |  | [optional] 
**targeting_setting** | [**CampaignServiceTargetingSetting**](CampaignServiceTargetingSetting.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



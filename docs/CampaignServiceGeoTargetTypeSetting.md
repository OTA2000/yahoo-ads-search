# CampaignServiceGeoTargetTypeSetting

<div lang=\"ja\">CampaignServiceGeoTargetTypeSettingsオブジェクトは、地域ターゲットの情報を格納するコンテナです。<br> ADD時、settingTypeがGEO_TARGET_TYPE_SETTINGの場合、必須となり、それ以外では省略可能となります。</div> <div lang=\"en\">CampaignServiceGeoTargetTypeSettings object is a container for GeoTargeting.<br> This field is optional. However, in ADD operation, this field is required only when settingType is 'GEO_TARGET_TYPE_SETTING', and it is optional when settingType is the others.</div> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**negative_geo_target_type** | [**CampaignServiceGeoTargetType**](CampaignServiceGeoTargetType.md) |  | [optional] 
**positive_geo_target_type** | [**CampaignServiceGeoTargetType**](CampaignServiceGeoTargetType.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



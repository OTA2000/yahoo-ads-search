# CampaignServiceDynamicAdsForSearchSetting

<div lang=\"ja\">CampaignServiceDynamicAdsForSearchSettingは、動的検索連動型広告に関する検索条件を表します。<br> ADD時、settingTypeがDYNAMIC_ADS_FOR_SEARCH_SETTINGの場合、必須となり、それ以外では省略可能となります。</div> <div lang=\"en\">CampaignServiceDynamicAdsForSearchSetting displays search condition for Dynamic ads for search.<br> This field is optional. However, in ADD operation, this field is required only when settingType is 'DYNAMIC_ADS_FOR_SEARCH_SETTING', and it is optional when settingType is the others.</div> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**feed_ids** | **list[int]** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;キャンペーンで使用するページフィードIDです。&lt;br&gt; ADD時およびSET時、このフィールドは必須となります。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Page Feed ID for campaign.&lt;br&gt; This field is required in ADD and SET operation.&lt;/div&gt;  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



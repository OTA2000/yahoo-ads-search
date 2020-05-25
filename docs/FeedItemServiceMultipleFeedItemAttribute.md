# FeedItemServiceMultipleFeedItemAttribute

<div lang=\"ja\">このフィールドは、ADDおよびSET時に省略可能となり、REMOVE時には無視されます。<br> ※placeholderFieldがSTRUCTURED_SNIPPET_VALUES, ADDITIONAL_ADVANCED_URLS, ADDITIONAL_ADVANCED_MOBILE_URLSの場合、ADDおよびSET時に必須となります。</div> <div lang=\"en\">This field is optional in ADD and SET operation, and will be ignored in REMOVE operation.<br> If the placeholderField is STRUCTURED_SNIPPET_VALUES, ADDITIONAL_ADVANCED_URLS, or ADDITIONAL_ADVANCED_MOBILE_URLS, this field is required in ADD and SET operation.</div> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**feed_attribute_values** | [**list[FeedItemServiceFeedAttributeValue]**](FeedItemServiceFeedAttributeValue.md) |  | [optional] 
**is_remove** | [**FeedItemServiceIsRemove**](FeedItemServiceIsRemove.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



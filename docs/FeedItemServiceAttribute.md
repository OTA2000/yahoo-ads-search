# FeedItemServiceAttribute

<div lang=\"ja\">FeedItemServiceAttributeオブジェクトは、フィードアイテムの属性情報の値を格納します。<br> このフィールドは、ADD時に必須となり、SET時に省略可能となり、REMOVE時に無視されます。</div> <div lang=\"en\">FeedItemServiceAttribute object holds the value of Feed Item information.<br> This field is required in ADD operation, is optional in SET operation, and will be ignored in REMOVE operation.</div> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**feed_attribute_id** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;フィード属性IDです。&lt;br&gt; このフィールドは、ADDおよびSET時に無視されます。&lt;br&gt; ※アドカスタマイザーの場合は、ADDおよびSET時に必須となります。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Feed attribute ID.&lt;br&gt; This field will be ignored in ADD and SET operation.&lt;br&gt; *For AD_CUSTOMIZER, this field is required in ADD and SET operation.&lt;/div&gt;  | [optional] 
**multiple_feed_item_attribute** | [**FeedItemServiceMultipleFeedItemAttribute**](FeedItemServiceMultipleFeedItemAttribute.md) |  | [optional] 
**placeholder_field** | [**FeedItemServicePlaceholderField**](FeedItemServicePlaceholderField.md) |  | [optional] 
**simple_feed_item_attribute** | [**FeedItemServiceSimpleFeedItemAttribute**](FeedItemServiceSimpleFeedItemAttribute.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



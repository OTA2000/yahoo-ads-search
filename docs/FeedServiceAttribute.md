# FeedServiceAttribute

<div lang=\"ja\">FeedServiceAttributeオブジェクトは、自動データ挿入のリストの属性を格納します。<br> このフィールドは、ADDおよびSET時に省略可能となり、REMOVE時に無視されます。</div> <div lang=\"en\">FeedServiceAttribute object contains the attribute of auto data insertion list.<br> This field is optional in ADD and SET operation, and will be ignored in REMOVE operation.</div> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**feed_attribute_id** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;自動データ挿入のリストの属性（カラム）IDです。&lt;br&gt; このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Attribute ID (column ID) of auto data insertion list.&lt;br&gt; Although this field will be returned in the response, it will be ignored on input.&lt;/div&gt;  | [optional] 
**feed_attribute_name** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;自動データ挿入のリストの属性（カラム）名です。&lt;br&gt; このフィールドはADDおよびSET時に必須となり、REMOVE時に無視されます。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Attribute name (column name) of auto data insertion list.&lt;br&gt; This field is required in ADD and SET operation, and will be ignored in REMOVE operation.&lt;/div&gt;  | [optional] 
**placeholder_field** | [**FeedServicePlaceholderField**](FeedServicePlaceholderField.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# FeedItemServiceCustomParameter

<div lang=\"ja\">FeedItemServiceCustomParameterは、カスタムパラメータの内容を表します。<br> このフィールドは、ADDおよびSET時に必須となります。<br> SET時、このフィールドは既存の項目を置き換えます。<br> ※削除フラグを立てた場合(isRemove=TRUE)、このフィールドは無視され、こちらの項目関係なく、全項目が削除されます。</div> <div lang=\"en\">FeedItemServiceCustomParameter displays the element of custom parameters.<br> This field is required in ADD and SET operation.<br> This field replaces the  current items in SET operation.<br> *If the delete flag is set (isRemove=TRUE), this field will be ignored and all items will  be deleted.</div> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;キーです。&lt;br&gt; このフィールドは、ADDおよびSET時に必須となります。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Key of parameter.&lt;br&gt; This field is required in ADD and SET operation.&lt;/div&gt;  | [optional] 
**value** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;値です。&lt;br&gt; このフィールドは、ADDおよびSET時に省略可能となります。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Value of parameter.&lt;br&gt; This field is optional in ADD and SET operation.&lt;br&gt;&lt;/div&gt;  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



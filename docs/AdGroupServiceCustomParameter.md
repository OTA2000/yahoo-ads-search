# AdGroupServiceCustomParameter

<div lang=\"ja\">AdGroupServiceCustomParameterは、カスタムパラメータの内容を表します。<br> ADDおよびSET時、customParameters配下では必須となります。<br> ※SET時、既存の項目を置き換えます。また、このフィールドはisRemoveの設定値がTRUEの場合は無視され、全項目が削除されます。</div> <div lang=\"en\">AdGroupServiceCustomParameter displays the element of custom parameters.<br> In ADD and SET operation,this field is required under 'customParameters'.<br> *In SET operation, it will replace the current items. In addition, it will be ignored and all item will be deleted if 'isRemove'  is set TRUE.</div> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;キーです。&lt;br&gt; ADDおよびSET時、このフィールドは必須となります。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Key of parameter.&lt;br&gt; This field is required in ADD and SET operation.&lt;/div&gt;  | [optional] 
**value** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;値です。&lt;br&gt; ADDおよびSET時、このフィールドは省略可能となります。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Value of parameter.&lt;br&gt; This field is optional in ADD and SET operation.&lt;br&gt;&lt;/div&gt;  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



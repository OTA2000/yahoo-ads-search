# AdGroupWebpageServiceWebpageCondition

<div lang=\"ja\">AdGroupWebpageServiceWebpageConditionオブジェクトは、Webpageの条件を保持します。<br> このフィールドは、ADD時は必須となり、SET時は無視されます。</div> <div lang=\"en\">AdGroupWebpageServiceWebpageCondition object contains the rules of webpage.<br> This field is required in ADD operation, and will be ignored in SET operation.</div> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**argument** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;条件の設定値(正規表現の指定可)です。&lt;br&gt;ADD時、このフィールドは必須です。※typeがALL_PAGESの場合は省略可能となります。SET時、このフィールドは無視されます。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Value of rule setting (Can specify regular expression)&lt;br&gt;This field is required in ADD operation, and will be ignored in SET operation. *If type is &#39;ALL_PAGES&#39;, this field is optional in ADD operation.&lt;/div&gt;  | [optional] 
**webpage_condition_type** | [**AdGroupWebpageServiceWebpageConditionType**](AdGroupWebpageServiceWebpageConditionType.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



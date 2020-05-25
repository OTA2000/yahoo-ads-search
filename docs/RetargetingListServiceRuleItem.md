# RetargetingListServiceRuleItem

<div lang=\"ja\">RetargetingListServiceRuleItemは、ルールの評価条件を保持するオブジェクトです。<br> このフィールドは、ADDおよびSET時に必須となります。</div> <div lang=\"en\">RetargetingListServiceRuleItem is an object that holds evaluation condition of rule.<br> This field is required in ADD and SET operation.</div> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**custom_key_rule_item** | [**RetargetingListServiceCustomKeyRuleItem**](RetargetingListServiceCustomKeyRuleItem.md) |  | [optional] 
**rule_operator** | [**RetargetingListServiceRuleOperator**](RetargetingListServiceRuleOperator.md) |  | [optional] 
**rule_type** | [**RetargetingListServiceRuleType**](RetargetingListServiceRuleType.md) |  | [optional] 
**url_rule_item** | [**RetargetingListServiceUrlRuleItem**](RetargetingListServiceUrlRuleItem.md) |  | [optional] 
**value** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;評価値です。&lt;br&gt; ADDおよびSET時、このフィールドは必須となります。&lt;br&gt; ※括弧（()）、シングルクォート（&amp;#39;）、ダブルクォート（&amp;#34;）、タブ（\\t）は利用できません。&lt;br&gt; ※250文字まで指定可能です。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Evaluation value.&lt;br&gt; *Cannot use: bracket, single quote, double quote, and tab.&lt;br&gt; *Can select up to 250 characters.&lt;br&gt; This field is required in ADD and SET operation.&lt;/div&gt;  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



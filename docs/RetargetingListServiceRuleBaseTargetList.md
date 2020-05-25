# RetargetingListServiceRuleBaseTargetList

<div lang=\"ja\">RetargetingListServiceRuleBaseTargetListは、ベースターゲットリストの情報を保持するオブジェクトです。<br> このフィールドは、省略可能となります。<br> ※targetListTypeがRULEの場合、このフィールドは必須となります。</div> <div lang=\"en\">RetargetingListServiceRuleBaseTargetList is an object that holds Rule based target list information.<br> This field is optional.<br>*If the targetListType is RULE, this field is required.</div> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_date** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;ルール適用終了日です。&lt;br&gt; このフィールドは、ADDおよびSET時に省略可能となります。&lt;br&gt; isDateSpecificがTRUEである場合、ADDおよびSET時に必須となります。&lt;br&gt; ※YYYYMMDD形式です。&lt;br&gt; ※リクエスト日は2037/12/30まで 指定可能です。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;End date of rule setting.&lt;br&gt; This field is optional in ADD and SET operation.&lt;br&gt; If isDateSpecific is TRUE, this field  is required in ADD and SET operation.&lt;br&gt; *In YYYYMMDD format&lt;br&gt; *Request date can be set up to 2037/12/30&lt;/div&gt;  | [optional] 
**is_all_visitor_rule** | [**RetargetingListServiceIsAllVisitorRule**](RetargetingListServiceIsAllVisitorRule.md) |  | [optional] 
**is_date_specific_rule** | [**RetargetingListServiceIsDateSpecificRule**](RetargetingListServiceIsDateSpecificRule.md) |  | [optional] 
**rules** | [**list[RetargetingListServiceRuleGroup]**](RetargetingListServiceRuleGroup.md) |  | [optional] 
**start_date** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;ルール適用開始日です。&lt;br&gt; ADDおよびSET時、このフィールドは省略可能となります。&lt;br&gt; isDateSpecificがTRUEである場合、ADDおよびSET時に必須となります。 &lt;br&gt; ※YYYYMMDD形式です。&lt;br&gt;※リクエスト日は2037/12/30まで 指定可能です。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Start date of rule setting.&lt;br&gt; This field is optional in ADD and SET operation.&lt;br&gt; If isDateSpecific is TRUE, this field is  required in ADD and SET operation.&lt;br&gt; *In YYYYMMDD format&lt;br&gt; *Request date can be set up to 2037/12/30 &lt;/div&gt;  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



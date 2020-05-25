# AccountServiceBudget

<div lang=\"ja\">AccountServiceBudgetオブジェクトは、広告予算を表します。</div> <div lang=\"en\">AccountServiceBudget object describes Budget for advertising on the account.</div> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;アカウントの広告予算金額です。&lt;br&gt; SET時、このフィールドは無視されます。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Amount of budget.&lt;br&gt; This field will be ignored in SET operation.&lt;/div&gt;  | [optional] 
**end_date** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;掲載終了日です。&lt;br&gt; SET時、このフィールドは無視されます。&lt;br&gt;「yyyyMMdd」形式で表示されます。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;End date of ad serving.&lt;br&gt;This field will be ignored in SET operation.&lt;br&gt; It is displayed in &amp;#39;yyyyMMdd&amp;#39; format.&lt;/div&gt;  | [optional] 
**limit_charge_type** | [**AccountServiceLimitChargeType**](AccountServiceLimitChargeType.md) |  | [optional] 
**start_date** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;掲載開始日です。&lt;br&gt; 「yyyyMMdd」形式で表示されます。&lt;br&gt; SET時、このフィールドは無視されます。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Start date of ad serving.&lt;br&gt; This field will be ignored in SET operation.&lt;br&gt; It is displayed in &amp;#39;yyyyMMdd&amp;#39; format.&lt;/div&gt;  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



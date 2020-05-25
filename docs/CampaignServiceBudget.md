# CampaignServiceBudget

<div lang=\"ja\">CampaignServiceBudgetオブジェクトは、キャンペーン予算に関する情報を表します。<br> このフィールドは、ADD時に必須となり、SET時は省略可能となります。</div> <div lang=\"en\">CampaignServiceBudget object displays budget information for campaign.<br> This field is required in ADD operation, and will be optional in SET operation.</div> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;1日単位のキャンペーン予算利用金額です。&lt;br&gt; このフィールドは、ADD時は必須となり、SET時は省略可能となります。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Amount of budget of Campaign.&lt;br&gt; This field is required in ADD operation, and is optional in SET operation.&lt;/div&gt;  | [optional] 
**budget_period** | [**CampaignServiceBudgetPeriod**](CampaignServiceBudgetPeriod.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



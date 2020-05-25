# Account

<div lang=\"ja\">Accountオブジェクトは、アカウントを表します。</div> <div lang=\"en\">Search Account</div> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;アカウントIDです。&lt;br&gt; SET時、このフィールドは必須となります。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Account ID.&lt;br&gt; This field is required in SET operation.&lt;/div&gt;  | [optional] 
**account_name** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;アカウント名です。&lt;br&gt; SET時、このフィールドは省略可能となります。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Account Name.&lt;br&gt; This field is optional in SET operation.&lt;/div&gt;  | [optional] 
**account_status** | [**AccountServiceStatus**](AccountServiceStatus.md) |  | [optional] 
**account_type** | [**AccountServiceType**](AccountServiceType.md) |  | [optional] 
**auth_type** | [**AccountServiceAuthType**](AccountServiceAuthType.md) |  | [optional] 
**auto_tagging_enabled** | [**AccountServiceAutoTaggingEnabled**](AccountServiceAutoTaggingEnabled.md) |  | [optional] 
**budget** | [**AccountServiceBudget**](AccountServiceBudget.md) |  | [optional] 
**delivery_status** | [**AccountServiceDeliveryStatus**](AccountServiceDeliveryStatus.md) |  | [optional] 
**is_test_account** | [**AccountServiceIsTestAccount**](AccountServiceIsTestAccount.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



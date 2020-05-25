# AccountServiceSelector

<div lang=\"ja\">AccountServiceSelectorオブジェクトは、選択するアカウントを表します。</div> <div lang=\"en\">Explains which accounts to return.</div> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_ids** | **list[int]** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;アカウントIDの配列です。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Account IDs.&lt;/div&gt;  | [optional] 
**account_name** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;アカウント名&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Account Name&lt;/div&gt;  | [optional] 
**account_statuses** | [**list[AccountServiceStatus]**](AccountServiceStatus.md) |  | [optional] 
**account_types** | [**list[AccountServiceType]**](AccountServiceType.md) |  | [optional] 
**auth_type** | [**AccountServiceAuthType**](AccountServiceAuthType.md) |  | [optional] 
**include_test_account** | [**AccountServiceIncludeTestAccount**](AccountServiceIncludeTestAccount.md) |  | [optional] 
**number_results** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;ページの最大件数です。このフィールドは、1以上を指定する必要があります。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Maximum number of results to return in this page. This field must be greater than or equal to 1. Also see Entity Limits per operation.&lt;/div&gt;  | [optional] [default to 200]
**start_index** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;ページの先頭のインデックスです。このフィールドは、1以上を指定する必要があります。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Index of the first result to return in this page. This field must be greater than or equal to 1.&lt;/div&gt;  | [optional] [default to 1]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



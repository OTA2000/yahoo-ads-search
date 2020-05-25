# RetargetingListServiceSelector

<div lang=\"ja\">RetargetingListServiceSelectorは、ターゲットリストの検索条件（実行パラメータ）を保持するオブジェクトです。</div> <div lang=\"en\">RetargetingListServiceSelector is an object that holds search condition (parameter).</div> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;検索条件：アカウントIDです。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Search conditon: Account ID.&lt;/div&gt;  | 
**number_results** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;ページの最大件数です。このフィールドは、1以上を指定する必要があります。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Maximum number of results to return in this page. This field must be greater than or equal to 1. Also see Entity Limits per operation.&lt;/div&gt;  | [optional] [default to 500]
**start_index** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;ページの先頭のインデックスです。このフィールドは、1以上を指定する必要があります。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Index of the first result to return in this page. This field must be greater than or equal to 1.&lt;/div&gt;  | [optional] [default to 1]
**target_list_ids** | **list[int]** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;検索条件：ターゲットリストIDです。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Search conditon: Target List ID.&lt;/div&gt;  | [optional] 
**target_list_owner** | [**RetargetingListServiceTargetListOwner**](RetargetingListServiceTargetListOwner.md) |  | [optional] 
**target_list_types** | [**list[RetargetingListServiceTargetListType]**](RetargetingListServiceTargetListType.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



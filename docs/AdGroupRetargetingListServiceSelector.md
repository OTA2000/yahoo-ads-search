# AdGroupRetargetingListServiceSelector

<div lang=\"ja\">AdGroupRetargetingListServiceSelector、広告グループレベルでのターゲットリスト設定の検索条件（実行パラメータ）を保持するオブジェクトです。</div> <div lang=\"en\">AdGroupRetargetingListServiceSelector is an object that holds search condition (parameter).</div> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;検索条件：アカウントIDです。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Account ID.&lt;/div&gt;  | 
**ad_group_ids** | **list[int]** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;検索条件：広告グループIDです。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Ad group ID.&lt;/div&gt;  | [optional] 
**campaign_ids** | **list[int]** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;検索条件：キャンペーンIDです。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Campaign ID.&lt;/div&gt;  | [optional] 
**excluded_type** | [**AdGroupRetargetingListServiceExcludedType**](AdGroupRetargetingListServiceExcludedType.md) |  | [optional] 
**number_results** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;ページの最大件数です。このフィールドは、1以上を指定する必要があります。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Maximum number of results to return in this page. This field must be greater than or equal to 1. Also see Entity Limits per operation.&lt;/div&gt;  | [optional] [default to 500]
**start_index** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;ページの先頭のインデックスです。このフィールドは、1以上を指定する必要があります。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Index of the first result to return in this page. This field must be greater than or equal to 1.&lt;/div&gt;  | [optional] [default to 1]
**target_list_ids** | **list[int]** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;検索条件：ターゲットリストIDです。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Target list ID.&lt;/div&gt;  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



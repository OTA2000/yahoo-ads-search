# CampaignRetargetingListServiceSelector

<div lang=\"ja\">CampaignRetargetingListServiceSelectorオブジェクトは、キャンペーン階層におけるターゲットリストの設定情報を取得するための検索条件（実行パラメータ）を保持します。</div> <div lang=\"en\">CampaignRetargetingListServiceSelector object holds search conditions (exec parameters) to get Target List settings on the campaign level.</div> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;アカウントIDです。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Search conditon: Account ID.&lt;/div&gt;  | 
**campaign_ids** | **list[int]** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;キャンペーンIDです。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Search conditon: Campaign ID.&lt;/div&gt;  | [optional] 
**excluded_type** | [**CampaignRetargetingListServiceExcludedType**](CampaignRetargetingListServiceExcludedType.md) |  | [optional] 
**number_results** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;ページの最大件数です。このフィールドは、1以上を指定する必要があります。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Maximum number of results to return in this page. This field must be greater than or equal to 1. Also see Entity Limits per operation.&lt;/div&gt;  | [optional] [default to 500]
**start_index** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;ページの先頭のインデックスです。このフィールドは、1以上を指定する必要があります。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Index of the first result to return in this page. This field must be greater than or equal to 1.&lt;/div&gt;  | [optional] [default to 1]
**target_list_ids** | **list[int]** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;ターゲットリストIDです。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Search conditon: Target List ID.&lt;/div&gt;  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



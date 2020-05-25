# CampaignServiceSelector

<div lang=\"ja\">CampaignServiceSelectorオブジェクトは、操作の対象とするキャンペーンの情報およびフィルタ条件を表します。</div> <div lang=\"en\">CampaignServiceSelector object displays information and filter criteria of campaign to be operated.</div> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;検索条件：アカウントIDです。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Search condition: Account ID.&lt;/div&gt;  | 
**bidding_strategy_ids** | **list[int]** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;検索条件：自動入札IDです。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Search condition: Auto Bidding ID.&lt;/div&gt;  | [optional] 
**campaign_ids** | **list[int]** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;検索条件：キャンペーンIDです。&lt;br&gt; ※指定しない場合は、フィルタ条件に すべてのキャンペーンが含まれます。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Search condition: Campaign ID&lt;br&gt; * All campaign will return, if no campaign are not specified.&lt;/div&gt;  | [optional] 
**contains_label_id** | [**CampaignServiceContainsLabelId**](CampaignServiceContainsLabelId.md) |  | [optional] 
**label_ids** | **list[int]** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;検索条件：ラベルIDです。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Search condition: Label ID.&lt;/div&gt;  | [optional] 
**number_results** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;ページの最大件数です。このフィールドは、1以上を指定する必要があります。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Maximum number of results to return in this page. This field must be greater than or equal to 1. Also see Entity Limits per operation.&lt;/div&gt;  | [optional] [default to 500]
**start_index** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;ページの先頭のインデックスです。このフィールドは、1以上を指定する必要があります。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Index of the first result to return in this page. This field must be greater than or equal to 1.&lt;/div&gt;  | [optional] [default to 1]
**user_statuses** | [**list[CampaignServiceUserStatus]**](CampaignServiceUserStatus.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# BiddingStrategyServiceSelector

<div lang=\"ja\">BiddingStrategyServiceSelectorオブジェクトは、自動入札設定の検索条件に関する情報を表します。</div> <div lang=\"en\">BiddingStrategyServiceSelector object displays the details of search results of auto bidding setting .</div> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;アカウントID&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Account ID.&lt;/div&gt;  | 
**bidding_strategy_ids** | **list[int]** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;自動入札ID&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Auto bidding ID.&lt;/div&gt;  | [optional] 
**bidding_strategy_types** | [**list[BiddingStrategyServiceType]**](BiddingStrategyServiceType.md) |  | [optional] 
**number_results** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;ページの最大件数です。このフィールドは、1以上を指定する必要があります。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Maximum number of results to return in this page. This field must be greater than or equal to 1. Also see Entity Limits per operation.&lt;/div&gt;  | [optional] [default to 500]
**start_index** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;ページの先頭のインデックスです。このフィールドは、1以上を指定する必要があります。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Index of the first result to return in this page. This field must be greater than or equal to 1.&lt;/div&gt;  | [optional] [default to 1]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



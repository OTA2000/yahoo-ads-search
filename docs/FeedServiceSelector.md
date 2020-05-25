# FeedServiceSelector

<div lang=\"ja\">FeedServiceSelectorオブジェクトは、自動データ挿入のリストの基本情報を格納します。</div> <div lang=\"en\">FeedServiceSelector describes the basic information of list of Data auto insertion.</div> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;アカウントIDです。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Account ID.&lt;/div&gt;  | 
**feed_ids** | **list[int]** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;自動データ挿入のリストのIDです。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;List ID of Feed.&lt;/div&gt;  | [optional] 
**number_results** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;ページの最大件数です。このフィールドは、1以上を指定する必要があります。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Maximum number of results to return in this page. This field must be greater than or equal to 1. Also see Entity Limits per operation.&lt;/div&gt;  | [optional] [default to 50]
**placeholder_types** | [**list[FeedServicePlaceholderType]**](FeedServicePlaceholderType.md) |  | [optional] 
**start_index** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;ページの先頭のインデックスです。このフィールドは、1以上を指定する必要があります。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Index of the first result to return in this page. This field must be greater than or equal to 1.&lt;/div&gt;  | [optional] [default to 1]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



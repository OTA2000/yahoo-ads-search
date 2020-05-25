# AdGroupFeedServiceSelector

<div lang=\"ja\">AdGroupFeedServiceSelectorオブジェクトは、FeedItem情報を指定します。</div> <div lang=\"en\">AdGroupFeedServiceSelector describes the FeedItem information.</div> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;アカウントIDです。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Account ID.&lt;/div&gt;  | 
**ad_group_ids** | **list[int]** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;広告グループIDです。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Ad group ID.&lt;/div&gt;  | [optional] 
**campaign_ids** | **list[int]** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;キャンペーンIDです。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Campaign ID.&lt;/div&gt;  | [optional] 
**feed_item_ids** | **list[int]** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;FeedItem情報のIDです。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;FeedItem information ID.&lt;/div&gt;  | [optional] 
**number_results** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;ページの最大件数です。このフィールドは、1以上を指定する必要があります。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Maximum number of results to return in this page. This field must be greater than or equal to 1. Also see Entity Limits per operation.&lt;/div&gt;  | [optional] [default to 500]
**placeholder_types** | [**list[AdGroupFeedServicePlaceholderType]**](AdGroupFeedServicePlaceholderType.md) |  | [optional] 
**start_index** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;ページの先頭のインデックスです。このフィールドは、1以上を指定する必要があります。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Index of the first result to return in this page. This field must be greater than or equal to 1.&lt;/div&gt;  | [optional] [default to 1]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



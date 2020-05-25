# BidLandscapeServiceSelector

<div lang=\"ja\">BidLandscapeServiceSelectorオブジェクトは、予測するクライテリアを表します。</div> <div lang=\"en\">BidLandscapeServiceSelector object describes the criteria to be estimated.</div> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;アカウントIDです。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Account ID&lt;/div&gt;  | 
**campaign_id** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;キャンペーンIDです。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Campaign ID&lt;/div&gt;  | 
**ad_group_id** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;広告グループIDです。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Ad Gropup ID.&lt;/div&gt;  | 
**criterion_ids** | **list[int]** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;クライテリアIDです。最大100個まで指定できます。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;ID of this criterion. The maximum value is 100.&lt;/div&gt;  | [optional] 
**sim_type** | [**BidLandscapeServiceSimType**](BidLandscapeServiceSimType.md) |  | 
**start_index** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;ページの先頭のインデックスです。このフィールドは、1以上を指定する必要があります。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Index of the first result to return in this page. This field must be greater than or equal to 1.&lt;/div&gt;  | [optional] [default to 1]
**number_results** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;ページの最大件数です。このフィールドは、1以上を指定する必要があります。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Maximum number of results to return in this page. This field must be greater than or equal to 1. Also see Entity Limits per operation.&lt;/div&gt;  | [optional] [default to 100]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# AdGroupWebpageServiceSelector

<div lang=\"ja\">AdGroupWebpageServiceSelectorオブジェクトは、取得する条件を保持します。</div> <div lang=\"en\">AdGroupWebpageServiceSelector object contains the rules to be acquired.</div> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;アカウントID&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Account ID&lt;/div&gt;  | 
**ad_group_ids** | **list[int]** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;広告グループID&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;AdGroup ID&lt;/div&gt;  | [optional] 
**campaign_ids** | **list[int]** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;キャンペーンID&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Campaign ID&lt;/div&gt;  | [optional] 
**number_results** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;ページの最大件数です。このフィールドは、1以上を指定する必要があります。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Maximum number of results to return in this page. This field must be greater than or equal to 1. Also see Entity Limits per operation.&lt;/div&gt;  | [optional] [default to 500]
**start_index** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;ページの先頭のインデックスです。このフィールドは、1以上を指定する必要があります。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Index of the first result to return in this page. This field must be greater than or equal to 1.&lt;/div&gt;  | [optional] [default to 1]
**target_ids** | **list[int]** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;配信/除外設定を識別するID&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Unique ID to identify &amp;#39;Allow&amp;#39; or &amp;#39;Exclude&amp;#39; settings&lt;/div&gt;  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



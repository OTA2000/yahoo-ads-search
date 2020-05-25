# CampaignCriterionServiceSelector

<div lang=\"ja\">CampaignCriterionServiceSelectorオブジェクトは、操作の対象となるキャンペーンのクライテリアを表します。</div> <div lang=\"en\">CampaignCriterionServiceSelector object describes campaign criteria for operation.</div> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;アカウントIDです。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Account ID.&lt;/div&gt;  | 
**campaign_ids** | **list[int]** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;キャンペーンIDの配列です。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Campaign ID array.&lt;/div&gt;  | [optional] 
**criterion_ids** | **list[int]** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;クライテリオンIDの配列です。&lt;br&gt; 指定しない場合は、キャンペーンID以下のすべてのクライテリアが含まれます。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Criterion ID array.&lt;br&gt; If no criterionIds, all of criterionIds under the campaign ID are returned.&lt;/div&gt;  | [optional] 
**number_results** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;ページの最大件数です。このフィールドは、1以上を指定する必要があります。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Maximum number of results to return in this page. This field must be greater than or equal to 1. Also see Entity Limits per operation.&lt;/div&gt;  | [optional] [default to 500]
**start_index** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;ページの先頭のインデックスです。このフィールドは、1以上を指定する必要があります。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Index of the first result to return in this page. This field must be greater than or equal to 1.&lt;/div&gt;  | [optional] [default to 1]
**use** | [**CampaignCriterionServiceUse**](CampaignCriterionServiceUse.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



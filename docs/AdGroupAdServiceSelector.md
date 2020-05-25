# AdGroupAdServiceSelector

<div lang=\"ja\">AdGroupAdServiceSelectorオブジェクトは、操作の対象とする広告およびフィルタ条件を表します。</div> <div lang=\"en\">AdGroupAdServiceSelector object describes the information and filter criteria of the Ads to be operated on.</div> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;検索条件：アカウントID&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Search condition: Account ID.&lt;/div&gt;  | 
**ad_group_ids** | **list[int]** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;検索条件：広告グループID&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Search condition: Ad group ID.&lt;br&gt; Ads returned will be from adgroups whose ids are included in this list.&lt;/div&gt;  | [optional] 
**ad_ids** | **list[int]** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;検索条件：広告ID&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Search condition: Ad ID.&lt;br&gt; Ads will return from ads whose ids are included in this list.&lt;br&gt; If you omit adIds field, it will return all adIds under the adGroup.&lt;/div&gt;  | [optional] 
**ad_types** | [**list[AdGroupAdServiceAdType]**](AdGroupAdServiceAdType.md) |  | [optional] 
**approval_statuses** | [**list[AdGroupAdServiceApprovalStatus]**](AdGroupAdServiceApprovalStatus.md) |  | [optional] 
**campaign_ids** | **list[int]** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;検索条件：キャンペーンID&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Search condition: Campaign ID.&lt;br&gt; Ads returned will be from campaigns whose ids are included in this list.&lt;br&gt; An empty list means there are no campaign restrictions when selecting AdGroupAds.&lt;br&gt; * This field must contain distinct elements.&lt;br&gt;* This field cannot contain null elements.&lt;/div&gt;  | [optional] 
**contains_label_id** | [**AdGroupAdServiceContainsLabelId**](AdGroupAdServiceContainsLabelId.md) |  | [optional] 
**label_ids** | **list[int]** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;検索条件：ラベルID&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Search condition: Label ID&lt;/div&gt;  | [optional] 
**number_results** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;ページの最大件数です。このフィールドは、1以上を指定する必要があります。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Maximum number of results to return in this page. This field must be greater than or equal to 1. Also see Entity Limits per operation.&lt;/div&gt;  | [optional] [default to 500]
**start_index** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;ページの先頭のインデックスです。このフィールドは、1以上を指定する必要があります。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Index of the first result to return in this page. This field must be greater than or equal to 1.&lt;/div&gt;  | [optional] [default to 1]
**user_statuses** | [**list[AdGroupAdServiceUserStatus]**](AdGroupAdServiceUserStatus.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



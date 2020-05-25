# CampaignSharedSet

<div lang=\"ja\">CampaignSharedSetは、キャンペーンと対象外キーワードリストの関連付け情報を保持するオブジェクトです。</div> <div lang=\"en\">CampaignSharedSet is object to hold setup information between negative keyword list and campaign.</div> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;アカウントIDです。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Account ID.&lt;/div&gt;  | [optional] 
**campaign_id** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;キャンペーンIDです。&lt;br&gt; ADD時およびREMOVE時、このフィールドは必須です。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Campaign ID.&lt;br&gt; This field is required in ADD and REMOVE operation.&lt;/div&gt;  | [optional] 
**campaign_name** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;キャンペーン名です。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Campaign name.&lt;/div&gt;  | [optional] 
**shared_list_id** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;アカウントの対象外キーワードリストIDです。&lt;br&gt; ADD時およびREMOVE時、このフィールドは必須です。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Negative keyword list ID of the account.&lt;br&gt; This field is required in ADD and REMOVE operation.&lt;/div&gt;  | [optional] 
**shared_list_name** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;アカウントの対象外キーワードリスト名です。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Negative keyword list name of the account.&lt;/div&gt;  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



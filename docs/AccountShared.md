# AccountShared

<div lang=\"ja\">AccountSharedオブジェクトは、アカウント内で共有できる対象外キーワードリストの情報を表します。</div> <div lang=\"en\">AccountShared object describes negative keyword list which can be shared within the account.</div> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;アカウントIDです。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Account ID.&lt;/div&gt;  | [optional] 
**member_count** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;対象外キーワードリストに含まれるアイテム（検索対象外キーワード）数です。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Number of items on Negative keyword list (keyword excluded on search).&lt;/div&gt;  | [optional] 
**name** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;対象外キーワードリスト名です。&lt;br&gt;ADDおよびSET時、このフィールドは必須となります。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Negative keyword list name.&lt;br&gt;This field is required in ADD and SET operation.&lt;/div&gt;  | [optional] 
**reference_count** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;対象外キーワードリストを使用している キャンペーン数です。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Number of campaigns which use negative keyword list.&lt;/div&gt;  | [optional] 
**shared_list_id** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;対象外キーワードリストIDです。&lt;br&gt;SETおよびREMOVE時、このフィールドは必須となります。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Negative keyword list ID.&lt;br&gt;This field is required in SET and REMOVE operation.&lt;/div&gt;  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# Label

<div lang=\"ja\">Labelオブジェクトは、ラベルの情報を表します。</div> <div lang=\"en\">Label object describes label information.</div> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;アカウントIDです。&lt;br&gt; このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Account ID.&lt;br&gt; Although this field will be returned in the response, it will be ignored on input.&lt;/div&gt;  | [optional] 
**color** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;カラーです。&lt;br&gt; このフィールドは、ADDおよびSET時に省略可能となり、REMOVE時に無視されます。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Color.&lt;br&gt; This field is optional in ADD and SET operation, and will be ignored in REMOVE operation.&lt;/div&gt;  | [optional] 
**description** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;説明文です。&lt;br&gt; このフィールドは、ADDおよびSET時に省略可能となり、REMOVE時に無視されます。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Description.&lt;br&gt; This field is optional in ADD and SET operation, and will be ignored in REMOVE operation.&lt;/div&gt;  | [optional] 
**label_id** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;ラベルIDです。&lt;br&gt; このフィールドは、SETおよびREMOVE時に必須となり、ADD時に無視されます。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Label ID.&lt;br&gt; This field is required in SET and REMOVE operation, and will be ignored in ADD operation.&lt;/div&gt;  | [optional] 
**label_name** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;ラベル名です。&lt;br&gt; このフィールドは、ADD時に必須となり、SET時に省略可能となり、REMOVE時に無視されます。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Label Name.&lt;br&gt; This field is required in ADD operation, is optional in SET operation, and will be ignored in REMOVE operation.&lt;/div&gt;  | [optional] 
**labeled_ad_group** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;広告グループの紐付け数です。&lt;br&gt; このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Number of labeled AdGroup.&lt;br&gt; Although this field will be returned in the response, it will be ignored on input.&lt;/div&gt;  | [optional] 
**labeled_ad_group_ad** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;広告の紐付け数です。&lt;br&gt;このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Number of labeled AdGroupAd.&lt;br&gt; Although this field will be returned in the response, it will be ignored on input.&lt;/div&gt;  | [optional] 
**labeled_ad_group_criterion** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;キーワードの紐付け数です。&lt;br&gt; このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Number of labeled Ad Group Criterion.&lt;br&gt; Although this field will be returned in the response, it will be ignored on input.&lt;/div&gt;  | [optional] 
**labeled_campaign** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;キャンペーンの紐付け数です。&lt;br&gt; このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Number of labeled Campaign.&lt;br&gt; Although this field will be returned in the response, it will be ignored on input.&lt;/div&gt;  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



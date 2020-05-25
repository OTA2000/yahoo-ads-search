# FeedItemServiceTargetingKeyword

<div lang=\"ja\">FeedItemServiceTargetingKeywordオブジェクトは、データ自動挿入のターゲットキーワードを表します。<br> このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。<br> ※アドカスタマイザーの場合は、ADDおよびSET時に省略可能となります。</div> <div lang=\"en\">FeedItemServiceTargetingKeyword contains keyword setting for Data Auto Insertion.<br> Although this field will be returned in the response, it will be  ignored on input.<br> *For AD_CUSTOMIZER, this field is optional in ADD and SET operation.</div> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keyword_match_type** | [**FeedItemServiceKeywordMatchType**](FeedItemServiceKeywordMatchType.md) |  | [optional] 
**targeting_keyword_id** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;指定したキーワード（text）を識別する IDになります。&lt;br&gt; ※設定を解除する場合は「0」を指定 してください。&lt;br&gt; このフィールドは、SET時に省略可能となります。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;ID to identify the Targeting keyword (text).&lt;br&gt; * To deactive, set &amp;#34;0&amp;#34;.&lt;br&gt; This field is optional in SET operation.&lt;/div&gt;  | [optional] 
**text** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;指定するキーワードです。&lt;br&gt;※入力制限：80文字、10ワード までです。&lt;br&gt; このフィールドはADDおよびSET時に必須となります。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Keyword text.&lt;br&gt; * Insert limit: Up to 80 characters and/or 10 words.&lt;br&gt; This field is required in ADD and SET operation.&lt;/div&gt;  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# FeedItemServiceTargetingAdGroup

<div lang=\"ja\">FeedItemServiceTargetingAdGroupオブジェクトは、データ自動挿入の広告グループとの紐付けを表します。<br> このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。<br> ※アドカスタマイザーの場合、ADDおよびSET時に省略可能となります。</div> <div lang=\"en\">FeedItemServiceTargetingAdGroup contains ad group setting for Data Auto Insertion.<br> Although this field will be returned in the response, it will be  ignored on input.<br> *For AD_CUSTOMIZER, this field is optional in ADD and SET operation.</div> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**targeting_ad_group_id** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;配信に使用する広告グループIDです。&lt;br&gt; ※設定を解除する場合は「0」を指定してください。&lt;br&gt; ※addのリクエストで、「0」指定は未 指定と同じ扱いになります。&lt;br&gt; データ自動挿入の場合、このフィールドはADDおよびSET時に省略可能となります。 &lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Targeting Ad group ID.&lt;br&gt; * To deactive, insert &amp;#34;0&amp;#34;.&lt;br&gt; * It would be &amp;#34;no setting&amp;#34;, if &amp;#34;0&amp;#34; is set in add request.&lt;br&gt; For AD_CUSTOMIZER, this field is optional in ADD and SET operation.&lt;/div&gt;  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



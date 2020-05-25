# FeedItemServiceTargetingCampaign

<div lang=\"ja\">FeedItemServiceTargetingCampaignオブジェクトは、データ自動挿入のキャンペーンとの紐付けを表します。<br> このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。<br> ※アドカスタマイザーの場合は、ADDおよびSET時に省略可能となります。</div> <div lang=\"en\">FeedItemServiceTargetingCampaign contains Campaign setting for Data Auto Insertion.<br> Although this field will be returned in the response, it will be ignored on input.<br> *For AD_CUSTOMIZER, this field is optional in ADD and SET operation.</div> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**targeting_campaign_id** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;配信に使用するキャンペーンIDです。&lt;br&gt; ※設定を解除する場合は「0」を指定してください。&lt;br&gt; ※addのリクエストで、「0」指定は未指定と同じ扱いになります。&lt;br&gt; データ自動挿入の場合、このフィールドはADDおよびSET時に必須となります。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Campaign ID used for ad display.&lt;br&gt; *Specify &amp;#39;0&amp;#39; to clear the setting.&lt;br&gt; *The specified &amp;#39;0&amp;#39; will be handled as same as &amp;#39;not specified&amp;#39; by add request.&lt;br&gt; For AD_CUSTOMIZER, This field is required in ADD and SET operation.&lt;/div&gt;  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



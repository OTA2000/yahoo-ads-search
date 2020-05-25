# FeedItemServiceLocation

<div lang=\"ja\">FeedItemServiceLocationオブジェクトは、地域設定情報を格納します。<br> このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。<br> ※アドカスタマイザーの場合は、ADD時に省略可能となります。</div> <div lang=\"en\">FeedItemServiceLocation object contains the information of Geographic FeedItemServiceLocation.<br> Although this field will be returned in the  response, it will be ignored on input.<br> *For AD_CUSTOMIZER, this field is optional in ADD operation.</div> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**criterion_type_feed_item** | [**FeedItemServiceCriterionTypeFeedItem**](FeedItemServiceCriterionTypeFeedItem.md) |  | [optional] 
**geo_restriction** | [**FeedItemServiceGeoRestriction**](FeedItemServiceGeoRestriction.md) |  | [optional] 
**is_remove** | [**FeedItemServiceIsRemove**](FeedItemServiceIsRemove.md) |  | [optional] 
**target_id** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;地域種別コードです。&lt;br&gt; このフィールドは、ADD時に必須となり、SET時に省略可能となり、REMOVE時に無視されます。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;FeedItemServiceLocation Type Code.&lt;br&gt; This field is required in ADD operation, is optional in SET operation, and will be ignored in REMOVE operation.&lt;/div&gt;  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



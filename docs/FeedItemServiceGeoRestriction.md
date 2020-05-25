# FeedItemServiceGeoRestriction

<div lang=\"ja\">FeedItemServiceGeoRestrictionオブジェクトは、地域設定の配信を制御します。<br> このフィールドは、ADDおよびSET時に省略可能となり、REMOVE時に無視されます。<br> ※ADD時のデフォルト設定値はNONEとなります。 </div> <div lang=\"en\">FeedItemServiceGeoRestriction object controls ad delivery of location restriction.<br> This field is optional in ADD and SET operation, and will be ignored in  REMOVE operation.<br> The default value in ADD operation will be NONE.</div> <hr> <p>* <code>NONE</code> - <span lang=\"ja\">検索キーワードとユーザーの所在地の関係にかかわらず、配信されます。</span><span lang=\"en\">Regardless of the relationship between the search keyword and the user&#39;s location, Ads will be delivered.</span></p> <p>* <code>LOCATION_OF_PRESENCE</code> - <span lang=\"ja\">検索キーワードがユーザーの所在地と無関係の場合は配信されません。</span><span lang=\"en\">Ads will not be delivered if the search keyword is unrelated to the user&#39;s location.</span></p> <p>* <code>UNKNOWN</code> - <span lang=\"ja\">未知の値です。</span><span lang=\"en\">Unknown Value</span></p> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



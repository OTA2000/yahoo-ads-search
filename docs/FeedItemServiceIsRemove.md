# FeedItemServiceIsRemove

<div lang=\"ja\">FeedItemServiceIsRemoveは、カスタムパラメータの削除フラグです。<br> customParametersおよびreviewCustomParameters配下の場合、このフィールドはSET時に省略可能となります。<br> locationオブジェクト配下の場合、このフィールドは、ADDおよびREMOVE時に無視され、SET時に省略可能となります。<br> ※地域設定を解除する場合は、locationオブジェクトのisRemoveにTRUEを指定します。<br> 地域設定解除後は、geoTargetingRestrictionにNONEが設定されます。</div> <div lang=\"en\">FeedItemServiceIsRemove is Delete flag.<br> Under customParameters and reviewCustomParameters, this field is optional in SET operation.<br> Under location object, this field will be ignored in ADD and REMOVE operation, and is optional in SET operation.<br> *To deactivate the location restriction, set isRemove of location object to TRUE.<br> After the deactivation, geoTargetingRestriction will be set to NONE.</div> <hr> <p>* <code>TRUE</code> - <span lang=\"ja\">カスタムパラメータの削除フラグがオンです。</span><span lang=\"en\">Delete flag is on.</span></p> <p>* <code>FALSE</code> - <span lang=\"ja\">カスタムパラメータの削除フラグがオフです。</span><span lang=\"en\">Delete flag is off.</span></p> <p>* <code>UNKNOWN</code> - <span lang=\"ja\">未知の値です。</span><span lang=\"en\">Unknown Value</span></p> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# FeedItemServiceDevicePreference

<div lang=\"ja\">FeedItemServiceDevicePreferenceは、広告を優先的に配信するデバイスを選択します。<br> このフィールドは、ADDおよびSET時に省略可能となり、REMOVE時に無視されます。<br> 電話番号オプションの場合、ADD時に省略可能となり、SET時に無視されます。<br> ※ADD時のデフォルト設定値はSMART_PHONEとなります。 </div> <div lang=\"en\">FeedItemServiceDevicePreference is a selection of device to deliver ads in high priority.<br> This field is optional in ADD and SET operation, and will be  ignored in REMOVE operation.<br> For CALLEXTENSION, this field is optional in ADD operation, and will be ignored in SET  operation.<br> *The default value for ADD operation will be SMART_PHONE.</div> <hr> <p>* <code>SMART_PHONE</code> - <span lang=\"ja\">スマートフォンを優先的に配信します。<br>作成（add）時のみご利用いただけます。<br>※優先デバイスの変更（set）・削除（remove）は実施できません。</span><span lang=\"en\">Deliver ads to Smartphone in higher priority<br>Available for add operation only<br>It cannot be used in set or remove operation</span></p> <p>* <code>NONE</code> - <span lang=\"ja\">指定なし</span><span lang=\"en\">not specified</span></p> <p>* <code>UNKNOWN</code> - <span lang=\"ja\">未知の値です。</span><span lang=\"en\">Unknown Value</span></p> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



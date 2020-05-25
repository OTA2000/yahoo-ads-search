# AdGroupServiceTargetAll

<div lang=\"ja\">AdGroupServiceTargetAllは、サイトリターゲティングにおける配信対象ユーザーの設定内容を表します。<br> ADDおよびSET時、このフィールドは必須となります。<br> ※TargetingSettingが未設定の場合、ADD時のデフォルト設定値はACTIVEとなります。</div> <div lang=\"en\">AdGroupServiceTargetAll describes the setting of target(include) users on Site Retargeting.<br> This field is required in ADD and SET operation.<br> *The default value in ADD operation for the case of no setting 'TargetingSetting' is ACTIVE.</div> <hr> <p>* <code>ACTIVE</code> - <span lang=\"ja\">すべてのユーザーを配信対象とします。<br>ターゲットリストのユーザーは入札価格調整率の適用のみ行います。</span><span lang=\"en\">All users are target of ad delivery.<br>Only applying bid adjustment rate is done for users on the Target List.</span></p> <p>* <code>DEACTIVE</code> - <span lang=\"ja\">ターゲットリストのユーザーのみを配信対象とします。<br>また、ターゲットリストのユーザーに対して入札価格調整率を適用します。</span><span lang=\"en\">Users on the Target List are target of ad delivery.<br>And bid adjustment rate is applied to users on the Target List.</span></p> <p>* <code>UNKNOWN</code> - <span lang=\"ja\">未知の値です。</span><span lang=\"en\">Unknown Value</span></p> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



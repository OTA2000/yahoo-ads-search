# FeedItemServiceCustomParameters

<div lang=\"ja\">FeedItemServiceCustomParametersオブジェクトは、カスタムパラメータの設定を表します。<br> CustomParametersおよびReviewCustomParameters配下では、このフィールドはレスポンスの際に返却されますが、リクエストの際には無視されます。<br> ※CustomParameters配下でのみ、クイックリンクオプションの場合、ADDおよびSET時に省略可能となります。</div> <div lang=\"en\">FeedItemServiceCustomParameters displays the setting of custom parameters.<br> Under customParameters and ReviewCustomParameters, this field will be  returned in the response, but it will be ignored on input.<br> *Under customParameters, this field will be optional  in ADD and SET operation for QUICKLINK option.</div> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_remove** | [**FeedItemServiceIsRemove**](FeedItemServiceIsRemove.md) |  | [optional] 
**parameters** | [**list[FeedItemServiceCustomParameter]**](FeedItemServiceCustomParameter.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



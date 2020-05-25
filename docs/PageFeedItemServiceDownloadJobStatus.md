# PageFeedItemServiceDownloadJobStatus

<div lang=\"ja\">PageFeedItemServiceDownloadJobStatusは、ページフィードアイテムダウンロードジョブの実行状況を表します。<br> このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。</div> <div lang=\"en\">PageFeedItemServiceDownloadJobStatus displays status of page feed item download jobs.<br> Although this field will be returned in the response, it will be ignored on input.</div> <hr> <p>* <code>IN_PROGRESS</code> - <span lang=\"ja\">処理中</span><span lang=\"en\">Currently in progress of creating.</span></p> <p>* <code>COMPLETED</code> - <span lang=\"ja\">処理完了</span><span lang=\"en\">Job has completed.</span></p> <p>* <code>FIELDS_ERROR</code> - <span lang=\"ja\">ダウンロード不可能なフィールドの組み合わせを指定した場合のエラー</span><span lang=\"en\">Error if invalid conbination.</span></p> <p>* <code>TIMEOUT</code> - <span lang=\"ja\">タイムアウト</span><span lang=\"en\">Timeout occured.</span></p> <p>* <code>SYSTEM_ERROR</code> - <span lang=\"ja\">エラー</span><span lang=\"en\">System error occured.</span></p> <p>* <code>UNKNOWN</code> - <span lang=\"ja\">未知の値です。</span><span lang=\"en\">Unknown Value</span></p> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



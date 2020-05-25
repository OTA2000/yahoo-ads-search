# AuditLogServiceJobStatus

<div lang=\"ja\">AuditLogServiceJobStatusは、操作履歴取得ジョブの実行状況を表します。<br> このフィールドは、job配下ではレスポンスの際に返却されますが、リクエストの際には無視されます。</div> <div lang=\"en\">AuditLogServiceJobStatus describes the job status of acquiring operation history data.<br> Under 'job', although this field will be returned in the response, it will be ignored on input.</div> <hr> <p>* <code>SYSTEM_ERROR</code> - <span lang=\"ja\">エラーです。</span><span lang=\"en\">It&#39;s error.</span></p> <p>* <code>IN_PROGRESS</code> - <span lang=\"ja\">処理中です。</span><span lang=\"en\">The process is in progress.</span></p> <p>* <code>COMPLETED</code> - <span lang=\"ja\">処理完了です。</span><span lang=\"en\">The process has been completed.</span></p> <p>* <code>TIMEOUT</code> - <span lang=\"ja\">タイムアウトです。</span><span lang=\"en\">Timeout occurred.</span></p> <p>* <code>UNKNOWN</code> - <span lang=\"ja\">未知の値です。</span><span lang=\"en\">Unknown Value</span></p> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



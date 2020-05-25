# PageFeedItemServiceJobValue

<div lang=\"ja\">PageFeedItemServiceJobValueは、upload、downloadの処理状況を格納するコンテナです。</div> <div lang=\"en\">PageFeedItemServiceJobValue retains a container of the processing situation results (upload/download).</div> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**download_job** | [**PageFeedItemServiceDownloadJob**](PageFeedItemServiceDownloadJob.md) |  | [optional] 
**errors** | [**list[Error]**](Error.md) |  | [optional] 
**operation_succeeded** | **bool** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;処理結果です。trueの場合は、処理は成功しました。falseの場合は処理が失敗しています。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;The process results. If true, the process succeeded. If false, the process failed.&lt;/div&gt;  | [optional] 
**upload_job** | [**PageFeedItemServiceUploadJob**](PageFeedItemServiceUploadJob.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



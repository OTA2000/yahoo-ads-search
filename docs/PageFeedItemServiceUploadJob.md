# PageFeedItemServiceUploadJob

<div lang=\"ja\">PageFeedItemServiceUploadJobオブジェクトは、ページフィードアイテム情報をダウンロードする処理内容を格納します。</div> <div lang=\"en\">PageFeedItemServiceUploadJob object retains contents of page feed item information for upload.</div> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;アカウントID&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Account ID&lt;/div&gt;  | [optional] 
**end_date** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;ジョブの終了日&lt;br&gt; 形式：yyyyMMddHHmmss&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;End date of job&lt;br&gt; Format:yyyyMMddHHmmss&lt;/div&gt;  | [optional] 
**error_count** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;エラーの件数&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;count of error occured&lt;/div&gt;  | [optional] 
**feed_ids** | **list[int]** |  | [optional] 
**job_id** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;ジョブID&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Job ID.&lt;/div&gt;  | [optional] 
**progress** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;ジョブの進捗状況&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Progress of page feed item job&lt;/div&gt;  | [optional] 
**start_date** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;ジョブの開始日&lt;br&gt; 形式：yyyyMMddHHmmss&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Start date of job&lt;br&gt; Format:yyyyMMddHHmmss&lt;/div&gt;  | [optional] 
**upload_job_status** | [**PageFeedItemServiceUploadJobStatus**](PageFeedItemServiceUploadJobStatus.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



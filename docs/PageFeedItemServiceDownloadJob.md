# PageFeedItemServiceDownloadJob

<div lang=\"ja\">PageFeedItemServiceDownloadJobオブジェクトは、ページフィードアイテム情報をダウンロードする処理内容を格納します。</div> <div lang=\"en\">PageFeedItemServiceDownloadJob object retains contents of page feed item information for download.</div> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;アカウントIDです。&lt;br&gt; このフィールドは必須です。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Account ID.&lt;br&gt; This field is required.&lt;/div&gt;  | [optional] 
**bulk_encoding** | [**PageFeedItemServiceBulkEncoding**](PageFeedItemServiceBulkEncoding.md) |  | [optional] 
**bulk_lang** | [**PageFeedItemServiceBulkLang**](PageFeedItemServiceBulkLang.md) |  | [optional] 
**bulk_output** | [**PageFeedItemServiceBulkOutput**](PageFeedItemServiceBulkOutput.md) |  | [optional] 
**download_job_status** | [**PageFeedItemServiceDownloadJobStatus**](PageFeedItemServiceDownloadJobStatus.md) |  | [optional] 
**end_date** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;ジョブの終了日です。&lt;br&gt; このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。&lt;br&gt; 形式：yyyyMMddHHmmss&lt;/div&gt;&lt;div lang&#x3D;\&quot;en\&quot;&gt;End date of job.&lt;br&gt; Although this field will be returned in the response, it will be ignored on input.  &lt;br&gt; Format:yyyyMMddHHmmss&lt;/div&gt;  | [optional] 
**feed_ids** | **list[int]** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;フィードIDです。&lt;br&gt; このフィールドは必須です。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Feed ID.&lt;br&gt; This field is required.&lt;/div&gt;  | [optional] 
**job_id** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;ジョブIDです。&lt;br&gt; このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Job ID.&lt;br&gt; Although this field will be returned in the response, it will be ignored on input.&lt;/div&gt;  | [optional] 
**progress** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;ジョブの進捗状況です。&lt;br&gt; このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Progress of page feed item job.&lt;br&gt; Although this field will be returned in the response, it will be ignored on input.&lt;/div&gt;  | [optional] 
**start_date** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;ジョブの開始日です。&lt;br&gt;このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。 &lt;br&gt; 形式：yyyyMMddHHmmss &lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Start date of job.&lt;br&gt; Although this field will be returned in the response, it will be ignored on input.&lt;br&gt; Format:yyyyMMddHHmmss&lt;/div&gt;  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# CampaignServiceUrlReviewData

<div lang=\"ja\">CampaignServiceUrlReviewDataオブジェクトは、URLの審査状況を表します。<br> このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。</div> <div lang=\"en\">CampaignServiceUrlReviewData object displays review status of URL.<br> Although this field will be returned in the response, it will be ignored on input.</div> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disapproval_reason_codes** | **list[str]** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;審査否認理由コードです。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Code of Disapproval reason.&lt;br&gt;&lt;/div&gt;  | [optional] 
**disapproval_review_url** | [**CampaignServiceReviewUrl**](CampaignServiceReviewUrl.md) |  | [optional] 
**in_review_url** | [**CampaignServiceReviewUrl**](CampaignServiceReviewUrl.md) |  | [optional] 
**url_approval_status** | [**CampaignServiceUrlApprovalStatus**](CampaignServiceUrlApprovalStatus.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



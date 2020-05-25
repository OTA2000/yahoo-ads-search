# KeywordEstimatorServiceCampaignEstimateRequest

<div lang=\"ja\">KeywordEstimatorServiceCampaignEstimateRequestオブジェクトは、見積もりを行うキャンペーンを格納するコンテナです。</div> <div lang=\"en\">KeywordEstimatorServiceCampaignEstimateRequest object is a container for a campaign to estimate.</div> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ad_group_estimate_requests** | [**list[KeywordEstimatorServiceAdGroupEstimateRequest]**](KeywordEstimatorServiceAdGroupEstimateRequest.md) | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;見積もりを行う広告グループを格納するコンテナです。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;A container for the Ad Group to estimate&lt;/div&gt;  | 
**campaign_id** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;キャンペーンIDです。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Campaign ID&lt;/div&gt;  | [optional] 
**daily_budget** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;見積もりで使用するキャンペーンの一日あたりの予算です。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Daily campaign budget used to estimate&lt;/div&gt;  | [optional] 
**provinces** | **list[str]** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;見積もりで使用する広告配信する指定地域（都道府県）です。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Province to serve Ads used to estimate&lt;/div&gt;  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



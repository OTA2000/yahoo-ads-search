# FeedItem

<div lang=\"ja\">FeedItemオブジェクトは、フィードアイテム情報を格納します。</div> <div lang=\"en\">FeedItem object contains the information of Feed Item.</div> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;アカウントIDです。&lt;br&gt; このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Account ID.&lt;br&gt; Although this field will be returned in the response, it will be ignored on input.&lt;/div&gt;  | [optional] 
**approval_status** | [**FeedItemServiceApprovalStatus**](FeedItemServiceApprovalStatus.md) |  | [optional] 
**custom_parameters** | [**FeedItemServiceCustomParameters**](FeedItemServiceCustomParameters.md) |  | [optional] 
**device_preference** | [**FeedItemServiceDevicePreference**](FeedItemServiceDevicePreference.md) |  | [optional] 
**disapproval_reason_codes** | **list[str]** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;審査否認理由です。&lt;br&gt; このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Reject reason on editorial review.&lt;br&gt; Although this field will be returned in the response, it will be ignored on input.&lt;/div&gt;  | [optional] 
**end_date** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;配信終了日です。&lt;br&gt;※空で設定すると、既存の配信終了日は削除されます。&lt;br&gt; このフィールドは、ADDおよびSET時に省略可能となり、REMOVE時に無視されます。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;End date of ad display.&lt;br&gt;∗By setting blank, existing end date of ad display will be deleted. &lt;br&gt;This field is optional in ADD and SET operation, and will be ignored in REMOVE operation.&lt;/div&gt;  | [optional] 
**feed_id** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;フィードIDです。&lt;br&gt; このフィールドはレスポンスの際に返却されますが、リクエストの際には無視されます。&lt;br&gt; ※アドカスタマイザーの場合は、ADD時に必須となります。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Feed ID.&lt;br&gt;Although this field will be returned in the response, it will be ignored on input.&lt;br&gt; *For AD_CUSTOMIZER, this field is required in ADD operation.&lt;/div&gt;  | [optional] 
**feed_item_attribute** | [**list[FeedItemServiceAttribute]**](FeedItemServiceAttribute.md) |  | [optional] 
**feed_item_id** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;フィードアイテムIDです。&lt;br&gt; このフィールドは、SETおよびREMOVE時に必須となり、ADD時に無視されます。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Feed Item ID.&lt;br&gt;This field is required in SET and REMOVE operation, and will be ignored in ADD operation.&lt;/div&gt;  | [optional] 
**feed_item_track_id** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;トラッキング用フィードアイテムIDです。&lt;br&gt; このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Feed Item ID for tracking.&lt;br&gt; Although this field will be returned in the response, it will be ignored on input.&lt;/div&gt;  | [optional] 
**invalided_trademarks** | **list[str]** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;制限された商標です。&lt;br&gt; このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。 &lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Invalided trademarks.&lt;br&gt; Although this field will be returned in the response, it will be ignored on input.&lt;/div&gt;  | [optional] 
**location** | [**FeedItemServiceLocation**](FeedItemServiceLocation.md) |  | [optional] 
**placeholder_type** | [**FeedItemServicePlaceholderType**](FeedItemServicePlaceholderType.md) |  | [optional] 
**review_custom_parameters** | [**FeedItemServiceCustomParameters**](FeedItemServiceCustomParameters.md) |  | [optional] 
**scheduling** | [**FeedItemServiceScheduling**](FeedItemServiceScheduling.md) |  | [optional] 
**start_date** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;配信開始日です。&lt;br&gt; ※空で設定すると、既存の配信開始日は削除されます。&lt;br&gt; このフィールドは、ADDおよびSET時に省略可能となり、REMOVE時に無視されます。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Start date of ad display&lt;br&gt; ∗On setting blank, existing start date of ad display will be deleted.&lt;br&gt; This field is optional in ADD and SET operation, and will be ignored in REMOVE operation.&lt;/div&gt;  | [optional] 
**targeting_ad_group** | [**FeedItemServiceTargetingAdGroup**](FeedItemServiceTargetingAdGroup.md) |  | [optional] 
**targeting_campaign** | [**FeedItemServiceTargetingCampaign**](FeedItemServiceTargetingCampaign.md) |  | [optional] 
**targeting_keyword** | [**FeedItemServiceTargetingKeyword**](FeedItemServiceTargetingKeyword.md) |  | [optional] 
**trademark_status** | [**FeedItemServiceTrademarkStatus**](FeedItemServiceTrademarkStatus.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



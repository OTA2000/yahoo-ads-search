# AdGroupAdServiceAd

<div lang=\"ja\">AdGroupAdServiceAdオブジェクトは、広告に関する情報を表します。<br> ADD時、このフィールドは必須となります。</div> <div lang=\"en\">AdGroupAdServiceAd object describes ad information.<br> This field is required in ADD operation.</div> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ad_type** | [**AdGroupAdServiceAdType**](AdGroupAdServiceAdType.md) |  | [optional] 
**additional_advanced_mobile_urls** | [**list[AdGroupAdServiceAdditionalAdvancedMobileUrls]**](AdGroupAdServiceAdditionalAdvancedMobileUrls.md) |  | [optional] 
**additional_advanced_urls** | [**list[AdGroupAdServiceAdditionalAdvancedUrls]**](AdGroupAdServiceAdditionalAdvancedUrls.md) |  | [optional] 
**advanced_mobile_url** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;最終リンク先URL（スマートフォン）です。&lt;br&gt; ADD時、このフィールドは省略可能となります。※adTypeがDYNAMIC_SEARCH_LINKED_ADの場合は無視されます。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Landing Page URL (Smartphone).&lt;br&gt; This field is optional in ADD operation. *If adType is DYNAMIC_SEARCH_LINKED_AD, this field will be ignored.&lt;/div&gt;  | [optional] 
**advanced_url** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;最終リンク先URLです。&lt;br&gt; ADD時、このフィールドは必須となります。※adTypeがDYNAMIC_SEARCH_LINKED_ADの場合は無視されます。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Landing Page URL.&lt;br&gt; This field is required in ADD operation. *If adType is DYNAMIC_SEARCH_LINKED_AD, this field will be ignored.&lt;/div&gt;  | [optional] 
**app_ad** | [**AdGroupAdServiceAppAd**](AdGroupAdServiceAppAd.md) |  | [optional] 
**custom_parameters** | [**AdGroupAdServiceCustomParameters**](AdGroupAdServiceCustomParameters.md) |  | [optional] 
**description** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;説明文です。&lt;br&gt; ADD時、このフィールドは必須となります。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Description of ad.&lt;br&gt; This field is required in ADD operation.&lt;/div&gt;  | [optional] 
**device_preference** | [**AdGroupAdServiceDevicePreference**](AdGroupAdServiceDevicePreference.md) |  | [optional] 
**display_url** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;表示URLです。&lt;br&gt; このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Display URL.&lt;br&gt; Although this field will be returned in the response, it will be ignored on input.&lt;/div&gt;  | [optional] 
**extended_text_ad** | [**AdGroupAdServiceExtendedTextAd**](AdGroupAdServiceExtendedTextAd.md) |  | [optional] 
**headline** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;タイトル文です。&lt;br&gt; ADD時、このフィールドは必須となります。※adTypeがDYNAMIC_SEARCH_LINKED_ADの場合は無視されます。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Title of ad.&lt;br&gt; This field is required in ADD operation. *If adType is DYNAMIC_SEARCH_LINKED_AD, this field will be ignored.&lt;/div&gt;  | [optional] 
**text_ad2** | [**AdGroupAdServiceTextAd2**](AdGroupAdServiceTextAd2.md) |  | [optional] 
**tracking_url** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;トラッキングURLです。&lt;br&gt; ADD時、このフィールドは省略可能となります。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Tracking URL.&lt;br&gt; This field is optional in ADD operation.&lt;/div&gt;  | [optional] 
**url** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;移行前のリンク先URLです。&lt;br&gt; このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Destination URL before upgrading. &lt;br&gt; Although this field will be returned in the response, it will be ignored on input.&lt;/div&gt;  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



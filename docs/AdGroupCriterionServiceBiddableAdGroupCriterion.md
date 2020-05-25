# AdGroupCriterionServiceBiddableAdGroupCriterion

<div lang=\"ja\">AdGroupCriterionServiceBiddableAdGroupCriterionオブジェクトは、広告グループの単価設定可能（包含）クライテリアです。</div> <div lang=\"en\">AdGroupCriterionServiceBiddableAdGroupCriterion object displays biddable criterion in ad group.</div> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_advanced_mobile_urls** | [**AdGroupCriterionServiceAdditionalAdvancedMobileUrls**](AdGroupCriterionServiceAdditionalAdvancedMobileUrls.md) |  | [optional] 
**additional_advanced_urls** | [**AdGroupCriterionServiceAdditionalAdvancedUrls**](AdGroupCriterionServiceAdditionalAdvancedUrls.md) |  | [optional] 
**advanced_mobile_url** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;カスタムURL（スマートフォン）です。&lt;br&gt; ADDおよびSET時、このフィールドは省略可能となります。&lt;br&gt; ※空で設定すると、既存のカスタムURL（スマートフォン）は削除されます。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Upgraded Custom URL (Smartphone).&lt;br&gt; This field is optional in ADD and SET operation.&lt;br&gt; *When tag is set blank, existing upgraded Custom URL (Smartphone) will be deleted.&lt;/div&gt;  | [optional] 
**advanced_url** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;移行後のカスタムURLです。&lt;br&gt; ADDおよびSET時、このフィールドは省略可能となります。※ADD時、移行してtracking Urlを指定している場合は必須となります。&lt;br&gt; ※空で設定すると、既存の移行後のカスタムURLは削除されます。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Upgraded Custom URL.&lt;br&gt; This field is optional in ADD and SET operation. *If upgraded and tracking Url is specified, it is required in ADD operation.&lt;br&gt; *When this is set blank, existing upgraded Custom URL will be deleted.&lt;/div&gt;  | [optional] 
**approval_status** | [**AdGroupCriterionServiceApprovalStatus**](AdGroupCriterionServiceApprovalStatus.md) |  | [optional] 
**bid** | [**AdGroupCriterionServiceBid**](AdGroupCriterionServiceBid.md) |  | [optional] 
**custom_parameters** | [**AdGroupCriterionServiceCustomParameters**](AdGroupCriterionServiceCustomParameters.md) |  | [optional] 
**destination_url** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;移行前のカスタムURLです。&lt;br&gt; ADDおよびSET時、このフィールドは省略可能となります。&lt;br&gt; ※空で設定すると、既存の移行前のカスタムURLは削除されます。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Custom URL of before upgrading.&lt;br&gt; This field is optional in ADD and SET operation.&lt;br&gt; *When tag is set blank, existing Custom URL before upgrade will be deleted.&lt;/div&gt;  | [optional] 
**disapproval_reason_codes** | **list[str]** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;審査否認コードです。&lt;br&gt; (コード詳細は、DictionaryServiceのgetDisapprovalReasonのレスポンスを参照)&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Code of Disapproval reason.&lt;br&gt; (Refer to DictionaryService getDisapprovalReason response for details)&lt;/div&gt;  | [optional] 
**review_advanced_mobile_url** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;配信審査中のカスタムURL（スマートフォン）です。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Upgraded Custom URL (Smartphone), in review.&lt;/div&gt;  | [optional] 
**review_advanced_url** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;移行後の配信審査中のカスタムURLです。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Upgraded Custom URL, in review.&lt;/div&gt;  | [optional] 
**review_custom_parameters** | [**AdGroupCriterionServiceCustomParameters**](AdGroupCriterionServiceCustomParameters.md) |  | [optional] 
**review_destination_url** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;移行前の配信審査中のカスタムURLです。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Custom URL of before upgrading, in review.&lt;/div&gt;  | [optional] 
**review_tracking_url** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;配信審査中のトラッキングURLです。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Tracking URL, in review.&lt;/div&gt;  | [optional] 
**tracking_url** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;トラッキングURLです。&lt;br&gt; ADDおよびSET時、このフィールドは省略可能となります。&lt;br&gt; ※空で設定すると、既存のトラッキングURLは削除されます。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Tracking URL.&lt;br&gt; This field is optional in ADD and SET operation.&lt;br&gt; *When tag is set blank, existing Tracking URL will be deleted.&lt;/div&gt;  | [optional] 
**user_status** | [**AdGroupCriterionServiceUserStatus**](AdGroupCriterionServiceUserStatus.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



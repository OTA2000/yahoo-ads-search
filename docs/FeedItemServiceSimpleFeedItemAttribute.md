# FeedItemServiceSimpleFeedItemAttribute

<div lang=\"ja\">このフィールドは、ADDおよびSET時に省略可能となり、REMOVE時に無視されます。<br> ※placeholderFieldがSTRUCTURED_SNIPPET_VALUES, ADDITIONAL_ADVANCED_URLS, ADDITIONAL_ADVANCED_MOBILE_URLSの場合、ADDおよびSET時に必須となります。</div> <div lang=\"en\">This field is optional in ADD and SET operation, and will be ignored in REMOVE operation.<br> If the placeholderField is STRUCTURED_SNIPPET_VALUES, ADDITIONAL_ADVANCED_URLS, or ADDITIONAL_ADVANCED_MOBILE_URLS, this field is required in ADD and SET operation.</div> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**feed_attribute_value** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;フィードアイテム情報の値です。&lt;br&gt;&lt;br&gt; ※データ自動挿入の利用時は、属性は以下のように入力してください：&lt;br&gt; ・AD_CUSTOMIZER_INTEGER&lt;br&gt; ex) 99999999&lt;br&gt;・AD_CUSTOMIZER_PRICE&lt;br&gt; ex) 19800 or 19,800&lt;br&gt; ・AD_CUSTOMIZER_DATE&lt;br&gt; ex) 20151231 235959&lt;br&gt; ・AD_CUSTOMIZER_STRING&lt;br&gt; ex) hoge ・STRUCTURED_SNIPPET_HEADER&lt;br&gt; ex) ブランド&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Value of feed iteim information.&lt;br&gt;&lt;br&gt; *When using data insertion, you need to enter attribution as follows:&lt;br&gt; ・AD_CUSTOMIZER_INTEGER&lt;br&gt; ex) 99999999&lt;br&gt; ・AD_CUSTOMIZER_PRICE&lt;br&gt; ex) 19800 or 19,800&lt;br&gt; ・AD_CUSTOMIZER_DATE&lt;br&gt; ex) 20151231 235959&lt;br&gt; ・AD_CUSTOMIZER_STRING&lt;br&gt; ex) home&lt;br&gt; ・STRUCTURED_SNIPPET_HEADER&lt;br&gt; ex) brand&lt;/div&gt;  | [optional] 
**review_feed_attribute_value** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;審査中のフィードアイテム情報です。&lt;br&gt; ※審査中の間のみ、レスポンス時に表示されます。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;The feed item information on editorial review.&lt;br&gt; *It is displayed for response only on Editorial Review.&lt;/div&gt;  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# AdGroupCriterionServiceBid

<div lang=\"ja\">AdGroupCriterionServiceBidオブジェクトは、入札価格を表示します。 （AdGroupCriterionService用のオブジェクトです。）<br> ADDおよびSET時、このフィールドは省略可能となります。</div> <div lang=\"en\">AdGroupCriterionServiceBid object displays the bid values. *Object for AdGroupCriterionService.<br> This field is optional in ADD and SET operation.</div> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ad_group_max_cpc** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;広告グループ入札価格です。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;CPC of Ad group.&lt;/div&gt;  | [optional] 
**bid_source** | [**AdGroupCriterionServiceBidSource**](AdGroupCriterionServiceBidSource.md) |  | [optional] 
**keyword_max_cpc** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;キーワード入札価格です。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;CPC of Keyword.&lt;/div&gt;  | [optional] 
**max_cpc** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;キーワード入札価格です。&lt;br&gt; このフィールドは、省略可能となります。その際、ADD時のデフォルト設定値は1となります。&lt;br&gt; ※maxCpcが0の場合は、設定なしと同様です。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;CPC of Keyword.&lt;br&gt; This field is optional. The default value in ADD operation will be 1.&lt;br&gt; *Confirmed as no setting, if value is set &amp;#34;0&amp;#34;.&lt;/div&gt;  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



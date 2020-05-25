# AdGroupAdServiceExtendedTextAd

<div lang=\"ja\">AdGroupAdServiceExtendedTextAdオブジェクトは、拡大テキスト広告に関する情報を表します。<br> ADD時、このフィールドは省略可能となります。※adTypeがEXTENDED_TEXT_ADの場合は必須です。</div> <div lang=\"en\">AdGroupAdServiceExtendedTextAd object describes the information of Extended Text Ad.<br> This field is optional in ADD operation. *If adType is EXTENDED_TEXT_AD, this field is required.</div> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**headline2** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;2行目のタイトルです。&lt;br&gt; ADD時、このフィールドは必須となります。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Title on the second line.&lt;br&gt; This field is required in ADD operation.&lt;/div&gt;  | [optional] 
**headline3** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;3行目のタイトルです。&lt;br&gt; ADD時、このフィールドは省略可能となります。その際、デフォルト設定値はnullとなります。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Title on the second line.&lt;br&gt; This field is optional in ADD operation. The default value will be null.&lt;/div&gt;  | [optional] 
**description2** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;2行目の説明文です。&lt;br&gt; ADD時、このフィールドは省略可能となります。その際、デフォルト設定値はnullとなります。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Description on the second line.&lt;br&gt; This field is optional in ADD operation. The default value will be null.&lt;/div&gt;  | [optional] 
**path1** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;自動作成される表示URLを補足するパスです。&lt;br&gt; ADD時、このフィールドは省略可能となります。その際、デフォルト設定値はnullとなります。&lt;br&gt;※path2を指定する場合は、path1は必須です。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;The path information which complements display URL generated automatically.&lt;br&gt; This field is optional in ADD operation. The default value will be null.&lt;br&gt;*To specify path2, path1 is required.&lt;/div&gt;  | [optional] 
**path2** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;自動作成される表示URLを補足するパスです。&lt;br&gt; ADD時、このフィールドは省略可能となります。その際、デフォルト設定値はnullとなります。&lt;br&gt;※path1を指定していない場合、path2は無視されます。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;The path information which complements display URL generated automatically.&lt;br&gt; This field is optional in ADD operation. The default value will be null.&lt;br&gt;*If path1 is not specified, path2 will be ignored.&lt;/div&gt;  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



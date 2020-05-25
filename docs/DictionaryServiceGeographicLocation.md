# DictionaryServiceGeographicLocation

<div lang=\"ja\">DictionaryServiceGeographicLocationオブジェクトは、地域情報を格納します。</div> <div lang=\"en\">DictionaryServiceGeographicLocation contains geographic location information.</div> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**child** | [**list[DictionaryServiceGeographicLocation]**](DictionaryServiceGeographicLocation.md) |  | [optional] 
**code** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;地域コードです。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Geographic code&lt;/div&gt;  | [optional] 
**full_name** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;地域名(都道府県名からすべて)です。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Name of places (Prefecture and all)&lt;/div&gt;  | [optional] 
**geographic_location_status** | [**DictionaryServiceGeographicLocationStatus**](DictionaryServiceGeographicLocationStatus.md) |  | [optional] 
**name** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;地域名(市区町村のみ)です。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Name of places (City Only)&lt;/div&gt;  | [optional] 
**order** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;並び順です。&lt;br&gt;下記の順序に基づいた連番となります。&lt;br&gt; 都道府県は北海道、青森、・・・・沖縄の順&lt;br&gt;都道府県配下の市区町村は五十音順&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Order of list&lt;br&gt;&lt;br&gt;Sequential number based on the order below.&lt;br&gt;&lt;br&gt; - Prefecture is in order of Hokkaido, Aomori to Okinawa. (North to South)&lt;br&gt;&lt;br&gt; - Cities under prefecture are listed in the order of the 50-character Japanese kana syllabary.&lt;/div&gt;  | [optional] 
**parent** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;上位地域コードです。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Parent geographic code&lt;/div&gt;  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



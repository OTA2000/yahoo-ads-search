# OfflineConversionServiceSelector

<div lang=\"ja\">OfflineConversionServiceSelectorオブジェクトは、登録したオフラインコンバージョンデータを照会するための検索条件を格納します。</div> <div lang=\"en\">OfflineConversionServiceSelector object contains search condition to inquire about registered offline conversion data.</div> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;検索条件：アカウントIDです。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Search conditon: Account ID.&lt;/div&gt;  | 
**upload_ids** | **list[int]** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;検索条件：アップロードIDです。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Search conditon: Upload ID.&lt;/div&gt;  | [optional] 
**sorts** | [**list[OfflineConversionServiceSort]**](OfflineConversionServiceSort.md) |  | [optional] 
**number_results** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;ページの最大件数です。このフィールドは、1以上を指定する必要があります。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Maximum number of results to return in this page. This field must be greater than or equal to 1. Also see Entity Limits per operation.&lt;/div&gt;  | [optional] [default to 500]
**start_index** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;ページの先頭のインデックスです。このフィールドは、1以上を指定する必要があります。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Index of the first result to return in this page. This field must be greater than or equal to 1.&lt;/div&gt;  | [optional] [default to 1]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



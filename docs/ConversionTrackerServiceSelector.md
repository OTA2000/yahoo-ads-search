# ConversionTrackerServiceSelector

<div lang=\"ja\">ConversionTrackerServiceSelectorオブジェクトは、操作の対象となるコンバージョントラッカーおよび操作を指定します。</div> <div lang=\"en\">ConversionTrackerServiceSelector object specifies ConversionTracker and operation.</div> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;アカウントIDです。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Account ID.&lt;/div&gt;  | 
**app_ids** | **list[str]** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;アプリケーションIDです。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;App ID.&lt;/div&gt;  | [optional] 
**categories** | [**list[ConversionTrackerServiceCategory]**](ConversionTrackerServiceCategory.md) |  | [optional] 
**conversion_counting_types** | [**list[ConversionTrackerServiceConversionCountingType]**](ConversionTrackerServiceConversionCountingType.md) |  | [optional] 
**conversion_date_range** | [**ConversionTrackerServiceConversionDateRange**](ConversionTrackerServiceConversionDateRange.md) |  | [optional] 
**conversion_tracker_ids** | **list[int]** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;コンバージョントラッカーIDです。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Conversion Tracker ID.&lt;/div&gt;  | [optional] 
**conversion_tracker_types** | [**list[ConversionTrackerServiceConversionTrackerType]**](ConversionTrackerServiceConversionTrackerType.md) |  | [optional] 
**exclude_from_biddings** | [**list[ConversionTrackerServiceExcludeFromBidding]**](ConversionTrackerServiceExcludeFromBidding.md) |  | [optional] 
**number_results** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;ページの最大件数です。このフィールドは、1以上を指定する必要があります。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Maximum number of results to return in this page. This field must be greater than or equal to 1. Also see Entity Limits per operation.&lt;/div&gt;  | [optional] [default to 500]
**start_index** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;ページの先頭のインデックスです。このフィールドは、1以上を指定する必要があります。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Index of the first result to return in this page. This field must be greater than or equal to 1.&lt;/div&gt;  | [optional] [default to 1]
**statuses** | [**list[ConversionTrackerServiceStatus]**](ConversionTrackerServiceStatus.md) |  | [optional] 
**tracking_code_types** | [**list[ConversionTrackerServiceTrackingCodeType]**](ConversionTrackerServiceTrackingCodeType.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



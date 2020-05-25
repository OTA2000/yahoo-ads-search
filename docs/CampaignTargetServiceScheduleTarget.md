# CampaignTargetServiceScheduleTarget

<div lang=\"ja\">CampaignTargetServiceScheduleTargetオブジェクトは、曜日・時間帯ターゲティングレポートを表します。<br> このフィールドは、ADD時およびSET時に省略可能となります。<br> ※targetTypeがSCHEDULEの場合、このフィールドはADD時に必須となります。</div> <div lang=\"en\">CampaignTargetServiceScheduleTarget describes Day of week/Hour targeting report.<br> *This field is optional in ADD and SET operation.<br> If targetType is SCHEDULE, this field is required in ADD operation.</div> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**day_of_week** | [**CampaignTargetServiceDayOfWeek**](CampaignTargetServiceDayOfWeek.md) |  | [optional] 
**end_hour** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;24時間表示の終了時刻です。&lt;br&gt;このフィールドは、ADD時に必須となります。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Ending hour in 24 hour time.&lt;br&gt;This field is required in ADD operation.&lt;/div&gt;  | [optional] 
**end_minute** | [**CampaignTargetServiceMinuteOfHour**](CampaignTargetServiceMinuteOfHour.md) |  | [optional] 
**start_hour** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;24時間表示の開始時刻です。&lt;br&gt;このフィールドは、ADD時に必須となります。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Starting hour in 24 hour time.&lt;br&gt;This field is required in ADD operation.&lt;/div&gt;  | [optional] 
**start_minute** | [**CampaignTargetServiceMinuteOfHour**](CampaignTargetServiceMinuteOfHour.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



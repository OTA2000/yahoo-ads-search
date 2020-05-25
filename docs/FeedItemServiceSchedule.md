# FeedItemServiceSchedule

<div lang=\"ja\">FeedItemServiceScheduleオブジェクトは、広告表示オプションの配信スケジュール設定を表します。<br> このフィールドは、ADDおよびSET時に省略可能となります。</div> <div lang=\"en\">FeedItemServiceSchedule object describes display schedule from Ad Display Option.<br> This field is optional in ADD and SET operation.</div> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**day_of_week** | [**FeedItemServiceDayOfWeek**](FeedItemServiceDayOfWeek.md) |  | [optional] 
**end_hour** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;終了時です。&lt;br&gt; ※0 ～ 24の範囲で設定してください。&lt;br&gt; このフィールドは、ADDおよびSET時に必須となります。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;End time in hour.&lt;br&gt; *Specify from 0 - 24.&lt;br&gt; This field is required in ADD and SET operation.&lt;/div&gt;  | [optional] 
**end_minute** | [**FeedItemServiceMinuteOfHour**](FeedItemServiceMinuteOfHour.md) |  | [optional] 
**start_hour** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;開始時です。&lt;br&gt; ※0 ～ 23の範囲で設定してください。&lt;br&gt; このフィールドは、ADDおよびSET時に必須となります。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Start time in hour.&lt;br&gt;*Specify from 0 - 23.&lt;br&gt; This field is required in ADD and SET operation.&lt;/div&gt;  | [optional] 
**start_minute** | [**FeedItemServiceMinuteOfHour**](FeedItemServiceMinuteOfHour.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



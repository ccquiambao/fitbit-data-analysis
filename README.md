# fitbit-data-analysis
Analyze sleep and heart rate logs recorded by Fitbit

Currently:
- Uses python-fitbit to access Fitbit API and pull sleep logs
- Pulls sleep logs for one week and accesses main sleep data (excludes naps)
- Uses Pandas to dispay sleep duration and bed time in Hours:Minutes:Seconds
- Displays average sleep duration and bed time during one week

## Future Goals

For API:
- Learn how to access API w/o python-fitbit (use python-oauth2)
- Access different data (heart rate, minute-by-minute sleep data)

For sleep data:
- Graph sleep duration and bed time using Matplotlib (learn Matplotlib, use Pandas better)
- Graph minute-by-minute sleep data, visualize sleep cycles per day (access min-by-min data, learn Matplotlib)

For heart rate data:
- Pull heart rate data (use python-fitbit, better is to access API directly)
- Visualize heart rate data using Matplotlib (learn Matplotlib)
- Try to find times of transitions in heart rate programmatically (first access data)

For both sets of data:
- First learn Raspberry Pi
- Schedule Raspberry Pi to run scripts weekly
- Store data for week
   -create database of every week's data (probably can do w/ python sqlite3)
   -find running averages/stats
- Email weekly stats to self (can't guarantee I'll read this email)

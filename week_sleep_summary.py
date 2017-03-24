import fitbit
import pandas as pd
from datetime import datetime, date, time, timedelta

'''
Rudimentary analysis of sleep data from personal fitbit.

Uses fitbit module to connect to Fitbit API and pull sleep logs.
Uses datetime library to make data more readable
Uses pandas to display and find averages of data
'''

# Uses personal fitbit account information to access Fitbit API
authd_client = fitbit.Fitbit(OAuthTwoClientID, ClientSecret, oauth2=True,
                             access_token=AccessToken, refresh_token=RefreshToken)


def get_raw_week_sleep():
    '''
    Pulls raw sleep logs for last seven days, returned as a list of dictionaries
    '''
    week_sleep_data = []
    week_date_range = (date.today() - timedelta(days = x) for x in xrange(7))
    for day in week_date_range:
        day_sleep_data = authd_client.sleep(date=day)
        week_sleep_data.append(day_sleep_data)
    return week_sleep_data

def get_useful_sleep(raw_data):
    '''
    Accesses main sleep information from sleep logs
    '''
    return [day['sleep'][0] for day in week_sleep_data]

def start_time_convert(start_time):
    '''
    Starting bed time is given as '2011-06-16T00:00:00.000' format.
    Return only time portion
    '''
    return datetime.strptime(start_time[-12:-4], '%H:%M:%S').time()

def start_time_total_seconds(start_time):
    '''
    Convert '12:23:45' to total seconds for math operations
    '''
    return start_time.hour * 3600 + start_time.minute * 60 + start_time.second

def seconds_to_time(seconds):
    '''
    Convert total seconds to number of hours, minutes, seconds
    '''
    seconds = int(seconds)
    hours, minutes = divmod(seconds, 3600)
    minutes,seconds = divmod(minutes, 60)
    return time(hours,minutes,seconds)

def ms_duration_to_hours(duration_seconds):
    '''
    Duration data is given in ms. Converts to hours,minutes, seconds
    '''
    duration_seconds = int(duration_seconds)
    hours, minutes = divmod(duration_seconds, 3600000)
    minutes,seconds = divmod(minutes, 60000)
    seconds = seconds // 1000
    return time(hours,minutes,seconds)

if __name__ == '__main__':
    # Get main sleep data, create DataFrame
    week_sleep_data = get_raw_week_sleep()
    week_cleaned_list = get_useful_sleep(week_sleep_data)
    df = pd.DataFrame(week_cleaned_list)

    # Convert duration (ms) to number of hours, find average duration
    df['duration_hours'] = df['duration'].apply(ms_duration_to_hours)
    avg_duration = df['duration'].mean()
    avg_duration = ms_duration_to_hours(avg_duration)

    # Convert startTime to time-only value, create new column of startTime in seconds
    df['startTime'] = df['startTime'].apply(start_time_convert)
    df['start_time_seconds']= df['startTime'].apply(start_time_total_seconds)
    avg_bed_time = seconds_to_time(df['start_time_seconds'].mean())

    # Display only desired data
    duration_start_time_col = ['dateOfSleep','duration_hours','startTime']
    print df[duration_start_time_col]
    print 'Average bed time: {}'.format(avg_bed_time)
    print 'Average sleep duration: {}'.format(avg_duration)

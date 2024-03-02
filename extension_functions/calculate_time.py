import datetime 

def calculate_target_time_offset(hour, minute):
    now = datetime.datetime.now()
    target_time_today = datetime.datetime(now.year, now.month, now.day, hour, minute)
    if now >= target_time_today:
        target_time_tomorrow = target_time_today + datetime.timedelta(days=1)
        return (target_time_tomorrow - now).total_seconds()
    else:
        return (target_time_today - now).total_seconds()
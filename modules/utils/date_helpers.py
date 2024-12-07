from datetime import datetime, timedelta

def get_current_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def get_export_timestamp():
    return datetime.now().strftime("%Y%m%d_%H%M%S")

def parse_timestamp(timestamp_str):
    return datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")

def get_default_date_range():
    end_date = datetime.now().date()
    start_date = end_date.replace(day=1)
    return start_date, end_date
import pytz

def get_timezone(country):
    if country == "INDIA":
        return pytz.timezone('Asia/Kolkata')
    elif country == "USA":
        return pytz.timezone('US/Central')
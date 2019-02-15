import datetime


def get_formatted_date():
    date = datetime.datetime.now()
    return date.strftime('%Y-%m-%d %H:%M:%S')

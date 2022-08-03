from datetime import datetime


def timestamp_checker(timestamp):
    
    timestamp_format = "%d %b %Y %H:%M"
    timestamp_now = datetime.now().replace(microsecond=0)
    try:
        timestamp = datetime.strptime(timestamp, timestamp_format)
        if timestamp <= timestamp_now:
            return False
        else:
            return True
    except ValueError:
        return False

def send_email():
    # function to send email
    
    pass

def scheduler():
    # queue system for sending emails based on timestamp
    
    pass
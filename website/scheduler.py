from datetime import datetime
from flask import Flask
from . import db
from flask_apscheduler import APScheduler
from apscheduler.schedulers.background import BackgroundScheduler


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

def send_email(event_id):
    # function to send email can be added later because it needs email credentials to configure
    print(f'email with event_id={event_id} has been sent')


def scheduled_task(event_id, timestamp):
    scheduler = BackgroundScheduler()
    timestamp_format = "%d %b %Y %H:%M"
    scheduler.add_job(send_email, 'date', run_date=datetime.strptime(timestamp, timestamp_format), args=[event_id])
    scheduler.start()
    print(f'email with event_id={event_id} has been scheduled to send at {timestamp}')
from datetime import datetime as dt
from flask import Flask
import pytz
from . import db
from flask_apscheduler import APScheduler
from apscheduler.schedulers.background import BackgroundScheduler


def timestamp_checker(timestamp):
    
    timestamp_format = "%d %b %Y %H:%M"
    timezone = pytz.timezone('Asia/Singapore')
    timestamp_now = dt.now(timezone)
    try:
        timestamp = timezone.localize(dt.strptime(timestamp, timestamp_format))
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
    timezone = pytz.timezone('Asia/Singapore')
    timestamp_format = "%d %b %Y %H:%M"
    scheduler.add_job(send_email,
                      'date', 
                      run_date=timezone.localize(dt.strptime(timestamp, timestamp_format)), 
                      args=[event_id])
    scheduler.start()
    print(f'email with event_id={event_id} has been scheduled to send at {timestamp} UTC+8 time.')
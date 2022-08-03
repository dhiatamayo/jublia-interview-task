from flask import Blueprint, render_template, request, flash
from sqlalchemy import exc
from .models import Email
from .scheduler import timestamp_checker, scheduled_task
from . import db

views = Blueprint('views', __name__)
    
@views.route('/', methods=['GET'])
def home():
    return render_template("home.html")

@views.route('/save_emails', methods=['GET', 'POST'])
def save_emails():
    
    if request.method == 'POST':
        try:
            event_id = request.form.get('event_id')
            email_subject = request.form.get('email_subject')
            email_content = request.form.get('email_content')
            timestamp = request.form.get('timestamp')
            
            if event_id.isdigit() == False:
                flash('Event Id must be integer', category='error') 
            elif int(event_id) < 1:
                flash('Event Id must be greater than 0') 
            elif email_subject == '' or email_content == '' or timestamp == '':
                flash('Please fill all the forms', category='error') 
            elif len(email_subject) > 150:
                flash('Email Subject cannot be longer than 150 characters', category='error')
            elif len(email_content) > 2000:
                flash('Email Content cannot be longer than 2000 characters', category='error')
            elif timestamp_checker(timestamp) == False:
                flash('Timestamp is in the past or format is incorrect', category='error')
            else:
                new_email = Email(event_id=event_id, 
                                  email_subject=email_subject, 
                                  email_content=email_content, 
                                  timestamp=timestamp)
                db.session.add(new_email)
                db.session.commit()                
                flash('Email saved!', category='success')
                
                scheduled_task(event_id, timestamp)
            
        except exc.IntegrityError:
            flash('Event Id already exists', category='error')
            
    return render_template('saveEmails.html')
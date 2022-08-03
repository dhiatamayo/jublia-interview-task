from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_apscheduler import APScheduler
from apscheduler.schedulers.background import BackgroundScheduler
from os import path

db = SQLAlchemy()
DB_NAME = 'emails.db'

scheduler = BackgroundScheduler()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '12345678'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)
    
    from .views import views
    
    app.register_blueprint(views, url_prefix='/')
    
    from .models import Email
    
    create_database(app)
    
    return app

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created database!')
        
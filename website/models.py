from . import db


class Email(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer, unique=True)
    email_subject = db.Column(db.String(150), nullable=False)
    email_content = db.Column(db.String(2000), nullable=False)
    timestamp = db.Column(db.String(), nullable=False)

# import datetime
# import requests
# from flask import Flask, request
# from flask_restful import Resource, Api, reqparse
# import sqlite3 as sql
from website import create_app


# class SaveEmail():
    
#     con = sql.connect('email.db', check_same_thread=False)
#     cur = con.cursor()
    
#     def __init__(self, event_id, email_subject, email_content, timestamp):
#         self.event_id = event_id
#         self.email_subject = email_subject
#         self.email_content = email_content
#         self.timestamp = timestamp
        
#     def create_table(self):
#         self.cur.execute('''CREATE TABLE IF NOT EXISTS emails
#                 (event_id integer PRIMARY KEY, email_subject TEXT, email_content TEXT, timestamp TEXT)''')

#     def insert_data(self):
#         self.cur.execute(f'''INSERT INTO emails (email_subject,email_content,timestamp) VALUES
#                 ('{self.email_subject}', '{self.email_content}', '{self.timestamp}')''')
#         self.con.commit()
#         print('data inserted to table')

#     def show_data(self):
#         for row in self.cur.execute('''SELECT * FROM emails'''):
#             print(row)

#     def close(self):
#         self.cur.close()
#         self.con.close()
        
#     def wrapper(self):
#         self.create_table()
#         self.insert_data()
        

# class Emails(Resource):
    
#     def get(self):
#         return emails
    
#     def post(self):
#         parser.add_argument("email_subject")
#         parser.add_argument("email_content")
#         parser.add_argument("timestamp")
#         args = parser.parse_args()
#         event_id = str(int(max(emails.keys())) + 1)
#         emails[event_id] = {
#             'email_subject': args['email_subject'],
#             'email_content': args['email_content'],
#             'timestamp': args['timestamp']
#         }
#         new_data = SaveEmail(emails[event_id]['email_subject'],emails[event_id]['email_content'],emails[event_id]['timestamp'])
#         new_data.wrapper()
#         return emails[event_id], 201


app = create_app()
# api = Api(app)
# x = datetime.datetime.now().strftime('%d %b %Y %H:%M')
# emails = {
#     '1' : {'email_subject': 'Jublia interview test api', 'email_content': 'Alalala lets test this', 'timestamp': str(x)}
# } # mocked data
# parser = reqparse.RequestParser()
# api.add_resource(Emails, '/save_emails')


if __name__ == "__main__":
    app.run(debug=True)


# x = datetime.datetime.now().strftime('%d %b %Y %H:%M')        
# temp = SaveEmail('Jublia interview task sekian', 'Alalala yuk test yuk', x)
# temp.create_table()
# temp.insert_data()
# temp.show_data()
# temp.close()
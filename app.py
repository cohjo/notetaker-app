from peewee import *
import datetime

db = PostgresqlDatabase('notetaker', user='postgres', password='',
                        host='localhost', port=5432)
db.connect()

class BaseModel(Model):
    class Meta:
        database = db

class Note(BaseModel):
    title = TextField()
    edited = DateTimeField(default = datetime.datetime.now)
    body = TextField()

db.create_tables([Note])

def create_note():
    new_title = input('Title: ')
    new_body = input('Note: ')
    new_note = Note(title = new_title, body = new_body)
    new_note.save()
    print('\nAdded to NoteTaker\n')

def notes_list():
    print('Your NoteTaker:\n')
    for i in Note.select()
        print(i.title + ' last edited on: ' + i.edited + ':\n\n' + i.body + '\n')

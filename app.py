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
    created = DateTimeField(default = datetime.datetime.now)
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

def edit_note_title():
    select = input('Which note would you like to edit the title for?: ')
    selected = Note.get(Note.title == select)
    selected.title = input('New title: ')
    selected.save()
    print('\nTitle changed successfully\n')

def edit_note_body():
    select = input('Which note would you like to edit the body for?: ')
    selected = Note.get(Note.title == select)
    selected.body = input('New body:\n')
    selected.save()
    print('\nBody changed successfully\n')

def edit_note():
    select = input('Which note would you like to edit?: ')
    selected = Note.get(Note.title == select)
    selected.title = input('New title: ')
    selected.body = input('New body:\n')
    selected.save()
    print('\nNote changed successfuly\n')

def delete_note():
    select = input('Which note would you like to delete?: ')
    selected = Note.get(Note.title == select)
    selected.delete_instance()


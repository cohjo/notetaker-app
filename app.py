from peewee import *
import datetime

import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as source:
    audio = r.listen(source)

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
    print('\n******************')
    print('Added to NoteTaker')
    print('******************\n')

def notes_list():
    print('Your NoteTaker:\n')
    for i in Note.select():
        print(i.title + ' was created ' + i.edited + ':\n\n' + i.body + '\n')

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

def run_notetaker():
    print('\nWhat would you like to do?')
    choice = input('(new, edit title, edit body, edit note, list, delete): ')
    if choice == 'new':
        create_note()
        run_notetaker()
    elif choice == 'edit title':
        edit_note_title()
        run_notetaker()
    elif choice == 'edit body':
        edit_note_body()
        run_notetaker()
    elif choice == 'edit note':
        edit_note()
        run_notetaker()
    elif choice == 'list':
        notes_list()
        run_notetaker()
    elif choice == 'delete':
        delete_note()
        run_notetaker()
    else:
        print('\nSee you next time!')

print('\n\n*********************')
print('Welcome to NoteTaker!')
print('*********************')
run_notetaker()


from peewee import *
import datetime
import pyaudio
import speech_recognition as sr

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

# FUNCTIONS FOR SPEECH RECOGNITION

def listener():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
    try:
        result = r.recognize_google(audio)
        return result
    except Exception:
        result = "Couldn't quite hear that."
        return result

def create_note():
    print('Title: ')
    new_title = listener()
    print(new_title)
    print('Body: ')
    new_body = listener()
    print(new_body)
    new_note = Note(title = new_title, body = new_body)
    new_note.save()
    print('\n******************')
    print('Added to NoteTaker')
    print('******************\n')

def notes_list():
    print('***************')
    print('Your NoteTaker:')
    print('***************\n')
    for i in Note.select():
        print(i.title + ' was created ' + str(i.edited) + ':\n' + i.body + '\n\n')

def edit_note_title():
    notes_list()
    print('Which note would you like to edit the title for?: ')
    select = listener()
    selected = Note.get(Note.title == select)
    print(select)
    print('New title: ')
    selected.title = listener()
    print(selected.title)
    selected.save()
    print('\n**************************')
    print('Title changed successfully')
    print('**************************\n')

def edit_note_body():
    notes_list()
    print('Which note would you like to edit the body for?: ')
    select = listener()
    selected = Note.get(Note.title == select)
    print(select)
    print('New body:\n')
    selected.body = listener()
    print(selected.body)
    selected.save()
    print('\n*************************')
    print('Body changed successfully')
    print('*************************\n')

def edit_note():
    notes_list()
    print('Which note would you like to edit?: ')
    select = listener()
    selected = Note.get(Note.title == select)
    print(select)
    print('New title: ')
    selected.title = listener()
    print(selected.title)
    print('New body: ')
    selected.body = listner()
    print(selected.body)
    selected.save()
    print('\n*************************')
    print('Note changed successfully')
    print('*************************\n')

def delete_note():
    notes_list()
    print('Which note would you like to delete?: ')
    select = listener()
    selected = Note.get(Note.title == select)
    print(select)
    selected.delete_instance()
    print('\n*************************')
    print('Note deleted successfully')
    print('*************************\n')

def run_notetaker():
    print('\nWhat would you like to do?')
    print('SAY (new, edit title, edit body, edit note, list, delete):')
    choice = listener()
    print()

    if choice == 'new':
        print('new')
        create_note()
        run_notetaker()
    elif choice == 'edit title':
        print('edit title')
        edit_note_title()
        run_notetaker()
    elif choice == 'edit body':
        print('edit body')
        edit_note_body()
        run_notetaker()
    elif choice == 'edit note':
        print('edit note')
        edit_note()
        run_notetaker()
    elif choice == 'list':
        print('list')
        notes_list()
        run_notetaker()
    elif choice == 'delete':
        print('delete')
        delete_note()
        run_notetaker()
    elif choice == "Couldn't quite hear that.":
        print("Couldn't quite hear that.")
        run_notetaker()
    else:
        print(choice)
        print('\nSee you next time!')

# FUNCTIONS WITHOUT SPEECH RECOGNITION

def create_note_text():
    new_title = input('Title: ')
    new_body = input('Note: ')
    new_note = Note(title = new_title, body = new_body)
    new_note.save()
    print('\nAdded to NoteTaker\n')
    print('\n******************')
    print('Added to NoteTaker')
    print('******************\n')

def notes_list_text():
    print('***************')
    print('Your NoteTaker:')
    print('***************\n')
    for i in Note.select():
        print(i.title + ' was created ' + i.edited + ':\n\n' + i.body + '\n')

def edit_note_title_text():
    notes_list_text()
    select = input('Which note would you like to edit the title for?: ')
    selected = Note.get(Note.title == select)
    selected.title = input('New title: ')
    selected.save()
    print('\n**************************')
    print('Title changed successfully')
    print('**************************\n')

def edit_note_body_text():
    notes_list_text()
    select = input('Which note would you like to edit the body for?: ')
    selected = Note.get(Note.title == select)
    selected.body = input('New body:\n')
    selected.save()
    print('\n*************************')
    print('Body changed successfully')
    print('*************************\n')

def edit_note_text():
    notes_list_text()
    select = input('Which note would you like to edit?: ')
    selected = Note.get(Note.title == select)
    selected.title = input('New title: ')
    selected.body = input('New body:\n')
    selected.save()
    print('\n*************************')
    print('Note changed successfully')
    print('*************************\n')

def delete_note_text():
    notes_list_text()
    select = input('Which note would you like to delete?: ')
    selected = Note.get(Note.title == select)
    selected.delete_instance()
    print('\n*************************')
    print('Note deleted successfully')
    print('*************************\n')

def run_notetaker_text():
    print('\nWhat would you like to do?')
    choice = input('(new, edit title, edit body, edit note, list, delete): ')
    if choice == 'new':
        create_note_text()
        run_notetaker_text()
    elif choice == 'edit title':
        edit_note_title_text()
        run_notetaker_text()
    elif choice == 'edit body':
        edit_note_body_text()
        run_notetaker_text()
    elif choice == 'edit note':
        edit_note_text()
        run_notetaker_text()
    elif choice == 'list':
        notes_list_text()
        run_notetaker_text()
    elif choice == 'delete':
        delete_note_text()
        run_notetaker_text()
    else:
        print('\nSee you next time!')

print('\n\n*********************')
print('Welcome to NoteTaker!')
print('*********************\n')
dec = input('Would you like to use voice or text input? (v / t): ')
if dec == 't': run_notetaker_text()
elif dec == 'v': run_notetaker()
else: 'Goodbye!'


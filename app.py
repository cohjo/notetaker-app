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

note1 = Note(title = 'First Note', body = 'Hello world')
note1.save()


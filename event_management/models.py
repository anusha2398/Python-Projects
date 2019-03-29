import peewee

db = peewee.SqliteDatabase("events.db") #to create database

class EventsList(peewee.Model):
	event_name = peewee.TextField()

	class Meta:
		database = db


class ParticipantsList(peewee.Model):
	participant_name = peewee.TextField() #textfield indicates the type of data
	event_name = peewee.ForeignKeyField(EventsList)

	class Meta:
		database = db

db.connect()
db.create_tables([EventsList, ParticipantsList])
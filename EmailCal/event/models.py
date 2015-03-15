from django.db import models

class Users(models.Model):
	userID = models.IntegerField(default=0)
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	email = models.CharField(max_length=100)
	
class Event(models.Model):
	user = models.ForeignKey(Users)
	event_ID = models.IntegerField(default=0)
	event_name = models.CharField(max_length=50)
	event_location = models.CharField(max_length=50)
	event_date = DateTimeField('event date')
	event_notes = models.CharField(max_length=200)
	
class Event_Invites(models.Model):
	user = models.ForeignKey(Users)
	event = models.ForeignKey(Event)
	event_ID = models.IntegerField(default=0)
	inviter_ID = models.IntegerField(default=0)
	invitee_ID = models.IntegerField(default=0)
from django.db import models
from aquaticore.databases.models import Database

class Specialist(models.Model):
	title = models.CharField(max_length=200)
	database = models.ForeignKey(Database)
	created = models.DateTimeField('date published')
	modified = models.DateTimeField(auto_now=True, default='0000-00-00 00:00:00')

	def __unicode__(self):
		return self.title
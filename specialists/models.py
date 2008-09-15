from django.db import models

class Specialist(models.Model):
	name = models.CharField(max_length=200)
	database = models.ForeignKey('databases.Database')
	created = models.DateTimeField('date published')
	modified = models.DateTimeField(auto_now=True, default='0000-00-00 00:00:00')

	def __unicode__(self):
		return self.title
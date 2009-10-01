from django.db import models

class Country(models.Model):
	title    = models.CharField(max_length=200)
	code     = models.CharField(max_length=10)
	created  = models.DateTimeField('date published')
	modified = models.DateTimeField(auto_now=True, default='0000-00-00 00:00:00')

	def __unicode__(self):
		return self.title
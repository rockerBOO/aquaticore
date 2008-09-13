from django.db import models

# Create your models here.
class Database(models.Model):
	title = models.CharField(max_length=200)
	website = models.CharField(max_length=200)
	organization = models.CharField(max_length=200)
	display_name = models.CharField(max_length=200)
	created = models.DateTimeField('date published')
	modified = models.DateTimeField(auto_now=True, default='0000-00-00 00:00:00')

	def __unicode__(self):
		return self.title
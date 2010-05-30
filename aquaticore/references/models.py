from django.db import models
from aquaticore.databases.models import Database
from aquaticore.authors.models import Author

class Reference(models.Model):
	title = models.CharField(max_length=200)
	source = models.CharField(max_length=200)
	year = models.IntegerField(4)
	author = models.ForeignKey('authors.Author')
	database = models.ForeignKey('databases.Database')
	created = models.DateTimeField('date published')
	modified = models.DateTimeField(auto_now=True, default='0000-00-00 00:00:00')

	def __unicode__(self):
		return self.title
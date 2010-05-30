from django.db import models
from aquaticore.databases.models import Database
from aquaticore.languages.models import Language
from aquaticore.geography.models import Country
from aquaticore.references.models import Reference

class CommonName(models.Model):
	title     = models.CharField(max_length=200)
	code      = models.CharField(max_length=200)
	language  = models.ForeignKey(Language)
	country   = models.ForeignKey(Country)
	reference = models.ForeignKey(Reference)
	database  = models.ForeignKey(Database)
	created   = models.DateTimeField('date published')
	modified  = models.DateTimeField(auto_now=True, default='0000-00-00 00:00:00')

	def __unicode__(self):
		return self.title
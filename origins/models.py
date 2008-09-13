from django.db import models
from aquaticore.geography.models import Country

class Origin(models.Model):	
	title = models.CharField(max_length=200)
	country = models.ForeignKey(Country)
	created = models.DateTimeField('date published')
	modified = models.DateTimeField(auto_now=True, default='0000-00-00 00:00:00')

	def __unicode__(self):
		return self.title
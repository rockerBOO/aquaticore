from django.db import models
from aquaticore.taxa.models import Species
from django.contrib.auth.models import User
from django.contrib import admin

# Create your models here.
class Aquarium(models.Model):
	title = models.CharField(max_length=200)
	user = models.ManyToManyField(User, null=False, blank=False)
	body = models.TextField()
	species = models.ManyToManyField(Species, null=True, blank=True)
	created = models.DateTimeField('date published')
	modified = models.DateTimeField(auto_now=True, default='0000-00-00 00:00:00')

	def __unicode__(self):
		return self.title
		
admin.site.register(Aquarium)
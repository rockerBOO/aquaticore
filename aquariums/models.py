from django.db import models
from aquaticore.fish.models import Fish
from django.contrib import admin

# Create your models here.
class Aquarium(models.Model):
	title = models.CharField(max_length=200)
	body = models.TextField()
	fish = models.ManyToManyField(Fish, null=True, blank=True)
	created = models.DateTimeField('date published')
	modified = models.DateTimeField(auto_now=True, default='0000-00-00 00:00:00')

	def __unicode__(self):
		return self.title
		
admin.site.register(Aquarium)
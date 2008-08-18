from django.db import models

class Fish:
	title = models.CharField(max_length=200)
	body = models.TextField()
	scientific_name = models.CharField(max_length=255)
	family = models.OneToOneField(FishFamily)
	origin = models.OneToOneField(FishOrigin)
	size = models.CharField(max_length=200)
	ph = models.DecimalField()
	temp = models.IntegerField(3)
	created = models.DateTimeField('date published')

	def __unicode__(self):
		return self.title
		
class FishCommmonName:
	title = models.CharField(max_length=200)
	fish = models.ForeignKey(Fish)
	created = models.DateTimeField('date published')
	
class Diet:
	title = models.CharField(max_length=200)
	created = models.DateTimeField('date published')
	
class FishFamily:
	title = models.CharField(max_length=200)
	created = models.DateTimeField('date published')
	
class FishOrigin:
	title = models.CharField(max_length=200)
	created = models.DateTimeField('date published')
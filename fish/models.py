from django.db import models
from django.forms import ModelForm
from django.contrib import admin

class FishOrder(models.Model):
	title = models.CharField(max_length=200)
	created = models.DateTimeField('date published')
	modified = models.DateTimeField(auto_now=True, default='0000-00-00 00:00:00')

class FishFamily(models.Model):
	title = models.CharField(max_length=200)
	order = models.ForeignKey(FishOrder)
	created = models.DateTimeField('date published')
	modified = models.DateTimeField(auto_now=True, default='0000-00-00 00:00:00')
	
	def __unicode__(self):
		return self.title

class CommonName(models.Model):
	title = models.CharField(max_length=200)
	created = models.DateTimeField()
	modified = models.DateTimeField(auto_now=True, default='0000-00-00 00:00:00')

	def __unicode__(self):
		return self.title

class Diet(models.Model):
	title = models.CharField(max_length=200)
	created = models.DateTimeField('date published')
	modified = models.DateTimeField(auto_now=True, default='0000-00-00 00:00:00')

	def __unicode__(self):
		return self.title

class FishOrigin(models.Model):
	title = models.CharField(max_length=200)
	created = models.DateTimeField('date published')
	modified = models.DateTimeField(auto_now=True, default='0000-00-00 00:00:00')

class Fish(models.Model):
	body = models.TextField()
	scientific_name = models.CharField(max_length=255)
	family = models.ForeignKey(FishFamily)
	origin = models.ManyToManyField(FishOrigin)
	diet = models.ManyToManyField(Diet)
	commonname = models.ManyToManyField(CommonName)
	min_size = models.IntegerField(4)
	max_size = models.IntegerField(4)
	min_ph = models.FloatField()
	max_ph = models.FloatField()
	min_temp = models.IntegerField(3)
	max_temp = models.IntegerField(3)
	created = models.DateTimeField('date published')
	modified = models.DateTimeField(auto_now=True, default='0000-00-00 00:00:00')

	def __unicode__(self):
		return self.title
		
class FishForm(ModelForm):	
	class Meta:
		model = Fish
	
class Country(models.Model):
	title = models.CharField(max_length=200)
	code = models.CharField(max_length=3)
	modified = models.DateTimeField(auto_now=True, default='0000-00-00 00:00:00')
	
	def __unicode__(self):
		return self.title
	
admin.site.register(Fish)
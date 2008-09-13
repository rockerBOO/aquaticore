from django.db import models

class Kingdom(models.Model):
	title = models.CharField(max_length=200)
	created = models.DateTimeField('date published')
	modified = models.DateTimeField(auto_now=True, default='0000-00-00 00:00:00')

	def __unicode__(self):
		return self.title

class Phylum(models.Model):
	title = models.CharField(max_length=200)
	kingdom = models.ForeignKey(Kingdom)
	created = models.DateTimeField('date published')
	modified = models.DateTimeField(auto_now=True, default='0000-00-00 00:00:00')

	def __unicode__(self):
		return self.title

class Class(models.Model):
	title = models.CharField(max_length=200)
	phylum = models.ForeignKey(Phylum)
	created = models.DateTimeField('date published')
	modified = models.DateTimeField(auto_now=True, default='0000-00-00 00:00:00')

	def __unicode__(self):
		return self.title

class Order(models.Model):
	title = models.CharField(max_length=200)
	fish_class = models.ForeignKey(Class)
	created = models.DateTimeField('date published')
	modified = models.DateTimeField(auto_now=True, default='0000-00-00 00:00:00')

	def __unicode__(self):
		return self.title

class Family(models.Model):
	title = models.CharField(max_length=200)
	order = models.ForeignKey(Order)
	created = models.DateTimeField('date published')
	modified = models.DateTimeField(auto_now=True, default='0000-00-00 00:00:00')
	
	def __unicode__(self):
		return self.title

class Genus(models.Model):
	title = models.CharField(max_length=200)
	family = models.ForeignKey(Family)
	created = models.DateTimeField('date published')
	modified = models.DateTimeField(auto_now=True, default='0000-00-00 00:00:00')

	def __unicode__(self):
		return self.title

class Species(models.Model):
	title = models.CharField(max_length=200)
	genus = models.ForeignKey(Genus)
	created = models.DateTimeField('date published')
	modified = models.DateTimeField(auto_now=True, default='0000-00-00 00:00:00')

	def __unicode__(self):
		return self.title
		
class Infraspecies(models.Model):
	title = models.CharField(max_length=200)
	species = models.ForeignKey(Species)
	created = models.DateTimeField('date published')
	modified = models.DateTimeField(auto_now=True, default='0000-00-00 00:00:00')

	def __unicode__(self):
		return self.title
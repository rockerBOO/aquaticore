from django.db import models
from flickrapi import FlickrAPI
from django.core.cache import cache
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class Kingdom(models.Model):
	name             = models.CharField(max_length=200, unique=True)
	is_accepted_name = models.NullBooleanField()
	created          = models.DateTimeField('date published')
	modified         = models.DateTimeField(auto_now=True, default='0000-00-00 00:00:00')

	def __unicode__(self):
		return self.title

class Phylum(models.Model):
	name             = models.CharField(max_length=200, unique=True)
	is_accepted_name = models.NullBooleanField()
	kingdom          = models.ForeignKey(Kingdom)
	created          = models.DateTimeField('date published')
	modified         = models.DateTimeField(auto_now=True, default='0000-00-00 00:00:00')

	def __unicode__(self):
		return self.title

class Class(models.Model):
	name             = models.CharField(max_length=200, unique=True)
	is_accepted_name = models.NullBooleanField()
	phylum           = models.ForeignKey(Phylum)
	created          = models.DateTimeField('date published')
	modified         = models.DateTimeField(auto_now=True, default='0000-00-00 00:00:00')

	def __unicode__(self):
		return self.title

class Order(models.Model):
	name             = models.CharField(max_length=200, unique=True)
	is_accepted_name = models.NullBooleanField()
	fish_class       = models.ForeignKey(Class)
	created          = models.DateTimeField('date published')
	modified         = models.DateTimeField(auto_now=True, default='0000-00-00 00:00:00')

	def __unicode__(self):
		return self.title

class Family(models.Model):
	name             = models.CharField(max_length=200, unique=True)
	is_accepted_name = models.NullBooleanField()
	order            = models.ForeignKey(Order)
	created          = models.DateTimeField('date published')
	modified         = models.DateTimeField(auto_now=True, default='0000-00-00 00:00:00')
	
	def __unicode__(self):
		return self.title

class Genus(models.Model):
	name             = models.CharField(max_length=200, unique=True)
	is_accepted_name = models.NullBooleanField()
	family           = models.ForeignKey(Family)
	created          = models.DateTimeField('date published')
	modified         = models.DateTimeField(auto_now=True, default='0000-00-00 00:00:00')

	def __unicode__(self):
		return self.title

class Species(models.Model):
	name               = models.CharField(max_length=200, unique=True)
	is_accepted_name   = models.NullBooleanField()
	author             = models.ForeignKey('authors.Author')
	genus              = models.ForeignKey(Genus)
	database           = models.ForeignKey('databases.Database')
	specialist         = models.ForeignKey('specialists.Specialist')
	reference          = models.ManyToManyField('references.Reference')
	accepted_name_code = models.CharField(max_length=30)
	name_code          = models.CharField(max_length=30)
	body               = models.TextField()
	url                = models.CharField(max_length=200)
	scrutiny_date      = models.DateField()
	created            = models.DateTimeField('date published')
	modified           = models.DateTimeField(auto_now=True, default='0000-00-00 00:00:00')
	
	def get_flickr_photos(self, limit=10, first_large=False, page_num=1):

		# Flickr Photos
		flickr = FlickrAPI('12ac22376b8bdd0127b4d78eb5b8eae9', cache=True, format='etree')
		flickr.cache = cache

		keyword = "\"" + self.name + "\""
		photos  = flickr.photos_search(text=keyword, sort="interestingness-desc", per_page=limit, page=page_num)
		
		if photos.attrib['stat'] == 'fail':
			return []
							
		flickr_photos = photos.find('photos').findall('photo')
		
		fps = []
		
		for photo in flickr_photos:			
			fps.append({\
				'src' : 'http://farm' + photo.attrib['farm'] + '.static.flickr.com/' + photo.attrib['server'] + '/' + photo.attrib['id'] + '_' + photo.attrib['secret'] + '_s.jpg',\
				'src_l' : 'http://farm' + photo.attrib['farm'] + '.static.flickr.com/' + photo.attrib['server'] + '/' + photo.attrib['id'] + '_' + photo.attrib['secret'] + '_m.jpg',
				'src_500' : 'http://farm' + photo.attrib['farm'] + '.static.flickr.com/' + photo.attrib['server'] + '/' + photo.attrib['id'] + '_' + photo.attrib['secret'] + '.jpg',\
				'url' : 'http://flickr.com/photos/' + photo.attrib['owner'] + '/' + photo.attrib['id'] + '/',\
				'title' : photo.attrib['title']})
			
		return fps

	def __unicode__(self):
		return self.title
		
class Infraspecies(models.Model):
	name             = models.CharField(max_length=200, unique=True)
	is_accepted_name = models.NullBooleanField()
	species          = models.ForeignKey(Species)
	created          = models.DateTimeField('date published')
	modified         = models.DateTimeField(auto_now=True, default='0000-00-00 00:00:00')

	def __unicode__(self):
		return self.title
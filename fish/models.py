from django.db import models
from django.forms import ModelForm
from django.contrib import admin
from flickrapi import *
from django.core.cache import cache
from aquaticore.articles.models import Article

class FishClass(models.Model):
	title = models.CharField(max_length=200)
	created = models.DateTimeField('date published')
	modified = models.DateTimeField(auto_now=True, default='0000-00-00 00:00:00')

	def __unicode__(self):
		return self.title

class FishOrder(models.Model):
	title = models.CharField(max_length=200)
	fish_class = models.ForeignKey(FishClass)
	created = models.DateTimeField('date published')
	modified = models.DateTimeField(auto_now=True, default='0000-00-00 00:00:00')

	def __unicode__(self):
		return self.title

class FishFamily(models.Model):
	title = models.CharField(max_length=200)
	order = models.ForeignKey(FishOrder)
	created = models.DateTimeField('date published')
	modified = models.DateTimeField(auto_now=True, default='0000-00-00 00:00:00')
	
	def __unicode__(self):
		return self.title

class FishGenus(models.Model):
	title = models.CharField(max_length=200)
	family = models.ForeignKey(FishFamily)
	created = models.DateTimeField('date published')
	modified = models.DateTimeField(auto_now=True, default='0000-00-00 00:00:00')

	def __unicode__(self):
		return self.title

class FishSpecies(models.Model):
	title = models.CharField(max_length=200)
	genus = models.ForeignKey(FishGenus)
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
	
	def __unicode__(self):
		return self.title

class Fish(models.Model):
	body = models.TextField()
	species = models.ForeignKey(FishSpecies)
	origin = models.ManyToManyField(FishOrigin, null=True, blank=True)
	diet = models.ManyToManyField(Diet, null=True, blank=True)
	cn = models.ManyToManyField(CommonName, null=True, blank=True)
	article = models.ManyToManyField(Article, null=True, blank=True)
	min_size = models.FloatField()
	max_size = models.FloatField()
	min_ph = models.FloatField()
	max_ph = models.FloatField()
	min_temp = models.FloatField()
	max_temp = models.FloatField()
	created = models.DateTimeField('date published')
	modified = models.DateTimeField(auto_now=True, default='0000-00-00 00:00:00')

	def __unicode__(self):
		return self.species.genus.title + " " + self.species.title
		
	def get_flickr_photos(self, limit=10, first_large=False):
		common_names = CommonName.objects.filter(fish=self).distinct()

		# Flickr Photos
		flickr = FlickrAPI('12ac22376b8bdd0127b4d78eb5b8eae9', cache=True, format='etree')
		flickr.cache = cache

		common_name_titles = []

		# add some of the common names
		for cn in common_names:
			common_name_titles.append(cn.title)

		keyword = '"' + self.species.genus.title + " " + self.species.title + '" OR "' + '" OR "'.join(common_name_titles) + '"'

		# return render_to_response('fish/detail.html', {'cn' : keyword})

		photos = flickr.photos_search(text=keyword, privacy_filter=1, sort="interestingness-desc", per_page=limit)
		flickr_photos = []
		
		if photos.attrib['stat'] == 'fail':
			return False
		
		if photos.find('photos').attrib['total'] != '0':
			photos = photos.find('photos').findall('photo')

			i = 0

			# Add sizes for each image
			for photo in photos:
				if photo == False:
					continue
				
				try:
					photo_sizes = flickr.photos_getSizes(photo_id=photo.attrib['id'])
				except FlickrError:
					continue
					
				if i == 0 and first_large:
					flickr_photos.append({'source' : photo_sizes.find('sizes').findall('size')[3].attrib['source'], \
						'url' : photo_sizes.find('sizes').findall('size')[3].attrib['url'], 'title' : photo.attrib['title']})				
				else:
					flickr_photos.append({'source' : photo_sizes.find('sizes').findall('size')[1].attrib['source'], \
						'url' : photo_sizes.find('sizes').findall('size')[3].attrib['url'], 'title' : photo.attrib['title']})
				i = i + 1
				
		return flickr_photos
		
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
admin.site.register(FishSpecies)
admin.site.register(FishGenus)
admin.site.register(FishFamily)
admin.site.register(FishOrder)
admin.site.register(FishClass)
admin.site.register(CommonName)
admin.site.register(FishOrigin)
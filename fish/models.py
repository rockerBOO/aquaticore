from django.db import models
from django.forms import ModelForm
from django.contrib import admin
from flickrapi import *
from django.core.cache import cache
from aquaticore.articles.models import Article
from aquaticore.taxa.models import Species
from aquaticore.diets.models import Diet
from aquaticore.origins.models import Origin
from aquaticore.common_names.models import CommonName
from elementtree.ElementTree import ElementTree
import urllib
from django.core.cache import cache

class Fish(models.Model):
	body = models.TextField(null=True, blank=True)
	species = models.ForeignKey('taxa.Species')
	origin = models.ManyToManyField('origins.Origin', null=True, blank=True)
	diet = models.ManyToManyField('diets.Diet', null=True, blank=True)
	cn = models.ManyToManyField('common_names.CommonName', null=True, blank=True)
	article = models.ManyToManyField('articles.Article', null=True, blank=True)
	min_size = models.FloatField(null=True, blank=True)
	max_size = models.FloatField(null=True, blank=True)
	min_ph = models.FloatField(null=True, blank=True)
	max_ph = models.FloatField(null=True, blank=True)
	min_temp = models.FloatField(null=True, blank=True)
	max_temp = models.FloatField(null=True, blank=True)
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
		photos  = flickr.photos_search(text=keyword, privacy_filter=1, sort="interestingness-desc", per_page=limit)
		
		if photos.attrib['stat'] == 'fail':
			return False
							
		flickr_photos = photos.find('photos').findall('photo')
		
		fps = []
		
		for photo in flickr_photos:
			username = flickr.people_getInfo(user_id=photo.attrib['owner'])
			username = username.find('username')
			
			fps.append({\
				'src' : 'http://farm' + photo.attrib['farm'] + '.static.flickr.com/' + photo.attrib['server'] + '/' + photo.attrib['id'] + '_' + photo.attrib['secret'] + '_t.jpg',\
				'src_l' : 'http://farm' + photo.attrib['farm'] + '.static.flickr.com/' + photo.attrib['server'] + '/' + photo.attrib['id'] + '_' + photo.attrib['secret'] + '_m.jpg',\
				'url' : 'http://flickr.com/photos/' + str(username) + '/' + photo.attrib['id'] + '/',\
				'title' : photo.attrib['title']})
			
		return fps
		
	def get_fishbase_info(self):
		
		key = 'get_fishbase_info_' + str(self.id) + '_feed'
		
		# fishbaseXml = "http://fishbase.sinica.edu.tw/webservice/Species/SpeciesSummary.asp?Genus=" + self.species.genus.title + "&Species=" + self.species.title + ""
		# feed = urllib.urlopen(fishbaseXml)
		# 	
		# # return feed
		# et = ElementTree()
		# tree = et.parse(feed)
		# value = dict((c, p) for p in tree.getiterator() for c in p)
		# 
		
		# feed = cache.get(key)
		feed = False
		
		if feed == False or feed == '' or feed == None:
			fishbaseXml = "http://fishbase.sinica.edu.tw/webservice/Species/SpeciesSummary.asp?Genus=" + self.species.genus.title + "&Species=" + self.species.title + ""
			
			try:
				feed = urllib.urlopen(fishbaseXml)
			except IOError:
				return {'error' : 'Sorry, seems fishbase is down at the moment'}
			
			# cache.set(key, feed, 3600)			
		
		for line in feed.read():
			if line.find('<html>'):
				return {'error' : 'Sorry, seems fishbase is down at the moment. There has been an error in the xml feed. '}
			
		# return feed
		et = ElementTree()
		
		# try:
		tree = et.parse(feed)
		# except ExpatError:
		# 	return {'error' : 'Sorry, seems fishbase is down at the moment'}
		
		value = dict((c, p) for p in tree.getiterator() for c in p)
		
		return value
	
	def __getstate__(self):
		return

class FishForm(ModelForm):	
	class Meta:
		model = Fish
	
admin.site.register(Fish)
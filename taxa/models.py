from django.db import models
from flickrapi import FlickrAPI
import gdata.youtube
import gdata.youtube.service
from django.core.cache import cache
import simplejson as json
from BeautifulSoup import BeautifulStoneSoup
from elementtree.ElementTree import ElementTree
import urllib
import sys
import re
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
		
		photos  = flickr.photos_search(text=keyword, sort="interestingness-desc", per_page=limit, page=page_num, license='1,2,3,4,5,6', extras='owner_name,license')
		
		if photos.attrib['stat'] == 'fail':
			return []
		
			# <licenses>
			# 	<license id="4" name="Attribution License"
			# 		url="http://creativecommons.org/licenses/by/2.0/" /> 
			# 	<license id="6" name="Attribution-NoDerivs License"
			# 		url="http://creativecommons.org/licenses/by-nd/2.0/" /> 
			# 	<license id="3" name="Attribution-NonCommercial-NoDerivs License"
			# 		url="http://creativecommons.org/licenses/by-nc-nd/2.0/" /> 
			# 	<license id="2" name="Attribution-NonCommercial License"
			# 		url="http://creativecommons.org/licenses/by-nc/2.0/" /> 
			# 	<license id="1" name="Attribution-NonCommercial-ShareAlike License"
			# 		url="http://creativecommons.org/licenses/by-nc-sa/2.0/" /> 
			# 	<license id="5" name="Attribution-ShareAlike License"
			# 		url="http://creativecommons.org/licenses/by-sa/2.0/" /> 
			# 	<license id="7" name="No known copyright restrictions"
			# 		url="http://flickr.com/commons/usage/" />
			# </licenses>
		
		flickr_photos = photos.find('photos').findall('photo')
		
		fps = []
		
		for photo in flickr_photos:
			fps.append({\
				'src' : 'http://farm' + photo.attrib['farm'] + '.static.flickr.com/' + photo.attrib['server'] + '/' + photo.attrib['id'] + '_' + photo.attrib['secret'] + '_s.jpg',\
				'src_l' : 'http://farm' + photo.attrib['farm'] + '.static.flickr.com/' + photo.attrib['server'] + '/' + photo.attrib['id'] + '_' + photo.attrib['secret'] + '_m.jpg',
				'src_500' : 'http://farm' + photo.attrib['farm'] + '.static.flickr.com/' + photo.attrib['server'] + '/' + photo.attrib['id'] + '_' + photo.attrib['secret'] + '.jpg',\
				'url' : 'http://flickr.com/photos/' + photo.attrib['ownername'] + '/' + photo.attrib['id'] + '/',\
				'ownername': photo.attrib['ownername'],\
				'license': photo.attrib['license'],\
				'title' : photo.attrib['title']})
		
		return fps
	
	def get_youtube_videos(self, limit=10):
		# yt_service = gdata.youtube.service.YouTubeService()
		# 		
		# yt_service.developer_key = 'AI39si6EFjf7JOPQa6_Ml32u74-IramXpeYvJ9Yr2z4ULX6nlQIb-UTB6fC6VH8g1SGDGiv6ogzxr4aZYCdtvvHBAOddPn4_-Q'
		# 		
		# query = gdata.youtube.service.YouTubeVideoQuery()
		# query.vq = self.name
		# query.orderby = 'viewCount'
		# query.racy = 'exclude'
		# query.alt  = 'json'
		# feed = yt_service.YouTubeQuery(query)
		# 		
		# 		
		# # 
		
		url = 'http://gdata.youtube.com/feeds/videos?start-index=1&max-results=' + str(limit) + '&vq=' + self.name + '&racy=exclude&orderby=viewCount&alt=json'
		
		# return url
		
		feed = urllib.urlopen(url)		
		
		try:
			data = json.load(feed)
		except ValueError:
			return {}
		
		return data
	
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
		
		if feed is False or feed is '' or feed is None:
			# http://fishbase.sinica.edu.tw/maintenance/FB/showXML.php?identifier=FB-10489&ProviderDbase=03
			fishbaseXml = "http://fishbase.sinica.edu.tw/maintenance/FB/showXML.php?identifier=FB-" + self.get_fishbase_species_id() + "&ProviderDbase=03"
			feed = urllib.urlopen(fishbaseXml) 
		
		et = ElementTree()
		
		tree = et.parse(feed)
		
		dataObjects = tree.findall('taxon/dataObject')
		
		# return dataObjects
		
		value = dict((c, p) for p in dataObjects.getiterator() for c in p)
		
		return value
	def get_fishbase_species_id(self):
		names = self.name.split(' ')
	    
		fishbaseCommon = "http://www.fishbase.us/webservice/ComNames/comnamesxml.php?Genus=" + names[0] + "&Species=" + names[1] + ""
	    
		try:
			common_names = urllib.urlopen(fishbaseCommon)
			
			lines = ''
			
			for line in common_names.read():
				lines += line
			
			# return lines
			matches = re.search(r'<speccode>([0-9]+)<\/speccode>', lines)
			if matches is None:
				return ''
			else:
				return matches.group(1)
		except IOError:
			return {'error': 'sorry'}
	def __unicode__(self):
		return self.name

class Infraspecies(models.Model):
	name             = models.CharField(max_length=200, unique=True)
	is_accepted_name = models.NullBooleanField()
	species          = models.ForeignKey(Species)
	created          = models.DateTimeField('date published')
	modified         = models.DateTimeField(auto_now=True, default='0000-00-00 00:00:00')
	
	def __unicode__(self):
		return self.title

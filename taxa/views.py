from django.template import Context, loader, RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from aquaticore.taxa.models import Family, Species, Genus
from django.http import HttpResponseRedirect
from django import forms
from django.core.paginator import Paginator
import datetime
import re

def index(request):
	return render_to_response('taxa/index.html', {}, context_instance=RequestContext(request))

def species_detail(request, species_name):	

	species_name = re.sub('[\+\_]', ' ', species_name)

	species = Species.objects.get(name=species_name)
	flickr_photos = species.get_flickr_photos(limit=4)
	return render_to_response('taxa/species_detail.html', {'species' : species, 'flickr_photos' : flickr_photos}, context_instance=RequestContext(request))

def family_detail(request, family_name):

	family_name = re.sub('[\+\_]', ' ', family_name)

	family = Family.objects.get(name=family_name)
	genuses = Genus.objects.filter(family=family)
	
	species_list = []
	
	for genus in genuses:
	
		
		species = Species.objects.filter(genus=genus)
	
		for s in species:
			photo = s.get_flickr_photos(1)
			if len(photo) > 0:
				photo = photo[0]
			species_list.append({'species' : s, 'photo' : photo})
	
	paginator = Paginator(species_list, 20)
	
	return render_to_response('taxa/family_detail.html', {'family' : family, 'species_list' : paginator.object_list}, context_instance=RequestContext(request))
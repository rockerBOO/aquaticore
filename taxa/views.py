from django.template import Context, loader, RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from aquaticore.taxa.models import Species, Genus
from django.http import HttpResponseRedirect
from django import forms
import datetime

def index(request):
	return render_to_response('taxa/index.html', {'species_list' : species_list}, context_instance=RequestContext(request))
	
def detail(request, species_name):	
	species = Species.objects.get(name=species_name)
	flickr_photos = species.get_flickr_photos(limit=5, first_large=True)
	return render_to_response('taxa/detail.html', {'species' : species, 'flickr_photos' : flickr_photos}, context_instance=RequestContext(request))
from django.template import Context, loader, RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from aquaticore.taxa.models import Family, Species, Genus
from django.http import HttpResponseRedirect
from django import forms
from django.core.paginator import Paginator
import datetime
import re

def index(request, tt_type=False, name=False):
    if tt_type is False or name is False:
        return render_to_response('tooltip/index.json', {}, context_instance=RequestContext(request))
    
    if tt_type == 'ts':
        name = name.replace('+', ' ')
        species = Species.objects.get(name=name)
        photos = species.get_flickr_photos(limit=1)
    
	return render_to_response('tooltip/index.json', {'species': species, 'photos': photos}, context_instance=RequestContext(request))
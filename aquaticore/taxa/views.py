from django.template import Context, loader, RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from aquaticore.taxa.models import Family, Species, Genus, Order, Phylum
from django.http import HttpResponseRedirect
from django import forms
from django.core.paginator import Paginator
import datetime
import re

def index(request):
	new_species  = Species.objects.all().order_by('-id')[:30]
	new_families = Family.objects.all().order_by('-id')[:10]
	new_orders   = Order.objects.all().order_by('-id')[:5]
	new_phylums  = Phylum.objects.all().order_by('-id')[:5]
	
	count_species = Species.objects.count()
	count_family  = Family.objects.count()
	count_order   = Order.objects.count()
	count_phylum  = Phylum.objects.count()
		
	return render_to_response('taxa/index.html', {'new_species': new_species, 'count_species': count_species, 'count_family': count_family, 'count_order': count_order, 'count_phylum': count_phylum, 'new_families': new_families, 'new_orders': new_orders, 'new_phylums': new_phylums}, context_instance=RequestContext(request))

def species_detail(request, species_name):	

    # if ("form_action" in request.POST and "species_name" in request.POST and request.POST["form_action"] == 'add'):
        # x = Species(name=request.POST["species_name"])
        

	species_name = re.sub('[\+\_]', ' ', species_name)

	species = Species.objects.get(name=species_name)
	flickr_photos = species.get_flickr_photos(limit=4)
	youtube_videos = species.get_youtube_videos(limit=4)
	# fishbase_info = species.get_fishbase_info()
	return render_to_response('taxa/species_detail.html', {'species' : species, 'flickr_photos' : flickr_photos, 'youtube_videos': youtube_videos}, context_instance=RequestContext(request))

def species_list(request):
	species_list = Species.objects.all()
	count_species = Species.objects.count()
	
	paginator = Paginator(species_list, 30)
	
	# Make sure page request is an int. If not, deliver first page.
	try:
		page = int(request.GET.get('page', '1'))
	except ValueError:
		page = 1

    # If page request (9999) is out of range, deliver last page of results.
	try:
		species_list = paginator.page(page)
	except (EmptyPage, InvalidPage):
		species_list = paginator.page(paginator.num_pages)

	return render_to_response('taxa/list/species.html', {'species_list' : species_list, 'count_species': count_species}, context_instance=RequestContext(request))

def order_detail(request, order_name):
	order = Order.objects.get(name=order_name)
	
	families = Family.objects.filter(order=order)
	
	paginator = Paginator(families, 20)
	
	# Make sure page request is an int. If not, deliver first page.
	try:
		page = int(request.GET.get('page', '1'))
	except ValueError:
		page = 1

    # If page request (9999) is out of range, deliver last page of results.
	try:
		families = paginator.page(page)
	except (EmptyPage, InvalidPage):
		families = paginator.page(paginator.num_pages)
	
	return render_to_response('taxa/order_detail.html', {'order' : order, 'families' : families}, context_instance=RequestContext(request))

def family_detail(request, family_name):
	family = Family.objects.get(name=family_name)
	genuses = Genus.objects.filter(family=family)
	
	species_list = []
	
	for genus in genuses:
		species_list += Species.objects.filter(genus=genus)

	paginator = Paginator(species_list, 20)
	
	# Make sure page request is an int. If not, deliver first page.
	try:
		page = int(request.GET.get('page', '1'))
	except ValueError:
		page = 1

    # If page request (9999) is out of range, deliver last page of results.
	try:
		species_list = paginator.page(page)
	except (EmptyPage, InvalidPage):
		species_list = paginator.page(paginator.num_pages)
	
	return render_to_response('taxa/family_detail.html', {'family' : family, 'species_list' : species_list}, context_instance=RequestContext(request))
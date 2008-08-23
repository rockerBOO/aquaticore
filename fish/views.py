from django.template import Context, loader
from django.http import HttpResponse
from aquaticore.fish.models import Fish, FishFamily, CommonName
from django.shortcuts import render_to_response, get_object_or_404
from datetime import datetime
from math import *
from flickrapi import FlickrAPI
from django.core.cache import cache

def index(request):
	fish_list = Fish.objects.all().order_by('-created')[:10]
	return render_to_response('fish/index.html', {'fish_list' : fish_list})

def top10(request):	
	top10_fish_list = Fish.objects.all().order_by('-created')[:10]
	return render_to_response('fish/top10.html', {'top10_fish_list' : top10_fish_list})
	
def detail(request, fish_id):
	fish = get_object_or_404(Fish, pk=fish_id)
	
	# common_names = CommonName.objects.filter(fish=fish)
	common_names = CommonName.objects.all()

	# Flickr Photos
	flickr = FlickrAPI('12ac22376b8bdd0127b4d78eb5b8eae9', cache=True)
	flickr.cache = cache
	
	photos = flickr.photos_search(text=fish.scientific_name, license=1, per_page='10')
	photos = photos.photos[0]
	
	flickr_photos = []
	
	# Add sizes for each image
	for photo in photos.photo:
		photo_sizes = flickr.photos_getSizes(photo_id=photo['id'])
		flickr_photos.append({'source' : photo_sizes.sizes[0].size[2]['source'], 'url' : photo_sizes.sizes[0].size[2]['url']})
	
	return render_to_response('fish/detail.html', {'fish': fish, 
		'common_names' : common_names,
		'flickr_photos' : flickr_photos,
		'max_size_in' : fish.max_size * 0.39, 
		'min_size_in' : fish.min_size * 0.39, 
		'max_temp_f' : ((fish.max_temp * 9) / 5) + 32, 
		'min_temp_f' : ((fish.min_temp * 9) / 5) + 32})
	

def add(request):
	fish = Fish.objects.get(pk=1)
	
	 return render_to_response('articles/add.html', {'form': fish})
	
    if request.method == 'POST':
        f = FishForm(request.POST, instance=fish)
        if f.is_valid():
			f.save()	
			
			return HttpResponseRedirect('/fish/' + str(f.id))
    else:
        form = FishForm(instance=fish)
    return render_to_response('articles/add.html', {'form': form})
from django.template import Context, loader
from django.http import HttpResponse
from aquaticore.fish.models import Fish, FishFamily, CommonName, FishOrigin, Diet, FishOrder
from django.shortcuts import render_to_response, get_object_or_404
from datetime import datetime
from math import *
from flickrapi import FlickrAPI
from django.core.cache import cache
from django.forms import ModelForm
import datetime

def index(request):
	fish_list = Fish.objects.all().order_by('-created')[:10]
	return render_to_response('fish/index.html', {'fish_list' : fish_list})

def top10(request):	
	top10_fish_list = Fish.objects.all().order_by('-created')[:10]
	return render_to_response('fish/top10.html', {'top10_fish_list' : top10_fish_list})
	
def detail(request, fish_id):
	fish = get_object_or_404(Fish, pk=fish_id)
	
	# diet = Diet(title="Flakes", created=datetime.datetime.now())
	# diet.save()
	# 
	# fish.diet.add(diet)
	
	
	
	# fish_origin = FishOrigin(title="Indonesia", created=datetime.datetime.now())
	# fish_origin.save()
	# 
	# fish.origin.add(fish_origin)
	
	common_names = CommonName.objects.filter(fish=fish).distinct()
	diets        = Diet.objects.filter(fish=fish)
	fish_origins = FishOrigin.objects.filter(fish=fish)

	# Flickr Photos
	flickr = FlickrAPI('12ac22376b8bdd0127b4d78eb5b8eae9', cache=True)
	flickr.cache = cache
	
	photos = flickr.photos_search(text=fish.scientific_name, sort="interestingness-desc", per_page='10')
	flickr_photos = []
	
	# return render_to_response('fish/detail.html', {'common_name' : photos.photos[0]['total']})
	
	if photos.photos[0]['total'] != '0':
		photos = photos.photos[0]
	
		# Add sizes for each image
		for photo in photos.photo:
			photo_sizes = flickr.photos_getSizes(photo_id=photo['id'])
			flickr_photos.append({'source' : photo_sizes.sizes[0].size[1]['source'], 'url' : photo_sizes.sizes[0].size[1]['url']})
	
	return render_to_response('fish/detail.html', {'fish': fish, 
		'common_names' : common_names,
		'diets' : diets,
		'fish_origins' : fish_origins,
		'flickr_photos' : flickr_photos,
		'max_size_in' : fish.max_size * 0.39, 
		'min_size_in' : fish.min_size * 0.39, 
		'max_temp_f' : ((fish.max_temp * 9) / 5) + 32, 
		'min_temp_f' : ((fish.min_temp * 9) / 5) + 32})

def diet_detail(request, diet_id):
	diet = get_object_or_404(Diet, pk=diet_id)
	fishes = Fish.objects.filter(diet=diet)

	return render_to_response('diet/detail.html', {'diet' : diet, 'fishes' : fishes})

def origin_detail(request, origin_id):
	origin = get_object_or_404(FishOrigin, pk=origin_id)
	fishes = Fish.objects.filter(origin=origin)

	return render_to_response('origin/detail.html', {'origin' : origin, 'fishes' : fishes})

def common_name_detail(request, common_name_id):
	common_name = get_object_or_404(CommonName, pk=common_name_id)
	fishes = Fish.objects.filter(commonname=common_name)

	return render_to_response('common_name/detail.html', {'common_name' : common_name, 'fishes' : fishes})

def add(request):
	
	# fo = FishOrder(title="Perciformes", created=datetime.datetime.now())
	# fo.save()
	# 
	# # ff = FishFamily.objects.get(title="Melanotaeniidae")
	# ff = FishFamily(title="Cichlidae", order=fo, created=datetime.datetime.now())
	# ff.save()
	# # 
	# # # 
	# f = Fish(scientific_name='Mikrogeophagus ramirezi', family=ff, created=datetime.datetime.now(), min_ph='5.0', max_ph='6.0', min_size='6', max_size='7', min_temp='25', max_temp='29')
	# f.save()
	# # 
	# fish_origin = FishOrigin(title="Venezuela", created=datetime.datetime.now())
	# fish_origin.save()
	# 
	# f.origin.add(fish_origin)
	# 
	# fish_origin = FishOrigin(title="Colombia", created=datetime.datetime.now())
	# fish_origin.save()
	# 
	# f.origin.add(fish_origin)
	# # 
	# # 
	# # 
	# # 
	# # 
	# return render_to_response('fish/add.html')
	
	
	fish = Fish.objects.get(pk=1)
	
	class FishForm(ModelForm):
		class Meta:
			model = fish

	if request.method == 'POST':
		f = FishForm(request.POST, instance=fish)
		if f.is_valid():
			f.save()
			return HttpResponseRedirect('/fish/' + str(f.id))
	else:
		form = FishForm(instance=fish)
	
	return render_to_response('fish/add.html', {'form': form})
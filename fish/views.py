from django.template import Context, loader, RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from aquaticore.fish.models import *
from django.shortcuts import render_to_response, get_object_or_404
from datetime import datetime
from math import *
from flickrapi import FlickrAPI
from django.core.cache import cache
from django.forms import ModelForm
import datetime
from django.core.exceptions import ObjectDoesNotExist

def index(request):
	fish_list = Fish.objects.all().order_by('-created')[:40]
	return render_to_response('fish/index.html', {'fish_list' : fish_list}, context_instance=RequestContext(request))

def top10(request):	
	fish_tmp_list = Fish.objects.all().order_by('-created')[:40]

	fish_list = []

	for fish in fish_tmp_list:
		# Photos
		photo = fish.get_flickr_photos(1)
		
		# Origins
		origins = FishOrigin.objects.filter(fish=fish)
		
		fish_list.append({'fish' : fish, 'photo' : photo, 'origins' : origins})

	return render_to_response('fish/top10.html', {'fish_list' : fish_list}, context_instance=RequestContext(request))
	
def newest(request):	
	fish_tmp_list = Fish.objects.all().order_by('-created')[:40]
	
	fish_list = []
	
	for fish in fish_tmp_list:
		# Photos
		photos = fish.get_flickr_photos(1)

		if len(photos) == 0:
			photo = []
		else:
			photo = photos[0]
		
		# Origins			
		origins = FishOrigin.objects.filter(fish=fish)
		
		fish_list.append({'fish' : fish, 'photo' : photo, 'origins' : origins})
		
	return render_to_response('fish/newest.html', {'fish_list' : fish_list}, context_instance=RequestContext(request))
	
def detail(request, fish_id):
	fish = get_object_or_404(Fish, pk=fish_id)
	
	if request.method == 'POST':
		if request.POST['action'] == 'add_origin':
			try:
				fish_origin = FishOrigin.objects.get(title__exact=request.POST['title'])
			except ObjectDoesNotExist:
				fish_origin = FishOrigin(title=request.POST['title'], created=datetime.datetime.now())
				fish_origin.save()

			fish.origin.add(fish_origin)
			return HttpResponseRedirect('/fish/' + str(fish.id))

		if request.POST['action'] == 'add_diet':
			try:
				diet = Diet.objects.get(title__exact=request.POST['title'])
			except ObjectDoesNotExist:
				diet = Diet(title=request.POST['title'], created=datetime.datetime.now())
				diet.save()
				
			fish.diet.add(diet)
			return HttpResponseRedirect('/fish/' + str(fish.id))

		if request.POST['action'] == 'add_common_name':
			try:
				cn = CommonName.objects.get(title__exact=request.POST['title'])
			except ObjectDoesNotExist:
				cn = CommonName(title=request.POST['title'], created=datetime.datetime.now())
				cn.save()
				
			fish.cn.add(cn)
			return HttpResponseRedirect('/fish/' + str(fish.id))
	
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

	flickr_photos = fish.get_flickr_photos(limit=13, first_large=True)
	
	# return render_to_response('fish/detail.html', {'cn' : flickr_photos})
	
	return render_to_response('fish/detail.html', {'fish': fish, 
		'common_names' : common_names,
		'diets' : diets,
		'fishbase_info' : fish.get_fishbase_info(),
		'fish_origins' : fish_origins,
		'flickr_photos' : flickr_photos,
		'max_size_in' : fish.max_size * 0.39, 
		'min_size_in' : fish.min_size * 0.39, 
		'max_temp_f' : ((fish.max_temp * 9) / 5) + 32, 
		'min_temp_f' : ((fish.min_temp * 9) / 5) + 32}, context_instance=RequestContext(request))

def diet_detail(request, diet_id):
	diet = get_object_or_404(Diet, pk=diet_id)
	fishes = Fish.objects.filter(diet=diet)
	return render_to_response('diet/detail.html', {'diet' : diet, 'fishes' : fishes}, context_instance=RequestContext(request))
	
def diet_delete(request, diet_id):
	diet = get_object_or_404(Diet, pk=diet_id)
	diet.delete()	
	return HttpResponseRedirect(request.META['HTTP_REFERER'])

def origin_detail(request, origin_id):
	origin = get_object_or_404(FishOrigin, pk=origin_id)
	fishes = Fish.objects.filter(origin=origin)
	
	fish_list = []
	
	for fish in fishes:
		# Photos
		photos = fish.get_flickr_photos(1)

		if len(photos) == 0:
			continue

		photo = photos[0]
		
		# Origins		
		origins = FishOrigin.objects.filter(fish=fish)
		
		fish_list.append({'fish' : fish, 'photo' : photo, 'origins' : origins})
	
	return render_to_response('origin/detail.html', {'origin' : origin, 'fish_list' : fish_list}, context_instance=RequestContext(request))
	
def origin_delete(request, origin_id):
	origin = get_object_or_404(FishOrigin, pk=origin_id)
	origin.delete()
	return HttpResponseRedirect(request.META['HTTP_REFERER'])

def common_name_detail(request, common_name_id):
	common_name = get_object_or_404(CommonName, pk=common_name_id)
	fishes = Fish.objects.filter(commonname=common_name)
	return render_to_response('common_name/detail.html', {'common_name' : common_name, 'fishes' : fishes}, context_instance=RequestContext(request))

def common_name_delete(request, common_name_id):
	common_name = get_object_or_404(CommonName, pk=common_name_id)
	common_name.delete()

	return HttpResponseRedirect(request.META['HTTP_REFERER'])


def class_detail(request, class_id):
	fish_class = get_object_or_404(FishClass, pk=class_id)
	family_list = FishOrder.objects.filter(fish_class=fish_class)

	fishes = []

	for family in family_list:
		genus_list = FishGenus.objects.filter(family=family)		

		for genus in genus_list:
			species_list = FishSpecies.objects.filter(genus=genus)

			for species in species_list:
				fish_list = Fish.objects.filter(species=species)

				for fish in fish_list:
					fishes.append(fish)

	fish_list = []

	for fish in fishes:
		# Photos
		photos = fish.get_flickr_photos(1)

		if len(photos) == 0:
			continue

		photo = photos[0]

		# Origins

		origins = FishOrigin.objects.filter(fish=fish)
		
		fish_list.append({'fish' : fish, 'photo' : photo, 'origins' : origins})

	return render_to_response('class/detail.html', {'class' : fish_class, 'fish_list' : fish_list}, context_instance=RequestContext(request))


# Order

def order_detail(request, order_id):
	order = get_object_or_404(FishOrder, pk=order_id)
	family_list = FishFamily.objects.filter(order=order)

	fishes = []
	
	for family in family_list:
		genus_list = FishGenus.objects.filter(family=family)		
		
		for genus in genus_list:
			species_list = FishSpecies.objects.filter(genus=genus)
		
			for species in species_list:
				fish_list = Fish.objects.filter(species=species)

				for fish in fish_list:
					fishes.append(fish)
	
	fish_list = []
	
	for fish in fishes:
		# Photos
		photos = fish.get_flickr_photos(1)

		if len(photos) == 0:
			continue

		photo = photos[0]
		
		# Origins
		
		origins = FishOrigin.objects.filter(fish=fish)
		
		fish_list.append({'fish' : fish, 'photo' : photo, 'origins' : origins})
					
	return render_to_response('order/detail.html', {'order' : order, 'fish_list' : fish_list}, context_instance=RequestContext(request))
	
# Family

def family_detail(request, family_id):
	family = get_object_or_404(FishFamily, pk=family_id)
	genus_list = FishGenus.objects.filter(family=family)

	fishes = []

	for genus in genus_list:
		species_list = FishSpecies.objects.filter(genus=genus)
		
		for species in species_list:
			fish_list = Fish.objects.filter(species=species)

			for fish in fish_list:
				fishes.append(fish)

	fish_list = []

	for fish in fishes:
		# Photos
		photos = fish.get_flickr_photos(1)

		if len(photos) == 0:
			continue

		photo = photos[0]
		
		# Origins
		
		origins = FishOrigin.objects.filter(fish=fish)
		
		fish_list.append({'fish' : fish, 'photo' : photo, 'origins' : origins})

	return render_to_response('family/detail.html', {'family' : family, 'fish_list' : fish_list}, context_instance=RequestContext(request))

# Genus

def genus_detail(request, genus_id):
	genus = get_object_or_404(FishGenus, pk=genus_id)
	species_list = FishSpecies.objects.filter(genus=genus)
	
	fishes = []
	
	for species in species_list:
		fish_list = Fish.objects.filter(species=species)
		
		for fish in fish_list:
			fishes.append(fish)
			
	fish_list = []

	for fish in fishes:
		# Photos
		photos = fish.get_flickr_photos(1)

		if len(photos) == 0:
			continue

		photo = photos[0]
		
		# Origins
		
		origins = FishOrigin.objects.filter(fish=fish)
		
		fish_list.append({'fish' : fish, 'photo' : photo, 'origins' : origins})
		
	return render_to_response('genus/detail.html', {'genus' : genus, 'fish_list' : fish_list}, context_instance=RequestContext(request))

def add(request):
	fish = Fish()

	if request.method == 'POST':
		form = FishForm(request.POST, instance=fish)
		if form.is_valid():
			fish = Fish(request.POST)
			fish.save()
			return HttpResponseRedirect('/fish/' + str(fish.id))
	else:
		form = FishForm(instance=fish)
	
	return render_to_response('fish/add.html', {'form': form}, context_instance=RequestContext(request))
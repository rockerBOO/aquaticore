from django.template import Context, loader, RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from aquaticore.aquariums.models import Aquarium
# from aquaticore.fish.models import FishOrigin
from django.http import HttpResponseRedirect
from django import forms
import datetime

def index(request):
    # return render_to_response('aquarium/index.html', {'aquarium_list' : aquarium_list}, context_instance=RequestContext(request))
    
    aquariums_list = Aquarium.objects.all()
    return render_to_response('aquarium/index.html', {'aquariums_list': aquariums_list}, context_instance=RequestContext(request))
	
def detail(request, aquarium_id):
	aquarium = get_object_or_404(Aquarium, pk=aquarium_id)
	fish_tmp_list = aquarium.fish.all()
	
	fish_list = []
	
	for fish in fish_tmp_list:
		# Photos
		photos = fish.get_flickr_photos(1)

		if len(photos) == 0:
			photo = []
		else:
			photo = photos[0]
		
		# Origins			
        # origins = FishOrigin.objects.filter(fish=fish)
        # origins = []
		
        # fish_list.append({'fish' : fish, 'photo' : photo, 'origins' : origins})
		fish_list.append({'fish' : fish, 'photo' : photo})
	
	return render_to_response('aquarium/detail.html', {'aquarium' : aquarium, 'fish_list' : fish_list}, context_instance=RequestContext(request))
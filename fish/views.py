from django.template import Context, loader
from django.http import HttpResponse
from aquaticore.fish.models import Fish, FishFamily, CommonName
from django.shortcuts import render_to_response, get_object_or_404
from datetime import datetime
from math import *

def index(request):
	fish_list = Fish.objects.all().order_by('-created')[:10]
	return render_to_response('fish/index.html', {'fish_list' : fish_list})

def top10(request):
	# ff = FishFamily(title='Melanotaeniidae')
	# 
	# # return render_to_response('fish/top10.html', {'ff' : ff})
	# 
	# if ff.id == None:
	# 	ff = FishFamily(title='Melanotaeniidae', created=datetime.now())
	# 	ff.save()
	# 
	# # return render_to_response('fish/top10.html', {'ff' : ff.id})
	# 
	# f = Fish(scientific_name='Melanotaenia boesemani', family=ff, created=datetime.now(), min_ph='6.8', max_ph='7.2', min_size='7', max_size='9', min_temp='27', max_temp='30')
	# f.save()
	
	top10_fish_list = Fish.objects.all().order_by('-created')[:10]
	return render_to_response('fish/top10.html', {'top10_fish_list' : top10_fish_list})
	
def detail(request, fish_id):
	fish = get_object_or_404(Fish, pk=fish_id)
	
	cn = CommonName(title="Frozen Bloodworms")	
	
	if cn.id == None:
		cn = CommonName(title="Frozen Bloodworms", created=datetime.now())
		cn.save()
	
	# return render_to_response('fish/detail.html', {'cn' : cn})
	
	fish.commonname = cn
	
	fish.save()
	
	return render_to_response('fish/detail.html', {'cn' : fish})
		
	return render_to_response('fish/detail.html', {'fish': fish, 
		'max_size_in' : fish.max_size * 0.39, 
		'min_size_in' : fish.min_size * 0.39, 
		'max_temp_f' : ((fish.max_temp * 9) / 5) + 32, 
		'min_temp_f' : ((fish.min_temp * 9) / 5) + 32})
	
	
		

def add(request):
	fish = Fish()
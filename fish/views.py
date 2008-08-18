from django.template import Context, loader
from django.http import HttpResponse
from aquaticore.fish.models import Fish
from django.shortcuts import render_to_response, get_object_or_404

def index(request):
    return render_to_response('fish/index.html')

def top10(request):
	top10_fish_list = Fish.objects.all().order_by('-created')[:10]
	return render_to_response('fish/top10.html', {'top10_fish_list' : top10_fish_list})
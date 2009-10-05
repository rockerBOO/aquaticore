from django.template import Context, loader, RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from aquaticore.databases.models import Database
from aquaticore.specialists.models import Specialist
# from aquaticore.fish.models import FishOrigin
from django.http import HttpResponseRedirect
from django import forms
import datetime

def index(request):
    # return render_to_response('aquarium/index.html', {'aquarium_list' : aquarium_list}, context_instance=RequestContext(request))
    
    database_list = Database.objects.all()
    return render_to_response('database/index.html', {'database_list': database_list}, context_instance=RequestContext(request))
	
def detail(request, database_id):
	database = get_object_or_404(Database, pk=database_id)	
	
	specialists = Specialist.objects.filter(database=database)
	
	return render_to_response('database/detail.html', {'database' : database, 'specialists': specialists}, context_instance=RequestContext(request))
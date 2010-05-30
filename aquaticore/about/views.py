from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404

def index(result):
    return render_to_response('about/index.html')

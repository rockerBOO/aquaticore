from django.template import Context, loader
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from aquaticore.blogs.models import Blog

def index(request):
    latest_entry_list = Blog.objects.all().order_by('-created')[:5]
    return render_to_response('blogs/index.html', {'latest_entry_list': latest_entry_list})
    
def detail(request, entry_id):
    entry = get_object_or_404(Blog, pk=entry_id)
    return render_to_response('blogs/detail.html', {'entry': entry})

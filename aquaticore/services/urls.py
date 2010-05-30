from django.template import Context, loader
from django.http import HttpResponse

def index(request):
    return render_to_response('plant/index.html')
from django import forms
from django.template import Context, loader, RequestContext
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

def join(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # Do form processing here...
			user = User.objects.create_user(request.POST['username'], 'no@g.com', request.POST['password1'])
			user.save()
			
			user = authenticate(username=user.username, password=user.password)

			if user is not None:
				if user.is_active:
					request.POST['password'] = request.POST['password1']
					login(request, user)
					return HttpResponseRedirect('/accounts/profile/')
					
			return HttpResponseRedirect('/accounts/join/')
		    
    else:
        form = UserCreationForm()
    return render_to_response('aquaticore/join.html', {'form': form}, context_instance=RequestContext(request))

def profile(request):
	return render_to_response('aquaticore/profile.html', context_instance=RequestContext(request))
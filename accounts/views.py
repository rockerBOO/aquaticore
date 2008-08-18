from django import forms
from django.template import Context, loader
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect

class AccountJoinForm(forms.Form):
    email    = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput, min_length=6)


def join(request):
    if request.method == 'POST':
        form = AccountJoinForm(request.POST)
        if form.is_valid():
            # Do form processing here...
            return HttpResponseRedirect('/accounts/profile/')
    else:
        form = AccountJoinForm()
    return render_to_response('aquaticore/join.html', {'form': form})

from django.conf.urls.defaults import *

urlpatterns = patterns('aquaticore.accounts.views.',
    (r'^join/$',    'join'),
	(r'^profile/$', 'profile'),
	(r'^login/$',   'django.contrib.auth.views.login', {'template_name': 'aquaticore/login.html'}),
	(r'^logout/$',  'django.contrib.auth.views.logout', {'template_name' : 'aquaticore/logout.html'})
)

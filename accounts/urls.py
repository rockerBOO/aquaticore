from django.conf.urls.defaults import *

urlpatterns = patterns('aquaticore.accounts.views.',
    (r'^join/$',    'join'),
	(r'^profile/$', 'profile'),
)

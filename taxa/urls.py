from django.conf.urls.defaults import *

urlpatterns = patterns('aquaticore.taxa.views',
    (r'^$',                          'index'),
    (r'^species/(?P<species_name>[^\/]+)/?',      'species_detail'),
	(r'^family/(?P<family_name>[^\/]+)/?',      'family_detail'),
)

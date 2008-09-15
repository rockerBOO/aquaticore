from django.conf.urls.defaults import *

urlpatterns = patterns('aquaticore.taxa.views',
    (r'^$',                          'index'),
    (r'^(?P<species_name>[^\/]+)/?',      'detail'),
)

from django.conf.urls.defaults import *

urlpatterns = patterns('aquaticore.aquariums.views',
    (r'^$',                          'index'),
    (r'^(?P<aquarium_id>\d+)/$',      'detail'),
)

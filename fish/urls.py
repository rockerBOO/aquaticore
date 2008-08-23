from django.conf.urls.defaults import *

urlpatterns = patterns('aquaticore.fish.views',
    (r'^$',                           'index'),
	(r'^top10$',                      'top10'),
	(r'^(?P<fish_id>\d+)/?',          'detail'),
	('add/',                          'add')
)

from django.conf.urls.defaults import *

urlpatterns = patterns('aquaticore.fish.views',
    (r'^$',                           'index'),
	(r'^top10$',                      'top10'),
	(r'^(?P<fish_id>\d+)/?',          'detail'),
	('add/',                          'add'),
	
	(r'^diet/(?P<diet_id>\d+)/?$',    'diet_detail'),
	(r'^diet/(?P<diet_id>\d+)/delete/?$',    'diet_delete'),
	
	(r'^origin/(?P<origin_id>\d+)/?$',                  'origin_detail'),
	(r'^origin/(?P<origin_id>\d+)/delete/?$',           'origin_delete'),
	
	(r'^common_name/(?P<common_name_id>\d+)/?$',        'common_name_detail'),
	(r'^common_name/(?P<common_name_id>\d+)/delete/?$', 'common_name_delete'),
)

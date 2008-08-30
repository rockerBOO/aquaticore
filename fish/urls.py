from django.conf.urls.defaults import *

urlpatterns = patterns('aquaticore.fish.views',
    (r'^$',                           'index'),
	(r'^top10/?$',                      'top10'),
	(r'^newest/?$',                      'newest'),
	(r'^(?P<fish_id>\d+)/?',          'detail'),
	('add/',                          'add'),
	
	(r'^diet/(?P<diet_id>\d+)/?$',    'diet_detail'),
	(r'^diet/(?P<diet_id>\d+)/delete/?$',    'diet_delete'),
	
	(r'^origin/(?P<origin_id>\d+)/?$',                  'origin_detail'),
	(r'^origin/(?P<origin_id>\d+)/delete/?$',           'origin_delete'),
	
	(r'^common_name/(?P<common_name_id>\d+)/?$',        'common_name_detail'),
	(r'^common_name/(?P<common_name_id>\d+)/delete/?$', 'common_name_delete'),
	
	(r'^genus/(?P<genus_id>\d+)/?$',        'genus_detail'),
	
	(r'^family/(?P<family_id>\d+)/?$',        'family_detail'),
	
	(r'^order/(?P<order_id>\d+)/?$',        'order_detail'),
	
	(r'^class/(?P<class_id>\d+)/?$',        'class_detail'),
)

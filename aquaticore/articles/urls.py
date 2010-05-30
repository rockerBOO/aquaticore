from django.conf.urls.defaults import *

urlpatterns = patterns('aquaticore.articles.views',
    (r'^$',                          'index'),
    (r'^(?P<article_id>\d+)/$',      'detail'),
	(r'^new/$',                      'new'),
	(r'^(?P<article_id>\d+)/delete/$',      'delete'),
)

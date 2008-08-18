from django.conf.urls.defaults import *
from django.contrib.comments.models import FreeComment

urlpatterns = patterns('aquaticore.articles.views',
    (r'^$',                          'index'),
    (r'^(?P<article_id>\d+)/$',      'detail'),
	(r'^new/$',                      'new'),
	(r'^(?P<article_id>\d+)/delete/$',      'delete'),
    (r'^(\d+)/comments/postfree/$',  'article_post_free_comment'),
    (r'^(\d+)/comments/',            include('django.contrib.comments.urls.comments'))
)

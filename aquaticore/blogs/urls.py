from django.conf.urls.defaults import *

urlpatterns = patterns('aquaticore.blogs.views.',
    (r'^$',                    'index'),
    (r'^(?P<entry_id>\d+)/$', 'detail')
)

#urlpatterns = patterns('',
#    url(r'^(?P<object_id>\d+)/results/$', 'django.views.generic.list_detail.object_detail', dict(info_dict, template_name='polls/results.html'), 'poll_results'),
#    (r'^(?P<poll_id>\d+)/vote/$', 'mysite.polls.views.vote'),
#)

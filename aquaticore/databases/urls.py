from django.conf.urls.defaults import *

urlpatterns = patterns('aquaticore.databases.views',
    (r'^$',                          'index'),
    (r'^(?P<database_id>\d+)/$',      'detail'),
)

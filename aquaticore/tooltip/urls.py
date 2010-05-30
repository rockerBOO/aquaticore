from django.conf.urls.defaults import *

urlpatterns = patterns('aquaticore.tooltip.views',
    (r'^$',                          'index'),
    (r'(?P<tt_type>[^:]+):(?P<name>[^\/]+)/?',                          'index'),
)

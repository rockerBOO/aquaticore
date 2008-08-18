from django.conf.urls.defaults import *
from django.contrib.comments.models import FreeComment

urlpatterns = patterns('aquaticore.accounts.views.',
    (r'^join/$',                          'join'),
)

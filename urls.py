from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^aquaticore/', include('aquaticore.foo.urls')),

    # Uncomment the next line to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line for to enable the admin:
    (r'^admin/(.*)',         admin.site.root),
    (r'^blogs/',             include('aquaticore.blogs.urls')),
    (r'^articles/',          include('aquaticore.articles.urls')),
    (r'^about/',             include('aquaticore.about.urls')),
	(r'^fish/',              include('aquaticore.fish.urls')),
	(r'^plants/',            include('aquaticore.plant.urls')),
	(r'^accounts/login/$',   'django.contrib.auth.views.login', {'template_name': 'aquaticore/login.html'}),
	(r'^accounts/',          include('aquaticore.accounts.urls')),
	(r'^feeds/',             include('aquaticore.feeds.urls')),
    (r'^/$',                 include('django.contrib.flatpages.urls')),
)

from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin
from django.contrib import admindocs

# Uncomment the next two lines to enable the admin:
admin.autodiscover()

urlpatterns = patterns('',
	# Uncomment the next line for to enable the admin:
    (r'^admin/', include(admin.site.urls)),

    # Uncomment the next line to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # (r'^feeds/(?P<url>.*)/$', 'django.contrib.syndication.views.feed', {'feed_dict': feeds}),

	(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
	
    (r'^blogs/',             include('aquaticore.blogs.urls')),
    (r'^articles/',          include('aquaticore.articles.urls')),
	(r'^fish/',              include('aquaticore.taxa.urls')),
	(r'^taxa/',              include('aquaticore.taxa.urls')),
	(r'^tooltip/',           include('aquaticore.tooltip.urls')),
	(r'^plants/',            include('aquaticore.plant.urls')),
	(r'^accounts/',          include('aquaticore.accounts.urls')),
	(r'^login/',             include('aquaticore.accounts.urls')),
	(r'^aquariums/',         include('aquaticore.aquariums.urls')),
	(r'^aquarium/',          include('aquaticore.aquariums.urls')),
    # (r'^privacy/',           ),
    
    (r'', include('django.contrib.flatpages.urls')),
)

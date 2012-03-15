from django.conf.urls.defaults import *
#from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from braatpaq import settings

from braatpaq.views import home_page, features_page, accessories_page

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    ('^$', home_page),                      # Home page
    ('^features/$', features_page),         # Features page
    ('^accessories/$', accessories_page),   # Accessories page

    # This line is a hack so that the resources in the static folder can be displayed.
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_URL, 'show_indexes': True}
        ),

    # Example:
    # (r'^braatpaq/', include('braatpaq.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)
#urlpatterns += staticfiles_urlpatterns()
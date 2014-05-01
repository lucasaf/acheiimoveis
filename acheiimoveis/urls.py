from django.conf.urls import patterns, include, url
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    #
    url(r'^admin/', include(admin.site.urls)),
    url(r'^addresses/', include('acheiimoveis.addresses.urls')),
    url(r'', include('acheiimoveis.core.urls', namespace='core')),
)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

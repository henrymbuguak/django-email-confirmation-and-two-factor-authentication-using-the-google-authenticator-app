from django.contrib import admin
from django.conf.urls import include, url


urlpatterns = [
    url('^admin/', admin.site.urls),
    url('^', include('dja_profile.urls')),
    url('^accounts/', include('django.contrib.auth.urls')),
    url(r'^settings/', include('django_mfa.urls', namespace="mfa")),
]

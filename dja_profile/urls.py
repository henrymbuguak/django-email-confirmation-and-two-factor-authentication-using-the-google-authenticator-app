from django.conf.urls import url
from . import views

app_name = 'dja_profile'

urlpatterns = [
    url(r'^$', views.signup, name='register_user'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
]


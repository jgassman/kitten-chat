from django.conf.urls import url
from django.contrib.auth import views as auth_views

from registration import views as registration_views

urlpatterns = [
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^sign_up/$', registration_views.sign_up, name='sign_up'),
]

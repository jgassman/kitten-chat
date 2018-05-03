from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from chat import urls as chat_urls

print(chat_urls)

urlpatterns = [
    url(r'^chat/', include(chat_urls)),
    url(r'^login/$', auth_views.login),
    url(r'^logout/$', auth_views.logout),
    url(r'^admin/', admin.site.urls),
]

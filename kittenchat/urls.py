from django.conf.urls import include, url
from django.contrib import admin

from chat import urls as chat_urls
from registration import urls as registration_urls


urlpatterns = [
    url(r'^chat/', include(chat_urls, namespace='chat')),
    url(r'^registration/', include(registration_urls, namespace='registration')),
    url(r'^admin/', admin.site.urls),
]

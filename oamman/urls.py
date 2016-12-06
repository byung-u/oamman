from django.conf.urls import url, include
from django.contrib import admin

from base.views import index

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', index, name='index'),
]

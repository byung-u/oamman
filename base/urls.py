# -*- coding: utf-8 -*-
from django.conf.urls import url
import views

urlpatterns = patterns(
    url(r'^list$', views.list_users, name='list_users'),
)

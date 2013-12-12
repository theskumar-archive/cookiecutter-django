# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url, patterns, include
from rest_framework import routers

from .views import UserViewSet

# Routers provide an easy way of automatically determining the URL conf
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)


# Wire up our API using automatic URL routing.
# Additionally, include login URLs for the browseable API.
urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)

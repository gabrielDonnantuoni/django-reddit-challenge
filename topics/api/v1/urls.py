"""
Topics URL Configuration
"""
###
# Libraries
###
from django.conf.urls import url, include
from rest_framework_nested.routers import DefaultRouter, NestedSimpleRouter

from topics.api.v1.views import TopicViewSet

###
# Routers
###
router = DefaultRouter()
router.register('topics', TopicViewSet)


###
# URL Patterns
###
urlpatterns = [
    url(r'', include(router.urls)),
]

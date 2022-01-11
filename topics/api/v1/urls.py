"""
Topics URL Configuration
"""
###
# Libraries
###
from django.conf.urls import url, include
from rest_framework_nested.routers import DefaultRouter, NestedSimpleRouter

from topics.api.v1.views import TopicViewSet
from posts.api.v1.views import NestedPostViewSet

###
# Routers
###
router = DefaultRouter()
router.register('topics', TopicViewSet, basename='topics')

topic_router = NestedSimpleRouter(router, 'topics', lookup='topic')
topic_router.register('posts', NestedPostViewSet, basename='posts')

###
# URL Patterns
###
urlpatterns = [
    url(r'', include(router.urls)),
    url(r'', include(topic_router.urls)),
]

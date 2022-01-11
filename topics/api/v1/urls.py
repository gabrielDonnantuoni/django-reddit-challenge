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
from comments.api.v1.views import NestedCommentViewSet

###
# Routers
###
router = DefaultRouter()
router.register('topics', TopicViewSet, basename='topics')

topic_router = NestedSimpleRouter(router, 'topics', lookup='topic')
topic_router.register('posts', NestedPostViewSet, basename='posts')

post_router = NestedSimpleRouter(topic_router, 'posts', lookup='post')
post_router.register('comments', NestedCommentViewSet, basename='comments')

###
# URL Patterns
###
urlpatterns = [
    url(r'', include(router.urls)),
    url(r'', include(topic_router.urls)),
    url(r'', include(post_router.urls)),
]

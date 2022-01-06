"""
Topics URL Configuration
"""
###
# Libraries
###
from django.conf.urls import url, include
from rest_framework_nested.routers import DefaultRouter, NestedSimpleRouter


###
# Routers
###
router = DefaultRouter()


###
# URL Patterns
###
urlpatterns = [
    url(r'', include(router.urls)),
]

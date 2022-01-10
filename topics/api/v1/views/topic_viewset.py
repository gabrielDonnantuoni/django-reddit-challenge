"""
API V1: Topic ViewSet
"""
###
# Libraries
###
from topics.models import Topic
from rest_framework import viewsets, permissions

from topics.api.v1.serializers import (
    TopicListSerializer,
    TopicDetailSerializer,
)
from helpers.permissions import IsOwnerOrReadOnly


###
# ViewSet
###
class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all().order_by('slug')
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly,
    ]
    lookup_field = 'slug'

    def get_serializer_class(self):
        if self.action == 'list':
            return TopicListSerializer
        return TopicDetailSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

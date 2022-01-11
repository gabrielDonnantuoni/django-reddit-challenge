"""
API V1: Topic ViewSet
"""
###
# Libraries
###
from posts.models import Post
from rest_framework import viewsets, permissions

from posts.api.v1.serializers import (
    PostListSerializer,
    PostDetailSerializer,
)
from helpers.permissions import IsOwnerOrReadOnly
from helpers.services import VotesService, DeleteService


###
# ViewSet
###
class NestedPostViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly,
    ]

    def get_queryset(self):
        topic_slug = self.kwargs.get('topic_slug')
        qs = Post.objects.filter(topic__slug=topic_slug)
        return VotesService(qs=qs).get_votes_count_query()

    def get_serializer_class(self):
        if self.action == 'list':
            return PostListSerializer
        return PostDetailSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_destroy(self, instance):
        DeleteService(instance).update_author_to_deleted()

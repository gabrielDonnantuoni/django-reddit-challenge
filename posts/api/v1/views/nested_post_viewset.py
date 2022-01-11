"""
API V1: Post ViewSet
"""
###
# Libraries
###
from rest_framework import viewsets

from topics.models import Topic
from posts.models import Post
from posts.api.v1.serializers import (
    PostListSerializer,
    PostDetailSerializer,
)
from helpers.views import VotesViewSetMixin
from helpers.services import VotesService, DeleteService


###
# ViewSet
###
class NestedPostViewSet(VotesViewSetMixin, viewsets.ModelViewSet):
    def get_queryset(self):
        topic_slug = self.kwargs.get('topic_slug')
        qs = Post.objects.filter(topic__slug=topic_slug)
        qs = VotesService(queryset=qs).get_query_by_request(self.request)
        return qs.order_by('-up_votes_count')

    def get_serializer_class(self):
        if self.action == 'list':
            return PostListSerializer
        return PostDetailSerializer

    def perform_create(self, serializer):
        topic_slug = self.kwargs.get('topic_slug')
        topic = Topic.objects.get(slug=topic_slug)
        author = self.request.user
        serializer.save(author=author, topic=topic)

    def perform_destroy(self, instance):
        DeleteService(instance).update_author_to_deleted()

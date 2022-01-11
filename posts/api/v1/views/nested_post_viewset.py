"""
API V1: Topic ViewSet
"""
###
# Libraries
###
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from topics.models import Topic
from posts.models import Post
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
    def get_permissions(self):
        self.permission_classes = [permissions.IsAuthenticatedOrReadOnly]
        if not self.action.endswith('vote'):
            self.permission_classes.append(IsOwnerOrReadOnly)
        return super().get_permissions()

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

    @action(detail=True, methods=['patch'], url_path='up-vote')
    def up_vote(self, request, *args, **kwargs):
        obj = self.get_object()
        service = VotesService(obj=obj, user=request.user)
        if obj.is_up_voted:
            obj = service.remove_up_vote()
        else:
            obj = service.add_up_vote()

        serializer = self.get_serializer(obj)
        return Response(serializer.data)

    @action(detail=True, methods=['patch'], url_path='down-vote')
    def down_vote(self, request, *args, **kwargs):
        obj = self.get_object()
        service = VotesService(obj=obj, user=request.user)
        if obj.is_down_voted:
            obj = service.remove_down_vote()
        else:
            obj = service.add_down_vote()

        serializer = self.get_serializer(obj)
        return Response(serializer.data)

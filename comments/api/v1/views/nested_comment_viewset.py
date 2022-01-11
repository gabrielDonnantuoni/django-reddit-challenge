"""
API V1: Nested Comment ViewSet
"""
###
# Libraries
###
from rest_framework import viewsets

from posts.models import Post
from comments.models import Comment
from comments.api.v1.serializers import (
    CommentListSerializer,
    CommentDetailSerializer,
)
from helpers.views import VotesViewSetMixin
from helpers.services import VotesService, DeleteService


###
# ViewSet
###
class NestedCommentViewSet(VotesViewSetMixin, viewsets.ModelViewSet):
    def get_queryset(self):
        post_pk = self.kwargs.get('post_pk')
        qs = Comment.objects.filter(post=post_pk)
        if self.action == 'list':
            qs = qs.filter(parent_comment__isnull=True)
        qs = VotesService(queryset=qs).get_query_by_request(self.request)
        return qs.order_by('-up_votes_count')

    def get_serializer_class(self):
        if self.action == 'list':
            return CommentListSerializer
        return CommentDetailSerializer

    def perform_create(self, serializer):
        post_pk = self.kwargs.get('post_pk')
        post = Post.objects.get(pk=post_pk)
        author = self.request.user
        serializer.save(author=author, post=post)

    def perform_destroy(self, instance):
        DeleteService(instance).update_author_to_deleted()

"""
API V1: Post Detail Serializer
"""
###
# Libraries
###
from rest_framework import serializers

from posts.models import Post, Tag
from comments.api.v1.serializers import CommentListSerializer
from helpers.custom_fields import NameRelatedField
from helpers.services import VotesService

from .post_list_serializer import PostListSerializer


###
# Serializer
###
class PostDetailSerializer(PostListSerializer):
    author = NameRelatedField(read_only=True, lookup='username')
    tags = NameRelatedField(queryset=Tag.objects.all(), many=True)
    top_comments = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = (
            'id', 'title', 'content', 'author', 'up_votes',
            'down_votes', 'user_vote_status', 'tags',
            'created_at', 'updated_at', 'top_comments',
        )
        read_only_fields = ('created_at', 'updated_at')

    def get_top_comments(self, obj):
        request = self.context['request']
        qs = obj.comments.filter(parent_comment__isnull=True)
        qs = VotesService(queryset=qs).get_query_by_request(request)
        qs = qs.order_by('-up_votes_count')[:5]
        return CommentListSerializer(
            instance=qs,
            many=True,
            context={'request': request},
        ).data

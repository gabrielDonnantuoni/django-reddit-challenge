"""
API V1: Comment Detail Serializer
"""
###
# Libraries
###
from rest_framework import serializers

from comments.models import Comment
from helpers.custom_fields import NameRelatedField

from .comment_list_serializer import CommentListSerializer


###
# Serializer
###
class CommentDetailSerializer(CommentListSerializer):
    author = NameRelatedField(read_only=True, lookup='username')
    parent_comment = serializers.PrimaryKeyRelatedField(
        queryset=Comment.objects.all(),
        required=False,
    )

    class Meta:
        model = Comment
        fields = (
            'id', 'content', 'up_votes', 'down_votes',
            'user_vote_status', 'author', 'replies',
            'created_at', 'updated_at', 'parent_comment',
        )

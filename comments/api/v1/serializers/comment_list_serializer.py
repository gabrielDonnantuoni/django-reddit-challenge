"""
API V1: Comment List Serializer
"""
###
# Libraries
###
from comments.models import Comment
from rest_framework import serializers

from helpers.services import VotesService


###
# Serializer
###
class CommentListSerializer(serializers.ModelSerializer):
    up_votes = serializers.IntegerField(source='up_votes_count')
    down_votes = serializers.IntegerField(source='down_votes_count')
    replies = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ('id', 'content', 'up_votes', 'down_votes', 'replies')

    def get_replies(self, obj):
        qs = VotesService(qs=obj.replies.all()).get_votes_count_query()
        return CommentListSerializer(
            instance=qs,
            many=True,
        ).data

"""
API V1: Comment List Serializer
"""
###
# Libraries
###
from comments.models import Comment
from rest_framework import serializers

from helpers.services import VotesService
from helpers.serializers import VotesSerializer


###
# Serializer
###
class CommentListSerializer(VotesSerializer):
    replies = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = (
            'id', 'content', 'up_votes', 'down_votes',
            'user_vote_status', 'replies',
        )

    def get_replies(self, obj):
        request = self.context['request']
        qs = obj.replies.all()
        qs = VotesService(queryset=qs).get_query_by_request(request)
        return CommentListSerializer(
            instance=qs,
            many=True,
            context={'request': request},
        ).data

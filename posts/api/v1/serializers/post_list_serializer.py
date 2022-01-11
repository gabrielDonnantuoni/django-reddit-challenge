"""
API V1: Post List Serializer
"""
###
# Libraries
###
from posts.models import Post
# from rest_framework import serializers

from helpers.serializers import VotesSerializer


###
# Serializer
###
class PostListSerializer(VotesSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'up_votes', 'down_votes', 'user_vote_status')

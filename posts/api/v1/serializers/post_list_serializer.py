"""
API V1: Post List Serializer
"""
###
# Libraries
###
from posts.models import Post
from rest_framework import serializers


###
# Serializer
###
class PostListSerializer(serializers.ModelSerializer):
    up_votes = serializers.IntegerField(source='up_votes_count')
    down_votes = serializers.IntegerField(source='down_votes_count')

    class Meta:
        model = Post
        fields = ('id', 'title', 'up_votes', 'down_votes')

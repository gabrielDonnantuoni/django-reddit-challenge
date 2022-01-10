"""
API V1: Topic Detail Serializer
"""
###
# Libraries
###
from rest_framework import serializers

from topics.models import Topic
from posts.api.v1.serializers import PostListSerializer
from helpers.custom_fields import NameRelatedField
from helpers.services import VotesService


###
# Serializer
###
class TopicDetailSerializer(serializers.ModelSerializer):
    author = NameRelatedField(read_only=True, lookup='username')
    better_rated_posts = serializers.SerializerMethodField()

    class Meta:
        model = Topic
        fields = (
            'slug', 'title', 'description', 'author',
            'better_rated_posts',
        )

    def get_better_rated_posts(self, obj):
        qs = VotesService(qs=obj.posts.all()).get_votes_count_query()
        qs = qs.order_by('-up_votes_count')[:5]
        return PostListSerializer(
            instance=qs,
            many=True,
        ).data

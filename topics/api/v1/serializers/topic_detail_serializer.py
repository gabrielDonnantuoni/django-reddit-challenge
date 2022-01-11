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
    top_posts = serializers.SerializerMethodField()

    class Meta:
        model = Topic
        fields = (
            'slug', 'title', 'description', 'author',
            'top_posts',
        )

    def get_top_posts(self, obj):
        request = self.context['request']
        qs = obj.posts.all()
        qs = VotesService(queryset=qs).get_query_by_request(request)
        qs = qs.order_by('-up_votes_count')[:5]
        return PostListSerializer(
            instance=qs,
            many=True,
        ).data

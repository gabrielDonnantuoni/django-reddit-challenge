"""
API V1: Topic Detail Serializer
"""
###
# Libraries
###
from topics.models import Topic
from rest_framework import serializers


###
# Serializer
###
class TopicDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Topic
        fields = ('slug', 'title', 'description', 'author')
        read_only_fields = ('author',)

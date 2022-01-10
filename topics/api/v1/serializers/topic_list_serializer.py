"""
API V1: Topic List Serializer
"""
###
# Libraries
###
from topics.models import Topic
from rest_framework import serializers


###
# Serializer
###
class TopicListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Topic
        fields = ('slug', 'title')

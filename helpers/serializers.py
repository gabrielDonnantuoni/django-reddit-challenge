from rest_framework import serializers


class VotesSerializer(serializers.ModelSerializer):
    up_votes = serializers.IntegerField(
        source='up_votes_count',
        read_only=True,
    )
    down_votes = serializers.IntegerField(
        source='down_votes_count',
        read_only=True,
    )
    user_vote_status = serializers.SerializerMethodField()

    def get_user_vote_status(self, obj):
        is_up = getattr(obj, 'is_up_voted', None)
        if is_up is not None:
            is_down = getattr(obj, 'is_down_voted')
            if is_down:
                return 'down_voted'
            if is_up:
                return 'up_voted'
        return None

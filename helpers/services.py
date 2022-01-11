from django.db.models import Count, Exists, OuterRef
from rest_framework.permissions import IsAuthenticated

from accounts.queries import get_deleted_user


class VotesService:
    """
    Note: Vote manager related methods 'hard set' some
    annotated values to turn easy to return updated data to user.
    Is this the right solution? The other way would be to make
    another query and aggregate again."""
    def __init__(self, obj=None, queryset=None, user=None):
        self.obj = obj
        self.user = user
        if queryset is None:
            self.queryset = self.obj.__class__.objects.all()
        else:
            self.queryset = queryset

    def add_up_vote(self):
        if self.obj.is_down_voted:
            self.remove_down_vote()

        self.obj.up_votes.add(self.user)
        self.obj.up_votes_count += 1
        self.obj.is_up_voted = True
        return self.obj

    def remove_up_vote(self):
        self.obj.up_votes.remove(self.user)
        self.obj.up_votes_count -= 1
        self.obj.is_up_voted = False
        return self.obj

    def add_down_vote(self):
        if self.obj.is_up_voted:
            self.remove_up_vote()

        self.obj.down_votes.add(self.user)
        self.obj.down_votes_count += 1
        self.obj.is_down_voted = True
        return self.obj

    def remove_down_vote(self):
        self.obj.down_votes.remove(self.user)
        self.obj.down_votes_count -= 1
        self.obj.is_down_voted = False
        return self.obj

    def get_votes_count_query(self):
        return self.queryset.annotate(
            up_votes_count=Count('up_votes'),
            down_votes_count=Count('down_votes'),
        )

    def get_vote_acknowledged_query(self):
        queryset = self.get_votes_count_query()

        user_up_voted = self.queryset.filter(
            up_votes=self.user,
            id=OuterRef('id'),
        )
        user_down_voted = self.queryset.filter(
            down_votes=self.user,
            id=OuterRef('id'),
        )
        return queryset.annotate(
            is_up_voted=Exists(user_up_voted),
            is_down_voted=Exists(user_down_voted),
        )

    def get_query_by_request(self, request):
        if IsAuthenticated().has_permission(request, None):
            self.user = request.user
            return self.get_vote_acknowledged_query()
        return self.get_votes_count_query()


class DeleteService:
    def __init__(self, obj):
        self.obj = obj

    def update_author_to_deleted(self):
        self.obj.author = get_deleted_user()
        self.obj.save()

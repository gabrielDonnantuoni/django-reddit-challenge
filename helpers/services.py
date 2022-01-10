from django.db.models import Count, Exists, OuterRef


class VotesService:
    def __init__(self, obj=None, model=None, user=None):
        self.obj = obj
        self.model = model or self.obj.__class__
        self.user = user

    def add_up_vote(self):
        if self.obj.is_down_voted:
            self.remove_down_vote()

        self.obj.up_votes.add(self.user)

    def remove_up_vote(self):
        self.obj.up_votes.remove(self.user)

    def add_down_vote(self):
        if self.obj.is_up_voted:
            self.remove_up_vote()

        self.obj.down_votes.add(self.user)

    def remove_down_vote(self):
        self.obj.down_votes.remove(self.user)

    def get_votes_count_query(self):
        return self.model.objects.annotate(
            up_votes_count=Count('up_votes'),
            down_votes_count=Count('down_votes'),
        )

    def get_vote_acknowledged_query(self):
        qs = self.get_votes_count_query()

        user_up_voted = self.model.objects.filter(
            up_votes=self.user,
            id=OuterRef('id'),
        )
        user_down_voted = self.model.objects.filter(
            down_votes=self.user,
            id=OuterRef('id'),
        )
        return qs.annotate(
            is_up_voted=Exists(user_up_voted),
            is_down_voted=Exists(user_down_voted),
        )

class VotesModelMixin:
    @property
    def up_votes_count(self):
        return self.up_votes.all().count()

    @property
    def down_votes_count(self):
        return self.down_votes.all().count()

    def add_up_vote(self, user):
        if self.down_votes.filter(id=user.id).exists():
            self.remove_down_vote(user)

        self.up_votes.add(user)

    def remove_up_vote(self, user):
        self.up_votes.remove(user)

    def add_down_vote(self, user):
        if self.up_votes.filter(id=user.id).exists():
            self.remove_up_vote(user)

        self.down_votes.add(user)

    def remove_down_vote(self, user):
        self.down_votes.remove(user)

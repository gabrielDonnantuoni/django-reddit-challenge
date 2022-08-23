from typing_extensions import Literal
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from helpers.permissions import IsOwnerOrReadOnly
from helpers.services import VotesService


class VotesViewSetMixin:
    def get_permissions(self):
        self.permission_classes = [permissions.IsAuthenticatedOrReadOnly]
        if not self.action.endswith('vote'):
            self.permission_classes.append(IsOwnerOrReadOnly)
        return super().get_permissions()

    def vote(self, request, vote_type: Literal['up', 'down']):
        obj = self.get_object()
        is_voted = getattr(obj, f'is_{vote_type}_voted')

        service = VotesService(obj=obj, user=request.user)
        remove_vote = getattr(service, f'remove_{vote_type}_vote')
        add_vote = getattr(service, f'add_{vote_type}_vote')

        if is_voted:
            remove_vote()
        else:
            add_vote()

        updated_obj = self.get_object()
        serializer = self.get_serializer(updated_obj)
        return Response(serializer.data)

    @action(detail=True, methods=['patch'], url_path='up-vote')
    def up_vote(self, request, *args, **kwargs):
        return self.vote(request, vote_type='up')

    @action(detail=True, methods=['patch'], url_path='down-vote')
    def down_vote(self, request, *args, **kwargs):
        return self.vote(request, vote_type='down')

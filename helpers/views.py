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

    @action(detail=True, methods=['patch'], url_path='up-vote')
    def up_vote(self, request, *args, **kwargs):
        obj = self.get_object()
        service = VotesService(obj=obj, user=request.user)
        if obj.is_up_voted:
            obj = service.remove_up_vote()
        else:
            obj = service.add_up_vote()

        serializer = self.get_serializer(obj)
        return Response(serializer.data)

    @action(detail=True, methods=['patch'], url_path='down-vote')
    def down_vote(self, request, *args, **kwargs):
        obj = self.get_object()
        service = VotesService(obj=obj, user=request.user)
        if obj.is_down_voted:
            obj = service.remove_down_vote()
        else:
            obj = service.add_down_vote()

        serializer = self.get_serializer(obj)
        return Response(serializer.data)

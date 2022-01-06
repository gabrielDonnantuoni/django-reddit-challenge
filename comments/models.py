"""
Posts Models
"""
###
# Libraries
###
from django.db import models
from django.utils.translation import ugettext as _

from accounts.models import User
from accounts.queries import get_deleted_user
from posts.models import Post
from helpers.models import TimestampModel, VotesModel


###
# Models
###
class Comment(TimestampModel, VotesModel):
    content = models.TextField(_('content'))
    parent_comment = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        verbose_name=_('parent comment'),
        related_name=_('replies'),
        null=True,
    )
    author = models.ForeignKey(
        User,
        on_delete=models.SET(get_deleted_user),
        verbose_name=_('author'),
        related_name='comments',
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        verbose_name=_('post'),
        related_name='comments',
    )

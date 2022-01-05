"""
Posts Models
"""
###
# Libraries
###
from django.db import models
from django.utils.translation import ugettext as _

from accounts.models import User
from topics.models import Topic
from helpers.models import TimestampModel, VotesModel


###
# Models
###
class Tag(models.Model):
    name = models.CharField(_('name'), max_length=50)


class Post(TimestampModel, VotesModel):
    title = models.CharField(_('title'), max_length=150)
    content = models.TextField(_('content'))
    author = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        verbose_name=_('author'),
        related_name='posts',
    )
    topic = models.ForeignKey(
        Topic,
        on_delete=models.CASCADE,
        verbose_name=_('topic'),
        related_name='posts',
    )
    tags = models.ManyToManyField(
        Tag,
        verbose_name=_('tags'),
        related_name='posts',
    )

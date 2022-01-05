"""
Topics Models
"""
###
# Libraries
###
from django.db import models
from django.utils.translation import ugettext as _

from accounts.models import User
from helpers.models import TimestampModel


###
# Models
###
class Topic(TimestampModel):
    slug = models.SlugField(_('slug'), max_length=100, unique=True)
    title = models.CharField(_('title'), max_length=150)
    description = models.CharField(_('description'), max_length=255)
    author = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        verbose_name=_('author'),
        related_name='topics',
    )

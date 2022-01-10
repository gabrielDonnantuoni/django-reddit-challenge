"""
Model helper
"""
###
# Libraries
###
from django.db import models
from django.utils.translation import ugettext as _


###
# Helpers
###
class TimestampModel(models.Model):
    '''
        Extend this model if you wish to have automatically updated
        created_at and updated_at fields.
    '''

    class Meta:
        abstract = True

    created_at = models.DateTimeField(
        _('created at'),
        null=False,
        blank=True,
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        _('updated at'),
        null=False,
        blank=True,
        auto_now=True,
    )


class VotesModel(models.Model):
    class Meta:
        abstract = True

    up_votes = models.ManyToManyField(
        'accounts.User',
        related_name='%(class)s_up_votes',
        verbose_name=_('up vote'),
    )
    down_votes = models.ManyToManyField(
        'accounts.User',
        related_name='%(class)s_down_votes',
        verbose_name=_('up vote'),
    )

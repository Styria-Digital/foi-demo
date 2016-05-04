# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


@python_2_unicode_compatible
class Presentation(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_('User'))
    title = models.CharField(verbose_name=_('Title'), max_length=200)
    content = models.TextField(verbose_name=_('Content'))
    start_datetime = models.DateTimeField(verbose_name=_('Start time'))

    class Meta:
        verbose_name = _('Presentation')
        verbose_name_plural = _('Presentations')

    def __str__(self):
        return self.title

    def get_url(self):
        return reverse('presentations:presentation_detail', kwargs={'pk': self.id})

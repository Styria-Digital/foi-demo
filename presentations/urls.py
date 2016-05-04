# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf.urls import url
from django.utils.translation import ugettext_lazy as _

from presentations.views import HomeView, PresentationListView, PresentationDetailView


urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(_(r'^all$'), PresentationListView.as_view(), name='all_presentations'),
    url(r'^(?P<pk>[0-9]+)/$', PresentationDetailView.as_view(), name='presentation_detail'),
]

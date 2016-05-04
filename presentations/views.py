# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import TemplateView, ListView, DetailView

from presentations.models import Presentation


class HomeView(TemplateView):
    template_name = 'presentations/home.html'

class PresentationListView(ListView):
    model = Presentation
    template_name = 'presentations/presentation_list.html'


class PresentationDetailView(LoginRequiredMixin, DetailView):
    model = Presentation
    template_name = 'presentations/presentation_detail.html'

from urllib.parse import urlencode

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse
from django.views.generic import TemplateView

from utils.validators import match_email_regex


class Challenge(TemplateView):
    template_name = 'dashboard/C009/index.html'
    extra_context = {
        'challenge_title': "Facing too much request!!",
        'FLAG': settings.ARENA_FLAGS['C009'],
    }

    def get_context_data(self, **kwargs):
        kwargs['has_proper_agent'] = settings.ARENA['USER_AGENT'] in self.request.headers['User-Agent']
        return super().get_context_data(**kwargs)



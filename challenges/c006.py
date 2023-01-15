from urllib.parse import urlencode

from django.conf import settings
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import TemplateView

from utils.validators import match_email_regex


class Challenge(TemplateView):
    template_name = 'dashboard/C006/index.html'
    extra_context = {
        'challenge_title': "Let's Have Some Music!",
        'FLAG': settings.ARENA_FLAGS['C005'],
    }






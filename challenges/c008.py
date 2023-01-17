from urllib.parse import urlencode

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse
from django.views.generic import TemplateView

from utils.validators import match_email_regex


class Challenge(TemplateView):
    template_name = 'dashboard/C008/index.html'
    extra_context = {
        'challenge_title': "A fantesy Lock!",
        'FLAG': settings.ARENA_FLAGS['C008'],
    }


class PathFinder(TemplateView):
    template_name = 'dashboard/C008/autoindex.html'
    extra_context = {
        'challenge_title': "A fantesy Lock!",
        'FLAG': settings.ARENA_FLAGS['C008'],
    }


class Recovery(TemplateView):
    template_name = 'dashboard/C008/recovery.html'
    extra_context = {
        'challenge_title': "A fantesy Lock!",
        'FLAG': settings.ARENA_FLAGS['C008'],
    }

    def get(self, request, *args, **kwargs):
        string = render_to_string(self.template_name, context=self.extra_context)
        return HttpResponse(string, content_type='text/plain')


class PathException(TemplateView):
    template_name = 'dashboard/C008/autoindex-empty.html'
    extra_context = {
        'challenge_title': "A fantesy Lock!",
        'FLAG': settings.ARENA_FLAGS['C008'],
    }






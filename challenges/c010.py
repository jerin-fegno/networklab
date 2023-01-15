from urllib.parse import urlencode

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse
from django.views.generic import TemplateView

from utils.validators import match_email_regex


class Challenge(TemplateView):
    template_name = 'dashboard/C010/index.html'
    extra_context = {
        'challenge_title': "Session Login!",
        'FLAG': settings.ARENA_FLAGS['C010'],
    }

    def get(self, request, *args, **kwargs):
        cxt = self.extra_context.copy()
        cookie_key = 'IS_SUPERADMIN'
        if cookie_key in request.COOKIES:
            cxt['has_admin_session'] = int(request.COOKIES.get(cookie_key, '0')) > 0
        response = render(request, self.template_name, context=cxt)
        if cookie_key not in request.COOKIES:
            response.set_cookie(cookie_key, 0)
        return response



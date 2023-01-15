from urllib.parse import urlencode

from django.conf import settings
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import TemplateView

from utils.validators import match_email_regex


class Challenge(TemplateView):
    template_name = 'dashboard/C007/index.html'
    extra_context = {
        'challenge_title': "Memory Sensitive!!",
        'FLAG': settings.ARENA_FLAGS['C007'],
        'server_crash': False,
    }

    def post(self, request, *args, **kwargs):
        uname = request.POST['username']
        pwd = request.POST['password']
        otp = request.POST['otp']
        url = request.POST['address']

        if (len(uname) + len(pwd) + len(otp) + len(url)) > 2048:
            return render(request, self.template_name, context={**self.extra_context, 'server_crash': True})
        return render(request, self.template_name, context=self.extra_context)





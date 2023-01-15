from urllib.parse import urlencode

from django.conf import settings
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import TemplateView

from utils.validators import match_email_regex


class Challenge(TemplateView):
    template_name = 'dashboard/C001/index.html'
    extra_context = {
        'challenge_title': "Login To Admin Panel",
    }


class LabadminLogin(TemplateView):
    template_name = 'dashboard/C001/labadmin.html'
    extra_context = {
        'challenge_title': "Login To Admin Panel",
        'FLAG': settings.ARENA_FLAGS['C001']

    }

    def get(self, request, *args, **kwargs):
        return redirect(reverse('C001'))

    def post(self, request):
        clicked_button = 'sentmail' in request.POST
        same_as_assistant_email = request.POST['email'].strip() == settings.ARENA['ASSISTANT_EMAIL'].strip()
        valid_email = match_email_regex(request.POST['email'].strip())
        if not clicked_button:
            return redirect(reverse('C001') + "?email_sent=invalid_source")
        elif not valid_email:
            return redirect(reverse('C001') + "?email_sent=invalid_email&email_addr=" + request.POST['email'].strip())
        elif same_as_assistant_email:
            return redirect(reverse('C001') + "?email_sent=true")
        else:
            self.extra_context['mission_status'] = 'success'
        return render(request, self.template_name, context=self.get_context_data())




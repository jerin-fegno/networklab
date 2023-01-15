from urllib.parse import urlencode

from django.conf import settings
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import TemplateView

from utils.validators import match_email_regex


class Challenge(TemplateView):
    template_name = 'dashboard/C002/index.html'
    extra_context = {
        'challenge_title': "How Well you know String?!",
        'FLAG': settings.ARENA_FLAGS['C002'],
        "PATTERN": "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz",
    }

    def get_context_data(self, **kwargs):

        flag = settings.ARENA_FLAGS['C002']
        script = "password = '';"  # save the value to variable 'password'
        """
        Ultimately, planning to get something like this for flag = "C A R D I A B C 1 2 3 4" (without spaces)
        
        password = '';
		password = password + numletter.substring(12, 13);
		password = password + numletter.substring(10, 11);
		password = password + numletter.substring(27, 28);
		password = password + numletter.substring(13, 14);
		password = password + numletter.substring(18, 19);
		password = password + numletter.substring(10, 13);
		password = password + numletter.substring(1, 5);
        """
        _old_index = -1

        for letter in flag:
            index = self.extra_context['PATTERN'].index(letter)
            if _old_index + 1 == index and ',' in script:
                body, tail = script.rsplit(',', 1)
                script = body + ',' + tail.replace(str(_old_index + 1), str(index + 1))
            else:
                script += f"\n		password = password + numletter.substring({index}, {index + 1});"
            _old_index = index
        kwargs['SCRIPT'] = script
        return super().get_context_data(**kwargs)



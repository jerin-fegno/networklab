from urllib.parse import urlencode

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse
from django.views.generic import TemplateView

from utils.validators import match_email_regex


class Challenge(TemplateView):
    template_name = 'dashboard/C004/index.html'
    extra_context = {
        'challenge_title': "Find Password File!",
    }

    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        flag = settings.ARENA_FLAGS['C003']
        secret_container = flag
        salt = ''.join(format(i, '08b') for i in bytearray("CHALLENGE C003", 'utf-8'))
        flag_to_bin = ''.join(format(i, '08b') for i in bytearray(secret_container, 'utf-8'))
        intermediate_bin = int(flag_to_bin, 2) ^ int(salt, 2)
        kwargs['BINARY_01'] = bin(intermediate_bin)
        kwargs['BINARY_02'] = salt
        """
        HOW TO RECALCULATE ? 
        Go to Websites like https://xor.pw/ 
        
        Give First Input as binary (base 2)
        Give Second Input as binary (base 2)
        --------------------------------------------
        Calculate its XOR   as ASCII in (base 256) [OR  Get the XOR and convert it to string!]         
        
        """
        return kwargs


class Secret(TemplateView):
    template_name = 'dashboard/C004/secrets.txt'
    extra_context = {
        'FLAG': settings.ARENA_FLAGS['C004'],
    }

    def get(self, request, *args, **kwargs):
        string = render_to_string(self.template_name, context=self.extra_context)
        return HttpResponse(string, content_type="text/plain")


class RobotsTXT(TemplateView):
    template_name = 'dashboard/C004/robots.txt'

    def get(self, request, *args, **kwargs):
        string = render_to_string(self.template_name)
        return HttpResponse(string, content_type="text/plain")


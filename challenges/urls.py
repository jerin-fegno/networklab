from django.urls import path, include, re_path
from django.views.generic import TemplateView

from challenges import (
    c001, c002, c003, c004, c005, c006, c007, c008, c009, c010
)

from challenges.general import GeneralInstructions

urlpatterns = [
    path('', GeneralInstructions.as_view(), name='general-instructions'),
    path('challenge-break-login-fault/', include([
        path('', c001.Challenge.as_view(), name='C001'),
        path('labadmin-login/', c001.LabadminLogin.as_view(), name='C001_labadmin_login'),
    ])),
    path('challenge-tough-analyzer/', include([
        path('', c002.Challenge.as_view(), name='C002'),
    ])),
    path('challenge-encoder-specialist/', include([
        path('', c003.Challenge.as_view(), name='C003'),
    ])),
    path('challenge-1994/', include([
        path('', c004.Challenge.as_view(), name='C004'),
        path('robots.txt', c004.RobotsTXT.as_view(), name='C004-robots'),
        path('secret-silufhaniurfp9q248yrhpq9fawrhuqWP98DIOJCSZX.txt', c004.Secret.as_view(), name='C004-secret'),
    ])),
    path('challenge-what-happened/', include([
        path('', c005.Challenge.as_view(), name='C005'),
    ])),
    path('challenge-torture/', include([
        path('', c006.Challenge.as_view(), name='C006'),
    ])),
    path('challenge-crash-it/', include([
        path('', c007.Challenge.as_view(), name='C007'),
    ])),
    path('challenge-explorer/', include([
        path('', c008.Challenge.as_view(), name='C008'),
        path('newlabassistant/', c008.PathFinder.as_view(), name='C008-path-finder'),
        path('newlabassistant/recovery.html', c008.Recovery.as_view(), name='C008-recovery'),
        re_path('^(.*)', c008.PathException.as_view(), name='C008-PathException'),
        re_path('^(.*)/(.*)', c008.PathException.as_view(), name='C008-PathException'),
        re_path('^newlabassistant/(.*)', c008.PathException.as_view(), name='C008-PathException-inner'),
    ])),
    path('challenge-master-manipulator/', include([
        path('', c009.Challenge.as_view(), name='C009'),
    ])),
    path('challenge-fake-the-role/', include([
        path('', c010.Challenge.as_view(), name='C010'),
    ])),

]


# PARIS : morse     https://morsedecoder.com/


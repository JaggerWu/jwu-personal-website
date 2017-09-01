# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template.loader import get_template


# Create your views here.
def index(request):
    # I am a cow-worker!
    cow_worker = (
        ' ___________________         \n'
        '< I am a cow-worker >        \n'
        ' -------------------         \n'
        '       \   ^__^              \n'
        '        \  (oo)\_______      \n'
        '           (__)\       )\/\  \n'
        '               ||----w |     \n'
        '               ||     ||     \n'
    )
    if True:
        return HttpResponse('Welcome to JianWu personal site!')

    return HttpResponse(cow_worker)

def about_me(request):
    return HttpResponse('This is Jian Wu\'s personal site.')

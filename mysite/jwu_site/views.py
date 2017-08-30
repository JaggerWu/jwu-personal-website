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

    return render_to_response(
        'I-am-co-worker.html',
        {'cow_worker': cow_worker}
    )

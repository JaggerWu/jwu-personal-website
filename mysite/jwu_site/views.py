# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import get_template
from django.http import StreamingHttpResponse
import os


# Create your views here.
def index(request):
    return render(request, 'index.html')


def about_me(request):
    # There are some introduction for myself.
    return render(request, 'about_me.html')

local_path = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)


def download_cv(request):
    file_name = os.path.join(local_path, 'file/Weed_detection.pdf')
    with open(file_name) as f:
        c = f.read()

    response = HttpResponse(c)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format('JianWu_cv.pdf')

    return response

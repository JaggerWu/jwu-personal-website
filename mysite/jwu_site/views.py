# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import get_template
import os

local_path = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)


# Create your views here.
def index(request):
    return render(request, 'index.html')


def about_me(request):
    # There are some introduction for myself.
    return render(request, 'base.html')


def cv(request):
    # There are my CV
    return render(request, 'cv.html')


def download_cv(request):
    file_path = os.path.join(local_path, 'file/cv/resume.pdf')
    if os.path.exists(file_path):
        with open(file_path, 'rb') as f:
            response = HttpResponse(f.read())
            response['Content-Type'] = 'application/octet-stream'
            response['Content-Disposition'] = 'attachment;filename="{0}"'.format('JianWu_cv.pdf')

            return response
    raise Http404

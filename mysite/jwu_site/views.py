# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import get_template


# Create your views here.
def index(request):
    return render(request, 'base.html')


def about_me(request):
    # There are some introduction for myself.
    return render(request, 'about_me.html')

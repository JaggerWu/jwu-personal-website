# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import get_template


# Create your views here.
def about_me(request):
    # I am a cow-worker!
    cow_worker = (
        '''
         ___________________        <br/>
         < I am a cow-worker >      <br/>
         -------------------        <br/>
               \   ^__^             <br/>
                \  (oo)\_______     <br/>
                   (__)\       )\/\ <br/>
                       ||----w |    <br/>
                       ||     ||    <br/>
        '''
        
    )
    
    return render(
        request, 
        'I-am-co-worker.html',
        {'cow_worker': cow_worker}
    )

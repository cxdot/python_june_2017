# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    print "*"*50
    return render(request, 'the_wall_app/index.html')

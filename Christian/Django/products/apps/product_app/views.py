# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse
from .models import Products



# Create your views here.
def index(request):
    print "*"*50
    return render(request, 'product_app/index.html')

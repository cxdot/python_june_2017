# -*- coding: utf-8 -*-
# from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.


def index(request):
	print('Welcome to index')
	return render(request, 'portfolio_app/index.html')

def testimonials(request):
	print('these are testimonials')
	return render(request, 'portfolio_app/testimonials.html')

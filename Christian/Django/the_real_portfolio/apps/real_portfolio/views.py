# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

def index(request):
	print ('in the index')
	return render(request, 'real_portfolio/index.html')

def projects(request):
	print ('these are my projects')
	return render(request, 'real_portfolio/projects.html')

def aboutme(request):
	print ('check me out')
	return render(request, 'real_portfolio/aboutme.html')

def testimonials(request):
	print('peoples thoughts')
	return render(request, 'real_portfolio/testimonials.html')

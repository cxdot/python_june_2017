# -*- coding: utf-8 -*-
# from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
# from django.shortcuts import render, HttpResponse
def index(request):
	print ('hello world')
	# response = "Hello, I am your first request!"
	return render(request, "hello_world_app/index.html")


# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

# Create your views here.

def index(request):
	
	if 'submit_data' not in request.session:
		request.session['submit_data'] = 0

	return render(request, 'survey_form/index.html')

def process(request):
	
	if request.method == "POST":
		request.session['name'] = request.POST['yourname']
		request.session['location'] = request.POST['location']
		request.session['language'] = request.POST['language']
		request.session['comment'] = request.POST['comment']		
	
		request.session['submit_data'] += 1

		return redirect('/results')

	return redirect('/')

def results(request):
	count = {
		'x': request.session['submit_data']
	}
	
	return render(request, 'survey_form/results.html', count)

def reset(request):
	request.session['submit_data'] = 0

	return redirect('/')


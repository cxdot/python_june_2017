from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string


def index(request):
        try:
            request.session['attempt']
        except KeyError: 
            request.session['attempt'] = 0
        return render(request, 'random_word_app/index.html')

def generate(request):
    if request.method == "POST":
        unique_id = get_random_string(length=14)
    
        request.session['word'] = unique_id
        request.session['attempt'] += 1
        
        return redirect('/')

def reset(request):
    del request.session['word']
    del request.session['attempt']
    
    return redirect('/')
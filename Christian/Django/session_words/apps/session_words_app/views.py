from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from datetime import datetime 

def index(request):
    return render(request, 'session_words_app/index.html')

def create(request):
    if request.method == "POST":
        print request.POST
        if request.POST['word'] == "":
            messages.error(request, "Word cannot be blank")
            return redirect('/')
        if 'big' not in request.POST:
            font_size = 'normal_font'
        else:
            font_size = 'large_font'
        word = {
            'word' : request.POST['word'],
            'color' : request.POST['color'],
            'font_size' : font_size,
            'time' : datetime.now().strftime('%d %b %Y %I:%M %p'),
        }
        print word
        try:
            request.session['words']
        except KeyError:
            request.session['words'] = []

        temp_list = request.session['words']
        temp_list.append(word)
        request.session['words'] = temp_list

        
    return redirect('/')

def clear(request):
    request.session.flush()
    return redirect('/')
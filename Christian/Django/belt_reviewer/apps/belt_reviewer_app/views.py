# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from .models import User


def index(request):

    return render(request, 'belt_reviewer_app/index.html')

def register(request):
    print 'register me'

    if request.method == "POST":
        form_data = request.POST

        check = User.objects.register_validate(form_data)
        if check:
            print check
            return redirect('/')

        user = User.objects.create(
        name = form_data['name'],
        alias = form_data['alias'],
        email = form_data['email'],
        password = form_data['password'],
        )

        request.session['user_id'] = user.id

        return redirect('/books')

    return redirect('/')

def login(request):
        if request.method == "POST":
            form_data = request.POST

            check = User.objects.login(form_data)

            if type(check) == type(User()):
                request.session['user_id'] = check.id
                return redirect('/books')

            print check
        return redirect('/')

def books(request):

    if 'user_id' in request.session:
        user_id = request.session['user_id']

        context = {
        "current_user": User.objects.get(id=user_id)
        }

    return render(request, 'belt_reviewer_app/books.html', context)

def logout(request):

    request.session.pop('user_id')
    
    return redirect('/')

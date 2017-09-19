# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from .models import User


def index(request):

    return render(request, 'login_register_app/index.html')


def create(request):

    if request.method == "POST":
        form_data = request.POST

        check = User.objects.validate(form_data)

        if check:
            print check
            return redirect('/')

        user = User.objects.create(
        first_name = form_data['first_name'],
        last_name = form_data['last_name'],
        email = form_data['email'],
        password = form_data['password']
        )

        request.session['user_id'] = user.id

        return redirect('/success')

    return redirect('/')

def login(request):
    if request.method == "POST":
        form_data = request.POST

        check = User.objects.login(form_data)

        if type(check) == type(User()):

            return redirect('/success')
        print check
    return redirect('/')


def success(request):

    if 'user_id' in request.session:
        user_id = request.session['user_id']

        context = {
        "current_user": User.objects.get(id=user_id)
        }

        return render(request, 'login_register_app/success.html', context)

    return redirect('/')

def logout(request):
    request.session.pop('user_id')

    return redirect ('/')

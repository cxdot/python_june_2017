# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from .models import User


def index(request):
    print "*"*50
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

    return render (request, 'belt_reviewer_app/books.html')

def login(request):
    print 'in the login method'

    if request.method == "POST":
        form_data = request.POST
        check = User.objects.login_validate
        if check:
            print check
            return redirect('/')

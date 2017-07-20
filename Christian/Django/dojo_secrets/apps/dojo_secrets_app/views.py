# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .models import User, Secret
from django.db.models import Count

def error_messages(request, errors):
    for error in errors:
        messages.error(request, error)

def getCurrentUser(request):
    user_id = request.session['user_id']

    return User.objects.get(id=user_id)

def index(request):
    print 'In the index method'

    return render(request, 'dojo_secrets_app/index.html')

def secrets(request):
    print 'inside the secret method'

    if 'user_id' in request.session:
        user=User.objects.get(id=request.session['user_id'])
        secrets = Secret.objects.all()
        liked_secrets = []

        # for secret in user.likes.all():
        #     liked_secrets.append(secret.id)

        secrets = Secret.objects.all()

        context = {
            'user': user,
            'secrets': secrets,
            'liked_secrets': liked_secrets,
        }

        return render(request, 'dojo_secrets_app/secrets.html', context)

    return redirect(reverse('landing'))

def popular_secrets(request):
    print "Inside the popular_secrets method."

    popular = Secret.objects.annotate(num_likes=Count('liked_by')).order_by('-num_likes')

    context = {
        'secrets': popular
    }

    return render(request, 'dojo_secrets_app/popular_secrets.html', context)

def register(request):
    print 'In the register method'

    if request.method == 'POST':
        errors = User.objects.register_validation(request.POST)

        if not errors:
            user = User.objects.create_user(request.POST)

            request.session['user_id'] = user.id

            return redirect(reverse('secrets'))

        error_messages(request, errors)

    return redirect(reverse('landing'))

def login(request):
    print 'In the login method'

    if request.method == 'POST':
        errors = User.objects.login_validation(request.POST)

        if type(errors) == type(User()):
            user = errors
            request.session['user_id'] = user.id

            return redirect(reverse('secrets'))

        error_messages(request, errors)

    return redirect(reverse ('landing'))

def logout(request):
    print 'inside the logout method'

    request.session.pop('user_id')

    return redirect(reverse('landing'))

def create_secret(request):
    print "Inside the create_secret method."

    if request.method == 'POST':
        errors = Secret.objects.secret_validation(request.POST)

        if not errors:
            user = getCurrentUser(request)
            secret = Secret.objects.create_secret(user, request.POST)

    return redirect(reverse('secrets'))

def create_like(request, id):
    print "Inside the create_like method."

    if request.method == 'POST':
        user = getCurrentUser(request)
        secret = Secret.objects.get(id=id)

        user.likes.add(secret)

    return redirect(reverse('secrets'))

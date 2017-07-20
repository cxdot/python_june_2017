# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import bcrypt

class UserManager(models.Manager):
    def register_validation(self, form_data):
        errors = []

        if len(form_data['first_name']) == 0:
            errors.append('First name is required')
        if len(form_data['last_name']) == 0:
            errors.append('Last name is required.')
        if len(form_data['email']) == 0:
            errors.append('Email is required')
        if len(form_data['password']) == 0:
            errors.append('Password is required.')
        if len(form_data['confirm_password']) == 0:
            errors.append('Password confirmation is required.')

        email_record = User.objects.filter(email=form_data['email']).first()

        if email_record:
            errors.append['Email has already been register.']

        return errors

    def login_validation(self, form_data):
        errors = []

        if len(form_data['email']) == 0:
            errors.append('Email is required')
        if len(form_data['password']) == 0:
            errors.append('Password is required.')

        user = User.objects.filter(email=form_data['email']).first()

        if not user:

            errors.append('That email does not exist.')

        if user:
            password = str(form_data['password'])
            user_password = str(user.password)

            encryptedpw = bcrypt.hashpw(password, user_password)

            if encryptedpw == user_password:
                return user

            errors.append('Invalid password')

        return errors

    def create_user(self, form_data):
        password = str(form_data['password'])
        encryptedpw = bcrypt.hashpw(password, bcrypt.gensalt())

        user = User.objects.create(
            first_name = form_data['first_name'],
            last_name = form_data['last_name'],
            email = form_data['email'],
            password = encryptedpw
        )

        return user

class User(models.Model):
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    email = models.EmailField(max_length=55)
    password = models.CharField(max_length=55)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

class SecretManager(models.Manager):
    def secret_validation(self, form_data):
        errors = []

        #Check inputs have data
        if len(form_data['context']) == 0:
            errors.append('Secret content is required')

        return errors

    def create_secret(self, user, form_data):
        secret = Secret.objects.create(
            context = form_data['context'],
            user = user,
        )
        return secret

class Secret(models.Model):
    context = models.TextField()
    user = models.ForeignKey(User, related_name='secrets')
    liked_by = models.ManyToManyField(User, related_name='likes')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = SecretManager()

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class UserManager(models.Manager):
    def register_validate(self, form_data):
        errors = []
        if len(form_data['name']) == 0:
            errors.append("Name cannot be blank.")
        if len(form_data['name']) < 2:
            errors.append("Name cannot be less than 2 characters.")
        if len(form_data['alias']) == 0:
            errors.append("Alias cannot be blank.")
        if len(form_data['email']) == 0:
            errors.append("Email is required.")
        if len(form_data['password']) == 0:
            errors.append("Password is required.")
        if len(form_data['password']) in range(1, 7):
            errors.append("Password cannot be less than 8 characters.")
        if (form_data['confirm_password']) != form_data['password']:
            errors.append("Passwords do not match.")
        return errors

    def validate_login(self, form_data):
        errors = []

        if len(form_data['email']) == 0:
            errors.append('Email is required.')
        if len(form_data['password']) == 0:
            errors.append('Password is required')

        return errors

    def login(self, form_data):
        errors = []

        errors = self.validate_login(form_data)

        if not errors:
            user = User.objects.filter(email=form_data['email']).first()

            if user:
                if str(form_data['password']) == user.password:
                    return user

            errors.append('Invalid Account Information')

        return errors

class User(models.Model):
    name = models.CharField(max_length=50)
    alias = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

class Books(models.Model):
    title = models.CharField(max_length=55)
    author = models.CharField(max_length=55)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

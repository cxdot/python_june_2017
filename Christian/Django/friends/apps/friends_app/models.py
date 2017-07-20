from __future__ import unicode_literals
from django.db import models
import bcrypt

class UserManager(models.Manager):
    def register_validation(self, form_data):
        errors = []

        if len(form_data['name']) == 0:
            errors.append('Name is required')
        if len(form_data['alias']) == 0:
            errors.append('Alias is required.')
        if len(form_data['email']) == 0:
            errors.append('Email is required.')
        if len(form_data['password']) == 0:
            errors.append('Password is required.')
        if len(form_data['password']) in range (0,8):
            errors.append('Password must be at least 8 characters.')
        if len(form_data['confirm_password']) == 0:
            errors.append('Password confirmation is required.')
        if form_data['confirm_password'] != form_data['password']:
            errors.append('Passwords do not match.')
        if len(form_data['dob']) == 0:
            errors.append('Must enter Date of Birth.')


        email_record = User.objects.filter(email=form_data['email']).first()

        if email_record:
            errors.append('Email has already been register.')

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
            name = form_data['name'],
            email = form_data['email'],
            password = encryptedpw,
            alias = form_data['alias'],
            dob = form_data['dob']
        )

        return user

class User(models.Model):
    name = models.CharField(max_length=55)
    alias = models.CharField(max_length=55)
    email = models.EmailField(max_length=55)
    password = models.CharField(max_length=55)
    dob = models.DateField(null=True)
    friends = models.ManyToManyField('self', related_name='friended_by')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

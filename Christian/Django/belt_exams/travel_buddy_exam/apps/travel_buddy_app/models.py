# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import bcrypt

class UserManager(models.Manager):
    def register_validation(self, form_data):
        errors = []

        if len(form_data['name']) == 0:
            errors.append('Name is required')
        if len(form_data['name']) < 3:
            errors.append('Name must be at least 3 characters')
        if len(form_data['username']) == 0:
            errors.append('Username is required.')
        if len(form_data['username']) < 3:
            errors.append('Username must be at least 3 characters')
        if len(form_data['password']) == 0:
            errors.append('Password is required.')
        if len(form_data['password']) in range (1,7):
            errors.append('Password must be at least 8 characters.')
        if len(form_data['confirm_password']) == 0:
            errors.append('Password confirmation is required.')
        if form_data['confirm_password'] != form_data['password']:
            errors.append('Passwords do not match.')


        user_record = User.objects.filter(username=form_data['username']).first()

        if user_record:
            errors.append('Username has already been register.')

        return errors

    def login_validation(self, form_data):
        errors = []

        if len(form_data['username']) == 0:
            errors.append('Username is required')
        if len(form_data['password']) == 0:
            errors.append('Password is required.')

        user = User.objects.filter(username=form_data['username']).first()

        if not user:

            errors.append('That username does not exist.')

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
            username = form_data['username'],
            password = encryptedpw
        )

        return user

class User(models.Model):
    name = models.CharField(max_length=55)
    username = models.CharField(max_length=55)
    password = models.CharField(max_length=55)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     string_output = "id: {} name: {} username: {} password: {}"
    #
    #     return string_output.format(
    #         self.id,
    #         self.name,
    #         self.username,
    #         self.password,
    #     )
    objects = UserManager()

class TripManager(models.Manager):
    def trip_validate(self, form_data):
        print 'trip validate'
        errors = []

        if len(form_data['destination']) == 0:
            errors.append('Must have a destination.')
        if len(form_data['desc']) == 0:
            errors.append('Must have a description.')

        return errors

    def create_trip(self, form_data, user):
        trip = Trip.objects.create(
            destination = form_data['destination'],
            plan = form_data['desc'],
            start_date = form_data['start_date'],
            end_date = form_data['end_date'],
            user = user
            )

        return trip

class Trip(models.Model):
    destination = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    plan = models.TextField()
    user = models.ForeignKey(User, related_name='trips')
    # users = models.ManyToManyField(User, related_name='joined_trips')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    objects = TripManager()

class JoinedTripsManager(models.Manager):
    def join_trip(self, user, trip):
        relation_exists = JoinedTrips.objects.filter(user=user, trip=trip).first()

        if not relation_exists:
            JoinedTrips.objects.create(
                user=user,
                trip=trip,
            )

class JoinedTrips(models.Model):
    user = models.ForeignKey(User, related_name="joined_trips")
    trip = models.ForeignKey(Trip, related_name="users_joined")

    objects = JoinedTripsManager()

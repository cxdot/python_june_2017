from __future__ import unicode_literals
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .models import *

def error_messages(request, errors):
    for error in errors:
        messages.error(request, error)

def getCurrentUser(request):
    user_id = request.session['user_id']

    return User.objects.get(id=user_id)

def index(request):
    print 'in the index'
    if 'user_id' in request.session:
        return redirect(reverse('travels'))

    return render(request, 'travel_buddy_app/index.html')

def travel_info(request):
    print 'inside the travel info'

    if 'user_id' in request.session:
        user = getCurrentUser(request)
        user_trips = JoinedTrips.objects.filter(user=user)

        joined_trip_ids = []
        for joined_trip in user_trips:
            joined_trip_ids.append(joined_trip.trip.id)

        print joined_trip_ids

        other_trips = Trip.objects.exclude(id__in=joined_trip_ids)

        context = {
            'user': user,
            'user_trips': user_trips,
            'other_trips': other_trips,
        }

        return render(request, 'travel_buddy_app/travels.html', context)

    return redirect(reverse('landing'))

def add_trip(request):
    print 'adding trip'
    if request.method == 'POST':
        errors = Trip.objects.trip_validate(request.POST)

        if not errors:
            user = getCurrentUser(request)
            trip = Trip.objects.create_trip(request.POST, user)
            JoinedTrips.objects.join_trip(user, trip)

            return redirect('travels')
        context = {
            'errors': errors
            }
        return render(request, 'travel_buddy_app/add_trip.html', context)

def trip(request):

    return render(request, 'travel_buddy_app/add_trip.html')

def join_trip(request, id):
    user = getCurrentUser(request)
    trip = Trip.objects.filter(id=id).first()

    JoinedTrips.objects.join_trip(user, trip)

    return redirect(reverse('travels'))

def destination(request, id):
    print 'destination'
    user = getCurrentUser(request)
    trip = Trip.objects.get(id=id)

    joined_users = trip.users_joined.all()

    print 'users', joined_users

    context = {
        'user': user,
        'trip': trip,
        'joined_users': joined_users,
    }

    return render(request, 'travel_buddy_app/destination.html', context)

def register(request):
    print 'In the register method'

    if request.method == 'POST':
        errors = User.objects.register_validation(request.POST)

        if not errors:
            user = User.objects.create_user(request.POST)

            request.session['user_id'] = user.id

            return redirect(reverse('travels'))

        error_messages(request, errors)

    return redirect(reverse('landing'))

def login(request):
    print 'In the login method'

    if request.method == 'POST':
        varuser = User.objects.login_validation(request.POST)
        # print '50*+362+953+9523+952396',errors
        if type(varuser) == type([0,0]):
            error_messages(request, varuser)
            print 'asdffdsf', type(varuser)
            return redirect(reverse ('landing'))
        else:
            request.session['user_id'] = varuser.id
            return redirect(reverse('travels'))
    return redirect(reverse ('landing'))

def logout(request):
    print 'inside the logout method'

    request.session.pop('user_id')

    return redirect(reverse('landing'))

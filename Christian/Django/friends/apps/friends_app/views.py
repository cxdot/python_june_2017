from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .models import *

# Create your views here.
def error_messages(request, errors):
    for error in errors:
        messages.error(request, error)

def index(request):
    print "*"*50
    if 'user_id' in request.session:
        return redirect(reverse('friends'))

    return render(request, 'friends_app/index.html')

def friends(request):

    if 'user_id' in request.session:
        user_id = request.session['user_id']
        user = User.objects.get(id=user_id)
        users = User.objects.exclude(id=user.id)

        friends = user.friends.all()
        exclude_ids = list(friends.values_list(flat=True))
        exclude_ids.append(user.id)
        users = User.objects.exclude(id__in=exclude_ids)

        context = {
        "current_user": user,
        'users': users,
        'friends': friends,
        }

    return render(request, 'friends_app/friends.html', context)

def add_friend(request, id):
    if request.method == 'POST':
        current_user = User.objects.get(id=request.session['user_id'])
        friend_user = User.objects.get(id=id)

        current_user.friends.add(friend_user)

    return redirect(reverse('friends'))

def remove_friend(request, id):
    # if request.method == 'POST':
    current_user = User.objects.get(id=request.session['user_id'])
    user = User.objects.get(id=id)

    current_user.friends.remove(user)

    return redirect(reverse('friends'))

def user_profile(request, id):
    user = User.objects.get(id=id)
    context = {
        'user': user,
    }
    return render(request, 'friends_app/user.html', context)

def register(request):
    print 'In the register method'

    if request.method == 'POST':
        errors = User.objects.register_validation(request.POST)

        if not errors:
            user = User.objects.create_user(request.POST)

            request.session['user_id'] = user.id

            return redirect(reverse('friends'))

        error_messages(request, errors)

    return redirect(reverse('landing'))

def login(request):
    print 'In the login method'

    if request.method == 'POST':
        user = User.objects.login_validation(request.POST)

        if type(user) == type([0,0]):
            error_messages(request, user)
            return redirect(reverse ('landing'))
        else:
            request.session['user_id'] = user.id
            return redirect(reverse('friends'))
    return redirect(reverse ('landing'))

def logout(request):
    print 'inside the logout method'

    request.session.pop('user_id')

    return redirect(reverse('landing'))

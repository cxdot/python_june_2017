# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from .models import Courses

# Create your views here.
def index(request):
    context = {
    "courses": Courses.objects.all()
    }
    return render(request, 'courses_app/index.html', context)

def process(request):
    Courses.objects.create(course_name=request.POST["name"], description=request.POST["description"])

    return redirect('/')

def damage(request, id):
    context = {
        "course": Courses.objects.get(id=id)
    }
    return render(request, 'courses_app/destroy.html', context)

def delete(request, id):
    context = {
        "remove": Courses.objects.get(id=id).delete()
    }
    return redirect('/', context)

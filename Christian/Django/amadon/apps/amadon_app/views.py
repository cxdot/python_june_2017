from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from products import items

def index(request):
    context = {
        "items" : items
    }
    return render(request, 'amadon_app/index.html', context)

def purchase(request, item_id):
    for item in items:
        if item['id'] == int(item_id):
            amount_charged = item['price'] * int(request.POST['quantity'])

    # handle exceptions for session keys if they do not yet exist
    try:
        request.session['total_charged']
    except KeyError:
        request.session['total_charged'] = 0

    try:
        request.session['total_items']
    except KeyError:
        request.session['total_items'] = 0        

    request.session['total_charged'] += amount_charged
    request.session['total_items'] += int(request.POST['quantity'])
    request.session['last_transaction'] = amount_charged
    return redirect('/checkout')

def checkout(request):
    return render(request, 'amadon_app/checkout.html')
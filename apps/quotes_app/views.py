# -*- coding: utf-8 -*-
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from ..logreg_app.models import User
from .models import Quote

def display(request):
    all_quotes = Quote.objects.all()
    all_favorites = User.objects.get(id=request.session['id']).faves.all()
    
    aq = set(all_quotes)
    af = set(all_favorites)

    aq -= af

    context = {
        'quotes' : Quote.objects.all(),
        'fave' : User.objects.get(id=request.session['id']).faves.all(),
        'no_fave' : aq
    }
    return render(request, 'quotes_app/display.html', context)

def create(request):
    errors = Quote.objects.quote_validation(request.POST)
    if len(errors):
        for tag, error in errors.iteritems(): 
            messages.error(request, error, extra_tags=tag)
        return redirect('/quotes/')
    else:
        user = User.objects.get(id = request.session['id'])
        Quote.objects.create(
        author = request.POST['author'],
        message = request.POST['message'],
        user = user)
        # quote_id = request.session['id']
        return redirect ('/quotes/')

def addfave(request, quoteid):
    Quote.objects.addfavorites(request.session['id'], quoteid)
    return redirect ('/quotes/')

def removefave(request, quoteid):
    Quote.objects.removefavorites(request.session['id'], quoteid)
    return redirect ('/quotes/')

def user(request, userid):
    context = {
        'oneuser' : User.objects.get(id=userid)
    }
    return render(request, 'quotes_app/user.html', context)

def clear(request):
    request.session.flush()
    return redirect('/')
# Create your views here.

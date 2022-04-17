from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
# from .models import related models
# from .restapis import related methods
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from datetime import datetime
import logging
import json

#from server import djangoapp

# Get an instance of a logger
logger = logging.getLogger(__name__)


# Create your views here.
def get_staticDjangoTemplate(request):
    context = {}
    if request.method == "GET":
        return render(request, 'djangoapp/staticDjango.html', context)

# Create an `about` view to render a static about page
def about(request):
    context = {}
    if request.method == "GET":
        return render(request, 'djangoapp/about.html', context)    


# Create a `contact` view to return a static contact page
def contact(request):
    context = {}
    if request.method == "GET":
        return render(request, 'djangoapp/contact.html', context)


# Create a `login_request` view to handle sign in request
def login_request(request):
    context = {}
    if request.method == "POST":
        _username = request.POST['username']
        _password = request.POST['psw']
        _user = authenticate(username=_username, password=_password)
        if _user is not None:
            login(request, user=_user)
            logger.debug("{} logueado con exito".format(_username))
            return redirect('djangoapp:index')
        else:
            logger.debug("el usuario'{}' no existe".format(_username))
            context['message'] = "usuario o contraseña incorrectos"
    else:
        logger.debug("A non post request was sended")
    return render(request, 'djangoapp/login.html', context)


# Create a `logout_request` view to handle sign out request
def logout_request(request):
    logout(request=request)
    return redirect('djangoapp:index')

# Create a `registration_request` view to handle sign up request
def registration_request(request):
    context = {}
    if request.method == 'POST':
        #Check if user exists
        _username = request.POST['username']
        _password = request.POST['psw']
        user_exist = False
        try:
            User.objects.get(username=_username)
            user_exist = True
        except:
            #no encontro el usuario
            logger.debug("fijate que el usuario {} no existe".format(_username))
        if not user_exist:
            new_user = User.objects.create(username=_username, password=_password)
            login(request=request, user=new_user)
            return redirect('djangoapp:index')
        else:
             context['message'] = "User already exists."    
    return render(request, 'djangoapp/registration.html', context)


# Update the `get_dealerships` view to render the index page with a list of dealerships
def get_dealerships(request):
    context = {}
    if request.method == "GET":
        return render(request, 'djangoapp/index.html', context)


# Create a `get_dealer_details` view to render the reviews of a dealer
# def get_dealer_details(request, dealer_id):
# ...

# Create a `add_review` view to submit a review
# def add_review(request, dealer_id):
# ...


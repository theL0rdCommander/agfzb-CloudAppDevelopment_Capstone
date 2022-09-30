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

from djangoapp.models import CarModel, DealerReview

from .restapis import get_dealers_from_cf, get_dealer_reviews_from_cf
#from server import djangoapp

# Get an instance of a logger
logger = logging.getLogger(__name__)


# Create your views here.
def get_staticDjangoTemplate(request):
    context = {}
    if request.method == "GET":
        return render(request, 'djangoapp/staticclDjango.html', context)


def index(request):
    return render(request,'djangoapp/index.html')

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
#def get_dealerships(request):
#    context = {}
#    if request.method == "GET":
#        return render(request, 'djangoapp/index.html', context)
#def get_dealerships(request):
    # context = {}
    # if request.method == "GET":
    #     url = "https://80e52559-bb9f-495b-8742-00bd31516ce8-bluemix.cloudantnosqldb.appdomain.cloud/dealerships"
    #     # Get dealers from the URL
    #     dealerships = get_dealers_from_cf(url)
    #     context['dealerships'] = dealerships
    #     render(request, 'djangoapp/index.html', context)


# Create a `get_dealer_details` view to render the reviews of a dealer
def get_dealer_details(request, dealer_id):
    return render(request,'djangoapp/index.html') #TO DELETE
#     render(request, 'djangoapp/dealer_details.html', context)
#     context = {}
#     dealer_reviews = get_dealer_reviews_from_cf(dealerId=dealer_id)
#     context['dealer_reviews'] = dealer_reviews
#     render(request, 'djangoapp/dealer_details.html', context)

# Create a `add_review` view to submit a review
def add_review(request, dealer_id):
    return render(request,'djangoapp/index.html') #TO DELETE
#     context = {}
#     if request.method == 'GET':
#         context['cars'] = CarModel.objects.get(dealer_id=dealer_id)
#         render(request, 'djangoapp/add_review.html', context)
#     elif request.method == 'POST':
#         # update the json_payload["review"] to standarized cloudant format 
#         content = request.POST['content']
#         check = request.POST['purchasecheck']
#         car = request.POST['car']
#         date = datetime.utcnow().isoformat( request.POST['purchasedate'])
        
#         #{{car.id}}>{{car.name}}-{{car.make.name}}-{{ car.year|date:"Y" }}
#         # TODO look after sentiment!!!
#         #review = DealerReview(dealer_id, request.user.name, check, content, date, car.make.name, car.model, car.year, "good",  ) 
#         redirect("djangoapp:dealer_details", dealer_id=dealer_id)

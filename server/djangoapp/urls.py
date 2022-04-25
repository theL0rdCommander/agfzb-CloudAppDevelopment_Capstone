from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'djangoapp'
urlpatterns = [

    # route is a string contains a URL pattern
    # view refers to the view function
    # name the URL
    path(route='', views=views.get_staticDjangoTemplate, name="index"),

    path(route='first_template',view=views.get_staticDjangoTemplate, name='staticDjango'),

    # path for about view
    path(route='about', view=views.about, name='about'),

    # path for contact us view
    path(route='contact', view=views.contact, name='contact'),

    # path for registration
    path('registration/', views.registration_request, name='registration'),

    # path for login
    path('login/', views.login_request, name='login_request'),

    # path for logout
    path('logout/', views.logout_request, name='logout_request'),

    # path for dealer reviews view
    path('/api/dealership', views.get_dealer_review, name='dealer_reviews'),
    
    # path for add a review view
    path('/api/review', views.add_review, name='add_review'),

    # (mine) path for get the dealerships (INDEX)
    path(route='/api/review?dealerId=""', view=views.get_dealerships, name='index')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

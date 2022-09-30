from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'djangoapp'
urlpatterns = [

    # route is a string contains a URL pattern
    # view refers to the view function
    # name the URL
    #path(route='', view=views.index, name="index"),
    path(route='index.html',view=views.get_staticDjangoTemplate, name='staticDjango'),
    path(route='',view=views.index, name='index'),

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

    
    ################    Dynamic views   ###############
    # path for dealerships
#    path(route='', view=views.get_dealerships, name='index'),

    # path for dealer reviews view
    path(route='dealer/<int:dealer_id>/', view=views.get_dealer_details, name='dealer_details'),

    # path for add a review view
    path(route='dealer/<int:dealer_id>/', view=views.add_review, name='add_review'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


'''

    # path for dealer reviews view TODO make some tracking of this and assume is ok
    path('api/dealership', views.get_dealer_details, name='dealer_reviews'),
    
    # path for add a review view
    path('api/review', views.add_review, name='add_review'),

    # get dealer details paths
    path('dealer/<int:dealer_id>/', views.get_dealer_details, name='dealer_details'),

    # (mine) path for get the dealerships (INDEX)
    path(route='api/review?dealerId="<int:dealer_id>', view=views.get_dealerships, name='index')

'''
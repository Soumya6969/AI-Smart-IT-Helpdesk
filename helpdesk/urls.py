from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),

    path('about/', views.about, name='about'),

    path('contact/', views.contact, name='contact'),

    path(
    'register/',
    views.register,
    name='register'
    ),
    path(
        'login/',
        views.login_user,
        name='login'
    ),

    path(
        'dashboard/',
        views.dashboard,
        name='dashboard'
    ),

    path(
        'logout/',
        views.logout_user,
        name='logout'
    ),

]
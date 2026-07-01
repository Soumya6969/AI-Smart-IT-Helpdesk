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
        'raise_ticket/',
        views.raise_ticket,
        name='raise_ticket'
    ),
    path(
    'my-tickets/',
    views.my_tickets,
    name='my_tickets'
    ),
    path(
    'ticket/<int:ticket_id>/',
    views.ticket_detail,
    name='ticket_detail'
    ),
    path(
    'ticket/<int:ticket_id>/edit/',
    views.edit_ticket,
    name='edit_ticket'
   ),
   path(
    'ticket/<int:ticket_id>/close/',
    views.close_ticket,
    name='close_ticket'
    ),
    path(
    'admin-dashboard/',
    views.admin_dashboard,
    name='admin_dashboard'
   ),
   path(
    'admin-ticket/<int:ticket_id>/',
    views.admin_ticket_detail,
    name='admin_ticket_detail'
   ),
    path(
        'logout/',
        views.logout_user,
        name='logout'
    ),

]
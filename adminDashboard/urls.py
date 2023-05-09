from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.Dashboard,name='Dashboard'),
    path('Search/',views.Search,name='Search'),
    path('DigitalPersonalLoan/',views.Digitalploan,name='Digitalploan'),
    path('DigitalBusinessLoan/',views.Digitalbloan,name='Digitalbloan'),
    path('PremiumPersonalLoan/',views.Premiumploan, name='Premiumploan'),
    path('PremiumBusinessLoan/',views.Premiumbloan, name='Premiumbloan'),
    path('Customers/',views.Customers, name='Customers'),
    path('Createaccount/',views.Createaccount, name='Createaccount'),
    path('Cardoffer/',views.Cardoffer, name='Cardoffer'),
    path('Specialoffer/',views.Specialoffer, name='Specialoffer'),
    path('Bumperoffer/',views.Bumperoffer, name='Bumperoffer'),
    path('Staroffer/',views.Staroffer, name='Staroffer'),

]
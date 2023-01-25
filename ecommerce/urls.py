from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('shoes/', views.Shoes, name='shoes'),
    path('watches/', views.Watches, name='watches'),
    path('phones/', views.Phones, name='phones'),
    path('laptops/', views.Laptops, name='laptops'),
    path('health-care/', views.HealthCare, name='health-care'),
    path('hair-grooming/', views.HairGrooming, name='hair-grooming'),
    path('cosmetics/', views.Cosmetics, name='cosmetics'),
    path('clothes/', views.Clothes, name='clothes'),
    path('books/', views.Books, name='books'),
]

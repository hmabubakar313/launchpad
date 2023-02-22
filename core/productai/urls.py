from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('description/', views.description, name='description'),
    path('product/', views.product, name='product'),
    path('login/', views.login, name='login'),
    path('login_page/', views.login_page, name='login_page'),
    path('signup/', views.signup, name='signup'),
    path('signup_page/', views.signup_page, name='signup_page'),
]
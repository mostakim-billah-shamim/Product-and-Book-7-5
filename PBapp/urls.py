from django.urls import path
from .views import *

urlpatterns = [
    path('', DashboardPage, name='dashboard'),

    path('register/', RegisterPage, name='register'),
    path('login/', LoginPage, name='login'),
    path('logout/', LogoutPage, name='logout'),


    path('product/', ProductPage, name='product'),
    path('editproduct/<str:id>/', ProductPage, name='editproduct'),
    path('delproduct/<str:id>/', ProductDeletePage, name='delproduct'),


    path('book/', BookPage, name='book'),
    path('editbook/<str:id>/', BookPage, name='editbook'),
    path('delbook/<str:id>/', BookDeletePage, name='delbook'),
    
]
from django.urls import path

from . import views 

urlpatterns  = [
    path('', views.home, name='home'), # for the homepage call the function called name="home"
    path('add', views.add, name='add')
]
from django.urls import path

from . import views 

# App URLs
urlpatterns  = [
    path('', views.index, name='index') # for the homepage call the function called name="index"
]
"""pizzeria URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from . import views

app_name = 'pizzas'

urlpatterns = [
    #first argument is an empty string which matches the base url
    #the second argument specifies the function name to call in views.py
    #third argumen provides the name 'index' for this URL pattern to refer to later
    path('',views.index, name='index'),
    path('pizzas', view.pizzas, name='pizzas'),
]
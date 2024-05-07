from . import views
from django.urls import path, include
urlpatterns =[
 path('form', views.get_name, name='form')
]
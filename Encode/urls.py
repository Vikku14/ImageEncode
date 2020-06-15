from django.urls import path
from . import views

urlpatterns = [
    path('', views.picture, name='picture')
]

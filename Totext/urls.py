from django.urls import path
from .views import ImageToText
urlpatterns = [
    path('', ImageToText, name='form')
]
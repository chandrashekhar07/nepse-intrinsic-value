from django.urls import path
from .views import getDetails
urlpatterns = [
    path('price/', getDetails)
]
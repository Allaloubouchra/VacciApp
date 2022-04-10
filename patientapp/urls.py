from django.urls import path
from centreapp.views import RegisterApi

urlpatterns = [
    path('registersoumia/', RegisterApi.as_view())
]
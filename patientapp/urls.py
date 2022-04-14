from django.urls import path
from patientapp.views import RegisterApi

urlpatterns = [
    path('register/', RegisterApi.as_view())
]

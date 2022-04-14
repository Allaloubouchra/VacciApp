from django.urls import path
<<<<<<< HEAD
from patientapp.views import RegisterApi

urlpatterns = [
    path('register/', RegisterApi.as_view())
=======
from centreapp.views import RegisterApi

urlpatterns = [
    path('registersoumia/', RegisterApi.as_view())
>>>>>>> 2db8e08b675beb61a63a38dc354036477a932829
]

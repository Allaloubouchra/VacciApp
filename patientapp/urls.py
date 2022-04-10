from django.urls import path
<<<<<<< HEAD
from patientapp.views import RegisterApi

urlpatterns = [
    path('register/', RegisterApi.as_view())

]
=======
from centreapp.views import RegisterApi

urlpatterns = [
    path('registersoumia/', RegisterApi.as_view())
]
>>>>>>> 0f84395cd689b6fe93dac6c2855f78b89c2667b5

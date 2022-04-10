from django.urls import path
<<<<<<< HEAD
from centreapp.views import LogInApi

urlpatterns = [
    path('login/', LogInApi.as_view()),

]
=======
from centreapp.views import LogInApi, RegisterApi

urlpatterns = [
    path('login/', LogInApi.as_view()),
    path('register/', RegisterApi.as_view())
]
>>>>>>> 0f84395cd689b6fe93dac6c2855f78b89c2667b5

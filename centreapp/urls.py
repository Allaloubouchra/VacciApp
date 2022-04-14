from django.urls import path
from centreapp.views import LogInApi, RegisterApi


urlpatterns = [
    path('login/', LogInApi.as_view()),
    path('register/', RegisterApi.as_view())
]

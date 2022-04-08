from django.urls import path

from centreapp.views import LogInApi

urlpatterns = [
    path('login/', LogInApi.as_view())
]
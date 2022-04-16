from django.urls import path

from centreapp.views import LogInApi, RegisterApi, SurveyViewSet

urlpatterns = [
    path('login/', LogInApi.as_view()),
    path('register/', RegisterApi.as_view()),
    path('survey/', SurveyViewSet.as_view()),
]

from django.urls import path, include
from rest_framework.routers import SimpleRouter

from centreapp.views import LogInApi, RegisterApi, SurveyViewSet

router = SimpleRouter()
router.register('survey', SurveyViewSet, )
urlpatterns = [
    path('login/', LogInApi.as_view()),
    path('register/', RegisterApi.as_view()),
    path('', include(router.urls)),

]

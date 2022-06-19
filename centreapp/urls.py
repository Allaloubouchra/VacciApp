from django.urls import path, include
from rest_framework.routers import SimpleRouter

from centreapp.views import LogInApi, SurveyViewSet, RegisterApi, CenterViewSet, VaccineViewSet, ListWilayaApi

router = SimpleRouter()

router.register('survey', SurveyViewSet, )
router.register('center', CenterViewSet, )
router.register('vaccine', VaccineViewSet, )

urlpatterns = [
    path('login/', LogInApi.as_view()),
    path('register/', RegisterApi.as_view(), ),
    path('wilayas/', ListWilayaApi.as_view(), ),
    path('', include(router.urls)),

]

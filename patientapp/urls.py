from django.urls import path, include
from rest_framework.routers import SimpleRouter

from patientapp.views import VaccinationAppointmentViewSet, AccountViewSet

router = SimpleRouter()
router.register('vaccination-appointment', VaccinationAppointmentViewSet, )
router.register('account', AccountViewSet, )
urlpatterns = [
    path('view-set/', include(router.urls)),

]
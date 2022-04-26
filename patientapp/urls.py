from django.urls import path, include
from rest_framework.routers import SimpleRouter

from patientapp.views import VaccinationAppointmentViewSet, AccountViewSet

router = SimpleRouter()
router.register('vaccination-appointment', VaccinationAppointmentViewSet, )

router.register('account', AccountViewSet, )


urlpatterns = [
    path('', include(router.urls)),

]

"""
GET website/vaccination-appointment/ => list
POST website/vaccination-appointment/ => create
GET website/vaccination-appointment/:id/ => retrieve
PUT/PATCH website/vaccination-appointment/:id/ => update
DELETE website/vaccination-appointment/:id/ => delete / destroy

GET website/vaccination-appointment/appointment-calendar/ => appointment_calendar
GET website/vaccination-appointment/appointment-calendar-V2/ => appointment_calendar_v2
DELETE website/vaccination-appointment/delete-multi/ => delete_ndeb
"""
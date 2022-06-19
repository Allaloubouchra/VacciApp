from django.contrib import admin

from patientapp.models import Account, VaccinationAppointment

admin.site.register(Account)
admin.site.register(VaccinationAppointment)

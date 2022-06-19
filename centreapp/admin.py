from django.contrib import admin

# Register your models here.
from centreapp.models import Doctor, Wilaya, City, Disease, Survey, VaccineCentre, WorkingHours, Vaccine, \
    VaccineAndCentre

admin.site.register(Doctor)
admin.site.register(Wilaya)
admin.site.register(City)
admin.site.register(Disease)
admin.site.register(Survey)
admin.site.register(VaccineCentre)
admin.site.register(WorkingHours)
admin.site.register(Vaccine)
admin.site.register(VaccineAndCentre)

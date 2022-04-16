from django.db import models
from centreapp import DayOfWeek
from patientapp.models import Account, VaccinationAppointment
from django.utils.translation import gettext_lazy as _


class Wilaya(models.Model):
    name = models.CharField(max_length=255, unique=True)
    matricule = models.PositiveIntegerField()


class City(models.Model):
    name = models.CharField(max_length=255)
    matriculate = models.PositiveIntegerField()
    wilaya = models.ForeignKey(Wilaya, on_delete=models.CASCADE, related_name="cities")


class Disease(models.Model):
    name = models.CharField(max_length=255, unique=True)


class Survey(models.Model):
    vaccination_appointment = models.OneToOneField(
        VaccinationAppointment,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    positive_covid = models.BooleanField(default=False)
    contamination = models.BooleanField(default=False)
    disease = models.ManyToManyField(Disease, blank=True)
    temperature = models.DecimalField(decimal_places=2, max_digits=5)
    heart_rate = models.PositiveIntegerField()
    respiratory_rate = models.PositiveIntegerField()
    blood_pressure = models.DecimalField(decimal_places=2, max_digits=5)
    oximetry = models.DecimalField(decimal_places=2, max_digits=5)


class VaccineCentre(models.Model):
    name = models.CharField(max_length=50)
    address = models.TextField(max_length=1000)
    num_phone = models.CharField(max_length=14)
    latitude = models.DecimalField(decimal_places=10, max_digits=20)
    longitude = models.DecimalField(decimal_places=10, max_digits=20)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='centres')


class WorkingHours(models.Model):
    centre = models.ForeignKey(VaccineCentre, on_delete=models.CASCADE)
    day_of_week = models.PositiveIntegerField(_("day of week"), choices=DayOfWeek.WEEKDAYS)
    from_hour = models.TimeField(_("from hour"), auto_now=False, auto_now_add=False, blank=True, null=True)
    to_hour = models.TimeField(_("to hour"), auto_now=False, auto_now_add=False, blank=True, null=True)
    from_hour_s = models.TimeField(_("from hour"), auto_now=False, auto_now_add=False, blank=True, null=True)
    to_hour_s = models.TimeField(_("to hour"), auto_now=False, auto_now_add=False, blank=True, null=True)

    class Meta:
        unique_together = ('centre', 'day_of_week',)
# available


class Doctor(models.Model):
    account = models.OneToOneField(
        Account,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    speciality = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    post = models.CharField(max_length=50)


class Vaccine(models.Model):
    name = models.CharField(max_length=50)
    time_between_dose = models.PositiveIntegerField()
    vaccine_centre = models.ManyToManyField("VaccineCentre", through='VaccineAndCentre')


class VaccineAndCentre(models.Model):
    centre = models.ForeignKey(VaccineCentre, on_delete=models.CASCADE, related_name='vaccines')
    vaccine = models.ForeignKey(Vaccine, on_delete=models.CASCADE, related_name='centres')
    available = models.BooleanField(default=True)

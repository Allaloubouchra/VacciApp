from django.db import models
from centreapp import DayOfWeek, Temperature, FreqCardiaque, FreqRespi, Tension, Saturation
from patientapp.models import Account, VaccinationAppointment
from django.utils.translation import gettext_lazy as _


class Wilaya(models.Model):
    name = models.CharField(max_length=255, unique=True)
    matricule = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=255)
    matriculate = models.PositiveIntegerField()
    wilaya = models.ForeignKey(Wilaya, on_delete=models.CASCADE, related_name="cities")

    def __str__(self):
        return self.name


class Disease(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Survey(models.Model):
    vaccination_appointment = models.OneToOneField(
        VaccinationAppointment,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    positive_covid = models.BooleanField(default=False)
    contamination = models.BooleanField(default=False)
    disease = models.ManyToManyField(Disease, blank=True)
    temperature = models.CharField(max_length=2, choices=Temperature.CHOICES, null=True, blank=True)
    heart_rate = models.CharField(max_length=2, choices=FreqCardiaque.CHOICES, null=True, blank=True)
    respiratory_rate = models.CharField(max_length=2, choices=FreqRespi.CHOICES, null=True, blank=True)
    blood_pressure = models.CharField(max_length=2, choices=Tension.CHOICES, null=True, blank=True)
    oximetry = models.CharField(max_length=2, choices=Saturation.CHOICES, null=True, blank=True)

    def __str__(self):
        return f'{self.pk}'


class VaccineCentre(models.Model):
    name = models.CharField(max_length=50)
    address = models.TextField(max_length=1000)
    num_phone = models.CharField(max_length=14)
    latitude = models.DecimalField(decimal_places=10, max_digits=20)
    longitude = models.DecimalField(decimal_places=10, max_digits=20)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='centres')

    def __str__(self):
        return self.name


class WorkingHours(models.Model):
    centre = models.ForeignKey(VaccineCentre, on_delete=models.CASCADE, related_name="working_hours")
    day_of_week = models.PositiveIntegerField(_("day of week"), choices=DayOfWeek.WEEKDAYS)
    from_hour = models.TimeField(_("from hour"), auto_now=False, auto_now_add=False, blank=True, null=True)
    to_hour = models.TimeField(_("to hour"), auto_now=False, auto_now_add=False, blank=True, null=True)
    from_hour_s = models.TimeField(_("from hour"), auto_now=False, auto_now_add=False, blank=True, null=True)
    to_hour_s = models.TimeField(_("to hour"), auto_now=False, auto_now_add=False, blank=True, null=True)

    def __str__(self):
        return self.centre.name + " " + self.get_day_of_week_display()

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

    def __str__(self):
        return self.account.user.get_full_name()


class Vaccine(models.Model):
    name = models.CharField(max_length=50)
    time_between_dose = models.PositiveIntegerField()
    vaccine_centre = models.ManyToManyField("VaccineCentre", through='VaccineAndCentre')

    def __str__(self):
        return self.name


class VaccineAndCentre(models.Model):
    centre = models.ForeignKey(VaccineCentre, on_delete=models.CASCADE, related_name='vaccines')
    vaccine = models.ForeignKey(Vaccine, on_delete=models.CASCADE, related_name='centres')
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.vaccine.name + " " + self.centre.name

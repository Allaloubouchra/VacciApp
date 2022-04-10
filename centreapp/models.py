from django.db import models
from patientapp.models import Account, VaccinationAppointment


class Staff(models.Model):
    account = models.OneToOneField(
        Account,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    vaccine_centre = models.ForeignKey("VaccineCenter", null=False, on_delete=models.CASCADE)


class Doctor(Staff):
    speciality = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    post = models.CharField(max_length=50)


class Receptionist(Staff):
    pass


class Survey(models.Model):
    vaccination_appointment = models.OneToOneField(
        VaccinationAppointment,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    positive_covid = models.CharField(max_length=50)
    contamination = models.CharField(max_length=50)
    disease = models.CharField(max_length=50)
    temperature = models.CharField(max_length=50)
    heart_rate = models.PositiveIntegerField(max_length=50)
    respiratory_rate = models.PositiveIntegerField(max_length=50)
    blood_pressure = models.CharField(max_length=50)
    oximetry = models.CharField(max_length=50)


class VaccineCentre(models.Model):

    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    num_phone = models.CharField(max_length=500)
    vaccination_appointment = models.ManyToManyField("patientapp.VaccinationAppointment")


class Vaccine(models.Model):
    name = models.CharField(max_length=50)
    time_between_dose = models.IntegerField()  # ajouter une methode
    vaccine_centre = models.ManyToManyField("VaccineCentre")

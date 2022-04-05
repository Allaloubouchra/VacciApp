from django.db import models
from patientapp.models import Account, VaccinationAppointment


class Staff(models.Model):
    account = models.OneToOneField(
        Account,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    vaccine_centre = models.ForeignKey("VaccineCentre", null=False, on_delete=models.CASCADE)


class Doctor(Staff):
    vaccination_appointment = models.ForeignKey("patientapp.VaccinationAppointment", null=False, on_delete=models.CASCADE)


class Receptionist(Staff):
    vaccination_appointment = models.ForeignKey("patientapp.VaccinationAppointment", null=False, on_delete=models.CASCADE)
    vaccine = models.ForeignKey("Vaccine", null=False,on_delete=models.CASCADE)


class Survey(models.Model):
    vaccination_appointment = models.OneToOneField(
        VaccinationAppointment,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    doctor = models.ForeignKey("Doctor", null=False, on_delete=models.CASCADE)


class VaccineCentre(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    num_phone = models.CharField(max_length=500)
    vaccination_appointment = models.ManyToManyField("patientapp.VaccinationAppointment")


class Vaccine(models.Model):
    name = models.CharField(max_length=50)
    time_between_dose = models.IntegerField()
    vaccination_appointment = models.ForeignKey("patientapp.VaccinationAppointment", null=False, on_delete=models.CASCADE)
    vaccine_centre = models.ManyToManyField("VaccineCentre")






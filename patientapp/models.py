from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    birthday = models.DateField()
    phone_num = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    MALE = 'Male'
    FEMALE = 'Female'
    GENDER_CHOICES = (
        ('MALE', 'Male'),
        ('FEMALE', 'Female'),
    )
    gender = models.CharField(choices=GENDER_CHOICES, max_length=30)

    @property
    def age(self):
        return timezone.now().year - self.birthday.year


class Patient(models.Model):
    account = models.OneToOneField(
        Account,
        on_delete=models.CASCADE,
        primary_key=True,
    )


class VaccinationAppointment(models.Model):
    date_appointment = models.DateField()
    time_appointment = models.TimeField()
    num_dose = models.IntegerField()
    arm = models.CharField(max_length=30)
    patient = models.ForeignKey("Patient", null=False, on_delete=models.CASCADE, related_name="appointments")
    doctor = models.ForeignKey("centreapp.Doctor", null=False, on_delete=models.CASCADE, )
    vaccine = models.ForeignKey("centreapp.Vaccine", null=False, on_delete=models.CASCADE)
    receptionist = models.ForeignKey("centreapp.Receptionist", null=False, on_delete=models.CASCADE)
    PENDING = 'Pending'
    CONFIRMED = 'confirmed'
    CANCELED = 'Canceled'
    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (CONFIRMED, 'confirmed'),
        (CANCELED, 'Canceled'),
    ]
    status = models.CharField(choices=STATUS_CHOICES, max_length=30)

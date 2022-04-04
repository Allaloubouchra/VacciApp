from django.db import models
from django.utils import timezone


class Account(models.Model):
    first_name = models.CharField(max_length=50, unique=True)
    last_name = models.CharField(max_length=50, unique=True)
    birthday = models.DateField()
    phone_num = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    gender = models.CharField(max_length=30)

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
    vaccine = models.ForeignKey("Vaccine", null=False)
    date_appointment = models.DateField()
    time_appointment = models.TimeField()
    PENDING = 'Pending'
    CONFIRMED = 'confirmed'
    CANCELED = 'Canceled'
    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (CONFIRMED, 'confirmed'),
        (CANCELED, 'Canceled'),
    ]
    num_dose = models.IntegerField()
    arm = models.CharField(max_length=30)




from datetime import datetime

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from patientapp import UserType, GenderType, AppointmentStatus, Arms


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    user_type = models.CharField(choices=UserType.USER_TYPE_CHOICES, max_length=1)
    birthday = models.DateField()
    phone_num = models.CharField(max_length=14)
    address = models.CharField(max_length=100)
    gender = models.CharField(choices=GenderType.GENDER_CHOICES, max_length=1)
    vaccine_centre = models.ForeignKey("centreapp.VaccineCentre", null=True, blank=True, on_delete=models.CASCADE)

    # validation : if user_type = patient  null= true vaccine_centre il n'existe pas else (user_type =staff)
    # vaccine_centre il existe  35:08
    @property
    def age(self):
        return timezone.now().year - self.birthday.year

    @property
    def is_patient(self):
        return self.user_type == UserType.PATIENT

    @property
    def is_doctor(self):
        return self.user_type == UserType.DOCTOR

    @property
    def is_receptionist(self):
        return self.user_type == UserType.RECEPTIONIST

    @property
    def is_doctor_or_is_receptionist(self):
        return self.is_receptionist or self.is_doctor

    @classmethod
    def get_patients_ids(cls):
        return Account.objects.filter(user_type=UserType.PATIENT).values_list('id', flat=True)

    @classmethod
    def get_doctors_ids(cls):
        return Account.objects.filter(user_type=UserType.DOCTOR).values_list('id', flat=True)

    @classmethod
    def get_receptionists_ids(cls):
        return Account.objects.filter(user_type=UserType.RECEPTIONIST).values_list('id', flat=True)


class VaccinationAppointment(models.Model):
    appointment_date = models.DateTimeField(verbose_name=_('Appointment Date'))
    num_dose = models.IntegerField()
    arm = models.CharField(max_length=1, choices=Arms.ARMS_CHOICES, null=True, blank=True)
    patient = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="p_appointments",
                                limit_choices_to={'id__in': Account.get_patients_ids})
    doctor = models.ForeignKey(Account, null=True, blank=True, on_delete=models.CASCADE, related_name="d_appointments",
                               limit_choices_to={'id__in': Account.get_doctors_ids})
    receptionist = models.ForeignKey(Account, null=True, blank=True, on_delete=models.CASCADE,
                                     related_name="confirmed_app",
                                     limit_choices_to={'id__in': Account.get_receptionists_ids})
    vaccine = models.ForeignKey("centreapp.Vaccine", null=False, on_delete=models.CASCADE)
    status = models.CharField(choices=AppointmentStatus.STATUS_CHOICES, max_length=2, default=AppointmentStatus.PENDING)
    centre = models.ForeignKey("centreapp.VaccineCentre", on_delete=models.CASCADE, related_name="appointments")

    def date_for_next_appointment(self):
        pass


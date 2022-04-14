from rest_framework import serializers
from centreapp.serializers import VaccineSerializer, VaccineCentreSerializer
from patientapp.models import *


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'user',
            'user_type',
            'get_user_type_display',
            'birthday',
            'phone_num',
            'address',
            'age',
            'gender',
            'vaccine_centre'
        )
        model = Account


class UserSerializer(serializers.ModelSerializer):
    account = AccountSerializer(required=False)

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
            'first_name',
            'last_name',
            'last_login',
            'is_staff',
            'is_superuser',
            'account',
        )


class VaccinationAppointmentSerializer(serializers.ModelSerializer):
    patient = AccountSerializer(read_only=True)
    doctor = AccountSerializer(read_only=True)
    receptionist = AccountSerializer(read_only=True)
    vaccine = VaccineSerializer(read_only=True)
    centre = VaccineCentreSerializer(read_only=True)

    class Meta:
        fields = (
            'id',
            'appointment_date',
            'num_dose',
            'arm',
            'get_arm_display',
            'patient',
            'patient_id',
            'doctor',
            'doctor_id',
            'receptionist',
            'receptionist_id',
            'vaccine',
            'vaccine_id',
            'status',
            'get_status_display',
            'centre',
            'centre_id',
        )
        model = VaccinationAppointment
        extra_kwargs = {
            "patient_id": {
                "write_only": True,
            },
            "doctor_id": {
                "write_only": True,
            },
            "receptionist_id": {
                "write_only": True,
            },
            "vaccine_id": {
                "write_only": True,
            },
            "centre_id": {
                "write_only": True,
            },
        }

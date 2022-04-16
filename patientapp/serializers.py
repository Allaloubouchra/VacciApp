from django.contrib.auth.models import User
from rest_framework import serializers
from patientapp.models import Account, VaccinationAppointment


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'user',  # user id et pas l'objet
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

    def get_fields(self):
        from centreapp.serializers import VaccineSerializer, VaccineCentreSerializer
        fields = super(VaccinationAppointmentSerializer, self).get_fields()
        fields['vaccine'] = VaccineSerializer(read_only=True)
        fields['centre'] = VaccineCentreSerializer(read_only=True)
        return fields

    class Meta:
        fields = (
            'id',
            'appointment_date',
            'num_dose',
            'arm',  # l or r
            'get_arm_display',  # left or right
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

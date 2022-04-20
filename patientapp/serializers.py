from django.contrib.auth.models import User
from django.utils import timezone
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

    def validate_appointment_date(self, data):
        if data < timezone.now():
            raise serializers.ValidationError("finish must occur after start")
        return data

    def validate(self, data):
        from centreapp.models import WorkingHours

        try:
            working_hour = WorkingHours.objects.get(centre_id=data['centre'],
                                                    day_of_week=data['appointment_date'].week_day())
            if not ((working_hour.from_hour <= data['appointment_date'].time() <= working_hour.to_hour) or
                    (working_hour.from_hour_s <= data['appointment_date'].time() <= working_hour.to_hour_s)):
                raise serializers.ValidationError("We are not available.")
        except Exception:
            raise serializers.ValidationError("the centre you selected is not available on that day of week.")
        return data

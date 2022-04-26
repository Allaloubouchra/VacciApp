from django.contrib.auth.models import User

from django.utils import timezone
from rest_framework import serializers
from patientapp.models import Account, VaccinationAppointment


class AccountSerializer(serializers.ModelSerializer):
    age = serializers.IntegerField()

    class Meta:
        fields = (
            # 'id',
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
        extra_kwargs = {'user': {'required': False}}

        model = Account


class UserSerializer(serializers.ModelSerializer):
    account = AccountSerializer(required=False)
    password = serializers.CharField(write_only=True)

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
            'password',
        )

    def create(self, validated_data):

        account_data = validated_data.pop('account', None)
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        if account_data is not None:
            account_data['user'] = user.id
            account_serializer = AccountSerializer(data=account_data)
            if account_serializer.is_valid(raise_exception=True):
                account_serializer.save()
        return user


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

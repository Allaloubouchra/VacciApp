from rest_framework import serializers
from patientapp.models import *


class AccountSerializer(serializers.ModelSerializer):
    # user one to one field
    age = serializers.Field()
    choices = serializers.ChoiceField(choices=Account.GENDER_CHOICES)

    class Meta:
        fields = ('birthday', 'phone_num', 'address', 'age', 'choices')
        model = Account


class PatientSerializer(serializers.ModelSerializer):
    birthday = serializers.DateField(source='Patient.account.birthday')
    phone_num = serializers.CharField(source='Patient.account.phone_num')
    address = serializers.CharField(source='Patient.account.address')
    choices = serializers.ChoiceField(choices=Account.GENDER_CHOICES)

    class Meta:
        fields = ('id', 'birthday', 'phone_num', 'address', 'choices')
        model = Patient


class VaccinationAppointmentSerializer(serializers.ModelSerializer):
    patient = serializers.RelatedField(source='patient', read_only=True)
    doctor = serializers.RelatedField(source='doctor', read_only=True)
    vaccine = serializers.RelatedField(source='vaccine', read_only=True)
    receptionist = serializers.RelatedField(source='receptionist', read_only=True)
    choices = serializers.ChoiceField(choices=VaccinationAppointment.STATUS_CHOICES)

    class Meta:
        fields = ('patient', 'doctor', 'vaccine', 'receptionist', 'date_appointment', 'time_appointment', 'choices',
                  'num_dose', 'arm')
        model = VaccinationAppointment


class UserSerializer(serializers.ModelSerializer):
    patient = PatientSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('patient', 'id', 'username', 'email', 'address')


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user
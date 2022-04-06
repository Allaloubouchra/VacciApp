from rest_framework import serializers
from patientapp.models import *


class AccountSerializer(serializers.ModelSerializer):
    age = serializers.Field()
    choices = serializers.ChoiceField(choices=Account.GENDER_CHOICES)

    class Meta:
        fields = ('first_name', 'last_name', 'birthday', 'phone_num', 'email', 'password', 'address', 'age', 'choices',
                  'MALE', 'FEMALE')
        model = Account


class PatientSerializer(serializers.ModelSerializer):
    vaccination_appointment_patient = serializers.RelatedField(source='vaccination_appointment', read_only=True)
    first_name = serializers.CharField(source='Patient.account.first_name')
    last_name = serializers.CharField(source='Patient.account.last_name')
    birthday = serializers.DateField(source='Patient.account.birthday')
    phone_num = serializers.CharField(source='Patient.account.phone_num')
    email = serializers.EmailField(source='Patient.account.email')
    password = serializers.CharField(source='Patient.account.password')
    address = serializers.CharField(source='Patient.account.address')
    choices = serializers.ChoiceField(choices=Account.GENDER_CHOICES)

    class Meta:
        fields = ('id', 'vaccination_appointment_patient', 'first_name', 'last_name', 'birthday', 'phone_num', 'email',
                  'password', 'address', 'choices')
        model = Patient


class VaccinationAppointmentSerializer(serializers.ModelSerializer):
    choices = serializers.ChoiceField(choices=VaccinationAppointment.STATUS_CHOICES)

    class Meta:
        fields = ('date_appointment', 'time_appointment', 'PENDING', 'CONFIRMED', 'CANCELED', 'choices', 'num_dose',
                  'arm')
        model = VaccinationAppointment







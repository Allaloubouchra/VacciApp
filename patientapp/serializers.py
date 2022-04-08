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

    first_name = serializers.CharField(source='Patient.account.first_name')
    last_name = serializers.CharField(source='Patient.account.last_name')
    birthday = serializers.DateField(source='Patient.account.birthday')
    phone_num = serializers.CharField(source='Patient.account.phone_num')
    email = serializers.EmailField(source='Patient.account.email')
    password = serializers.CharField(source='Patient.account.password')
    address = serializers.CharField(source='Patient.account.address')
    choices = serializers.ChoiceField(choices=Account.GENDER_CHOICES)

    class Meta:
        fields = ('id','first_name', 'last_name', 'birthday', 'phone_num', 'email',
                  'password', 'address', 'choices')
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







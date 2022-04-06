from rest_framework import serializers
from centreapp.models import *
from patientapp.models import Account, VaccinationAppointment
from patientapp.serializers import VaccinationAppointmentSerializer


class StaffSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source='Patient.account.first_name')
    last_name = serializers.CharField(source='Patient.account.last_name')
    birthday = serializers.DateField(source='Patient.account.birthday')
    phone_num = serializers.CharField(source='Patient.account.phone_num')
    email = serializers.EmailField(source='Patient.account.email')
    password = serializers.CharField(source='Patient.account.password')
    address = serializers.CharField(source='Patient.account.address')
    choices = serializers.ChoiceField(choices=Account.GENDER_CHOICES)
    vaccination_centre_staff = serializers.RelatedField(source='vaccine_centre', read_only=True)

    class Meta:
        fields = ('id', 'vaccination_appointment_staff', 'first_name', 'last_name', 'birthday', 'phone_num', 'email',
                  'password', 'address', 'choices')
        model = Staff


class DoctorSerializer(StaffSerializer):
    vaccination_appointment_doctor = serializers.RelatedField(source="vaccination_appointment", read_only=True)

    class Meta:
        fields = StaffSerializer.Meta.fields+("id", "vaccination_appointment_doctor",)
        # model = Staff


class ReceptionistSerializer(StaffSerializer):
    vaccination_appointment_receptionist = serializers.RelatedField(source="vaccination_appointment", read_only=True)
    vaccine_receptionist = serializers.RelatedField(source="vaccine", read_only=True)

    class Meta:
        fields = StaffSerializer.Meta.fields + ("id", "vaccination_appointment_receptionist", "vaccine_receptionist ",)
        # model = Staff


class SurveySerializer(serializers.ModelSerializer):
    date_appointment = serializers.DateField(source='vaccination_appointment.date_appointment')
    time_appointment = serializers.TimeField(source='vaccination_appointment.time_appointment')
    num_dose = serializers.IntegerField(source='vaccination_appointment.num_dose')
    arm = serializers.CharField(source='vaccination_appointment.arm')
    choices = serializers.ChoiceField(choices=VaccinationAppointment.STATUS_CHOICES)
    doctor_survey = serializers.RelatedField(source="doctor", read_only=True)

    class Meta:
        fields = ("id", "date_appointment", " time_appointment ", "num_dose", "arm ", "choices ", "doctor_survey")
        model = Survey


class VaccineCentreSerializer(serializers.ModelSerializer):
    vaccination_appointment = VaccinationAppointmentSerializer(read_only=True, many=True)

    class Meta:
        fields = ("id", "name", "address", "num_phone", "vaccination_appointment")
        model = VaccineCentre


class VaccineSerializer(serializers.ModelSerializer):
    vaccination_appointment_vaccine = serializers.RelatedField(source="vaccination_appointment", read_only=True)
    vaccine_centre = VaccineCentre(read_only=True, many=True)

    class Meta:
        fields = ("name", "time_between_dose", "num_phone", "vaccination_appointment_vaccine", "vaccine_centre",)
        model = Vaccine

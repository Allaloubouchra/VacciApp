from rest_framework import serializers
from centreapp.models import *


class StaffSerializer(serializers.ModelSerializer):
    vaccine_centre_staff = serializers.RelatedField(source="vaccine_centre", read_only=True)

    class Meta:
        fields = ("account", "vaccine_centre_staff",)
        model = Staff


class DoctorSerializer(serializers.ModelSerializer):
    vaccination_appointment_doctor = serializers.RelatedField(source="vaccination_appointment", read_only=True)

    class Meta:
        fields = ("vaccination_appointment_doctor",)
        model = Doctor


class ReceptionistSerializer(serializers.ModelSerializer):
    vaccination_appointment_receptionist = serializers.RelatedField(source="vaccination_appointment", read_only=True)
    vaccine_receptionist = serializers.RelatedField(source="vaccine", read_only=True)

    class Meta:
        fields = ("vaccination_appointment_receptionist", "vaccine",)
        model = Receptionist


class SurveySerializer(serializers.ModelSerializer):
    doctor_survey = serializers.RelatedField(source="doctor", read_only=True)

    class Meta:
        fields = ("doctor_survey", " vaccination_appointment")

class VaccineCentreSerializer(serializers.ModelSerializer):
            class Meta:
                fields = ("name", "address", "num_phone", "vaccination_appointment ")


class VaccineSerializer(serializers.ModelSerializer):
    vaccination_appointment_vaccine = serializers.RelatedField(source="vaccination_appointment", read_only=True)
    class Meta:
        fields = ("name", "time_between_dose", "num_phone", " vaccination_appointment_vaccine ")




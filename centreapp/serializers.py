from rest_framework import serializers

from centreapp.models import *


class WilayaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wilaya
        fields = ('id', 'name', 'matricule')


class SurveySerializer(serializers.ModelSerializer):
    from patientapp.serializers import VaccinationAppointmentSerializer
    vaccination_appointment = VaccinationAppointmentSerializer(read_only=True)

    class Meta:
        fields = (
            "id",
            "positive_covid",
            "contamination",
            "disease",
            "temperature",
            "heart_rate",
            "respiratory_rate",
            "blood_pressure",
            "oximetry",
            'vaccination_appointment',
        )
        model = Survey


class VaccineSerializer(serializers.ModelSerializer):
    vaccine_centres = VaccineCentre()

    # create method

    class Meta:
        fields = ("name", "time_between_dose", "num_phone", "vaccine_centre",)
        model = Vaccine

    def create(self, validated_data):
        vaccine_centre_data = validated_data.pop('vaccine_centres')
        vaccine = Vaccine.objects.create(**validated_data)

        for vaccine_centre in vaccine_centre_data:
            vaccine_centre, created = VaccineCentre.objects.get_or_create(name=vaccine_centre['name'])
            vaccine.vaccine_centres.add(vaccine_centre)
        return vaccine_centre

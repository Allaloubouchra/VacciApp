from rest_framework import serializers
from rest_framework.fields import ReadOnlyField

from centreapp.models import Wilaya, Disease, City, Survey, VaccineCentre, Doctor, WorkingHours, Vaccine, \
    VaccineAndCentre


class DoctorSerializer(serializers.ModelSerializer):
    from patientapp.serializers import AccountSerializer
    account = AccountSerializer(read_only=False)

    class Meta:
        fields = (
            "id",
            "speciality",
            "position",
            "post",
            "account",
        )
        model = Doctor


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('id',
                  'name',
                  'matriculate',
                  'wilaya',)


class WilayaSerializer(serializers.ModelSerializer):
    cities = CitySerializer(many=True, required=False)

    class Meta:
        model = Wilaya
        fields = (
            'id',
            'name',
            'matricule',
            'cities'
        )


class DiseaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disease
        fields = ('id',
                  'name',
                  )


class WorkingHoursSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "centre",
            "day_of_week",
            "from_hour",
            "to_hour",
            "from_hour_s",
            "to_hour_s",
            "get_day_of_week_display",
        )
        model = WorkingHours


class VaccineSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "name",
            "time_between_dose",
            "vaccine_centre",
        )
        model = Vaccine


class VaccineAndCentreSerializer(serializers.ModelSerializer):
    vaccine_name = ReadOnlyField(source='vaccine.name')

    class Meta:
        fields = (
            "centre",
            "vaccine",
            "available",
            "vaccine_name"
        )
        model = VaccineAndCentre


class VaccineCentreSerializer(serializers.ModelSerializer):
    city = CitySerializer(read_only=True)
    working_hours = WorkingHoursSerializer(many=True, required=False)
    vaccines = VaccineAndCentreSerializer(many=True, required=False)

    class Meta:
        fields = (
            "id",
            "name",
            "address",
            "num_phone",
            "latitude",
            "longitude",
            "city",
            'working_hours',
            'vaccines'
        )
        model = VaccineCentre


class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'pk',
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

        extra_kwargs = {
            'pk': {
                'read_only': True,
            }
        }

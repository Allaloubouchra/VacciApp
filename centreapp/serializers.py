from rest_framework import serializers

from centreapp.models import Wilaya, Disease, City, Survey, VaccineCentre, Doctor, WorkingHours, Vaccine, \
    VaccineAndCentre


class DoctorSerializer(serializers.ModelSerializer):
    from patientapp.serializers import AccountSerializer
    account = AccountSerializer(read_only=True)

    class Meta:
        fields = (
            "id",
            "speciality",
            "position",
            "post",
            "account",
        )
        model = Doctor


class WilayaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wilaya
        fields = ('id',
                  'name',
                  'matriculate'
                  )


class CitySerializer(serializers.ModelSerializer):
    wilaya = WilayaSerializer(read_only=True)

    class Meta:
        model = City
        fields = ('id',
                  'name',
                  'matriculate',
                  'wilaya',)


class DiseaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disease
        fields = ('id',
                  'name',
                  )


class VaccineCentreSerializer(serializers.ModelSerializer):
    city = CitySerializer(read_only=True)

    class Meta:
        fields = (
            "id",
            "name",
            "address",
            "num_phone",
            "latitude",
            "longitude",
            "city",
        )
        model = VaccineCentre


class VaccineSerializer(serializers.ModelSerializer):
    vaccine_centres = VaccineCentreSerializer(read_only=True)

    class Meta:
        fields = (
            "id",
            "name",
            "time_between_dose",
            "vaccine_centres",
        )
        model = Vaccine


class VaccineAndCentreSerializer(serializers.ModelSerializer):
    centre = VaccineCentreSerializer(read_only=True)
    vaccine = VaccineSerializer(read_only=True)

    class Meta:
        fields = (
            "centre",
            "vaccine",
            "available",
        )
        model = VaccineAndCentre


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


class WorkingHoursSerializer(serializers.ModelSerializer):
    # create method not confirmed
    centre = VaccineCentreSerializer(required=False)

    class Meta:
        fields = (
            "id",
            "centre",
            "day_of_week",
            "from_hour",
            "to_hour",
            "from_hour_s",
            "to_hour_s",
        )
        model = WorkingHours



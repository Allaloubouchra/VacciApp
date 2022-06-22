from django.db.models import Q
from django.utils import timezone
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from centreapp.serializers import SurveySerializer
from patientapp import AppointmentStatus
from patientapp.models import Account
from patientapp.models import VaccinationAppointment
from patientapp.serializers import VaccinationAppointmentSerializer, AccountSerializer


class VaccinationAppointmentViewSet(ModelViewSet):
    serializer_class = VaccinationAppointmentSerializer
    queryset = VaccinationAppointment.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super(VaccinationAppointmentViewSet, self).get_queryset()
        if self.request.user.account.is_patient:
            queryset = queryset.filter(patient__user=self.request.user)
        if self.request.user.account.is_doctor_or_is_receptionist:
            queryset = queryset.filter(centre=self.request.user.account.vaccine_centre)
        if self.action == 'appointment_calendar':
            queryset = queryset.filter(appointment_date__date=timezone.now()) \
                .order_by('appointment_date__hour', 'appointment_date__minute')

        return queryset

    # if self.request.user.account.is_receptionist:
    # queryset = queryset.filter(appointment_date = date.today()).order_by('datetime__hour', 'datetime__minute')

    def get_serializer(self, *args, **kwargs):
        data = kwargs.pop('data', None)
        if data is not None:
            data['patient_id'] = self.request.user.account.pk
            return super(VaccinationAppointmentViewSet, self).get_serializer(data=data, *args, **kwargs)
        return super(VaccinationAppointmentViewSet, self).get_serializer(*args, **kwargs)

    @action(["GET"], detail=False, url_path="appointment-calendar", )
    def appointment_calendar(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(["POST"], detail=True, url_path='validate')
    def validate_appointment(self, request, *args, **kwargs):
        appointment: VaccinationAppointment = self.get_object()
        if appointment.status == AppointmentStatus.CONFIRMED:
            appointment.doctor = request.user.account
            appointment.status = AppointmentStatus.DONE
            survey_serializer = SurveySerializer(data=request.data)
            if survey_serializer.is_valid(raise_exception=True):
                survey_serializer.save()
            appointment.save()
            return Response({"status": "Success"})
        return Response({"status": "Success"})

    @action(["POST"], detail=True, url_path='cancel')
    def cancel_appointment(self, request, *args, **kwargs):
        appointment: VaccinationAppointment = self.get_object()
        if appointment.status == AppointmentStatus.CONFIRMED:
            appointment.doctor = request.user.account
            appointment.status = AppointmentStatus.CANCELED
            survey_serializer = SurveySerializer(data=request.data)
            if survey_serializer.is_valid(raise_exception=True):
                survey_serializer.save()
            appointment.save()
            return Response()


class AccountViewSet(ModelViewSet):
    serializer_class = AccountSerializer
    queryset = Account.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super(AccountViewSet, self).get_queryset()
        if self.request.user.account.is_patient:
            queryset = queryset.filter(user=self.request.user)
        if self.request.user.account.is_doctor_or_is_receptionist:
            queryset = queryset.filter(
                Q(centre=self.request.user.account.centre) | Q(appointment__centre=self.request.user.account.centre))
        return queryset

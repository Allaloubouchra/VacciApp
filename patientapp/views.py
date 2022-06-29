from django.db.models import Q, Count, F, Value
from django.utils import timezone
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny
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
            queryset = queryset.filter(appointment_date__date=timezone.now(), status=AppointmentStatus.CONFIRMED) \
                .order_by('appointment_date__hour', 'appointment_date__minute')
        if self.action == 'pending_appointments':
            queryset = queryset.filter(status=AppointmentStatus.PENDING)

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
        return self.list(request, *args, **kwargs)

    @action(["GET"], detail=False, url_path="pending-appointments", )
    def pending_appointments(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

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

    @action(["GET"], detail=False, url_path="proofs", permission_classes=[AllowAny])
    def get_proofs(self, request, *args, **kwargs):
        patient_id = self.request.data.get('id')
        patient = Account.objects.filter(pk=patient_id)
        if patient.exists():
            vaccines = list(
                VaccinationAppointment.objects
                .filter(patient=patient.first(), status=AppointmentStatus.CONFIRMED)
                .values('vaccine__name')
                .annotate(doses=Count('id'))
                .order_by('vaccine__name')
                .values('vaccine__name', 'vaccine__required_doses', 'doses',
                        valid=Value(F('required_doses') == F('doses')))
            )
            patient_data = AccountSerializer(instance=patient.first()).data
            patient_data['vaccines'] = vaccines
            return Response(patient_data)
        return Response(status=404)


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

from django.db.models import Q
from django.utils import timezone
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from patientapp.models import Account

from patientapp.serializers import VaccinationAppointmentSerializer, AccountSerializer
from patientapp.models import VaccinationAppointment


class VaccinationAppointmentViewSet(ModelViewSet):
    serializer_class = VaccinationAppointmentSerializer
    queryset = VaccinationAppointment.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super(VaccinationAppointmentViewSet, self).get_queryset()
        if self.request.user.account.is_patient:
            queryset = queryset.filter(patient__user=self.request.user)
        if self.request.user.account.is_doctor_or_is_receptionist:
            queryset = queryset.filter(centre=self.request.user.centre)
        if self.action == 'appointment_calendar':
            queryset = queryset.filter(appointment_date__date=timezone.now()) \
                .order_by('appointment_date__hour', 'appointment_date__minute')

        return queryset

    # if self.request.user.account.is_receptionist:
    # queryset = queryset.filter(appointment_date = date.today()).order_by('datetime__hour', 'datetime__minute')

    @action(["GET"], detail=False, url_path="appointment-calendar", )
    def appointment_calendar(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)




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

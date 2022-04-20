from django.db.models import Q
from rest_framework.permissions import IsAuthenticated
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
        if self.request.user.account.is_patient():
            queryset = queryset.filter(user=self.request.user)
        if self.request.user.account.is_doctor_or_is_receptionist():
            queryset = queryset.filter(centre=self.request.user.centre)
        return queryset


class AccountViewSet(ModelViewSet):
    serializer_class = AccountSerializer
    queryset = Account.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super(AccountViewSet, self).get_queryset()
        if self.request.user.account.is_patient():
            queryset = queryset.filter(user=self.request.user)
        if self.request.user.account.is_doctor_or_is_receptionist():
            queryset = queryset.filter(
                Q(centre=self.request.user.account.centre) | Q(appointment__centre=self.request.user.account.centre))
        return queryset

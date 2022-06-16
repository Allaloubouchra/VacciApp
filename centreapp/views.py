from django.forms import model_to_dict
from rest_framework import generics, status
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated

from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from centreapp.models import Survey, VaccineCentre, Vaccine
from centreapp.serializers import SurveySerializer, VaccineCentreSerializer, VaccineSerializer


class UserCreateAPIView(generics.CreateAPIView):
    from patientapp.serializers import UserSerializer
    from rest_framework.permissions import AllowAny
    from django.contrib.auth.models import User
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)


class RegisterApi(generics.GenericAPIView):
    def post(self, request):
        from patientapp.serializers import UserSerializer
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogInApi(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        data = {'token': token.key,
                'user_type': user.account.user_type}
        data.update(model_to_dict(user, exclude=["password", "user_permissions", "is_staff", "is_active"]))
        try:
            data.update(model_to_dict(user.account, fields="__all__"))
        except Exception:
            pass
        return Response(data)


class SurveyViewSet(ModelViewSet):
    serializer_class = SurveySerializer
    queryset = Survey.objects.all()
    # todo limit access for doctors and centre doctors

class CenterViewSet(ModelViewSet):
    serializer_class = VaccineCentreSerializer
    queryset = VaccineCentre.objects.all()
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        queryset = super(CenterViewSet, self).get_queryset()
        return queryset



class VaccinViewSet(ModelViewSet):
    serializer_class = VaccineSerializer
    queryset = Vaccine.objects.all()
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        queryset = super(VaccinViewSet, self).get_queryset()
        return queryset

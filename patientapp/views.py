<<<<<<< HEAD
from django.forms import model_to_dict
from rest_framework import generics, status
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from patientapp.serializers import UserSerializer

=======

from rest_framework import generics, status

from rest_framework.response import Response
from centreapp.serializers import UserSerializer

>>>>>>> 0f84395cd689b6fe93dac6c2855f78b89c2667b5

class RegisterApi(generics.GenericAPIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
<<<<<<< HEAD
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
=======
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
>>>>>>> 0f84395cd689b6fe93dac6c2855f78b89c2667b5

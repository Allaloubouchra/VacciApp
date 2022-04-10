
from rest_framework import generics, status

from rest_framework.response import Response
from centreapp.serializers import UserSerializer


class RegisterApi(generics.GenericAPIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
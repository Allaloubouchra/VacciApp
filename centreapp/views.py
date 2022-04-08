from django.forms import model_to_dict
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response


class LogInApi(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        data = {'token': token.key}
        data.update(model_to_dict(user, exclude=["password", "user_permissions", "is_staff", "is_active"]))
        try:

            data.update(model_to_dict(user.account, fields="__all__"))
        except Exception:
            pass
        return Response(data)

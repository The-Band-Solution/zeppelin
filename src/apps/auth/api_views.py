from .serializers import (
    RegistrarUsuarioSerializer,
)

from django.contrib.auth.models import User
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
#from rest_condition import And, Or
#from oauth2_provider.contrib.rest_framework import OAuth2Authentication, TokenHasReadWriteScope

class RegistrarUsuarioViewSet(viewsets.ModelViewSet):
    #ViewSet para registrar usuários.
    serializer_class = RegistrarUsuarioSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        return Response({
            "message": "Usuário cadastrado com sucesso"
        }, status=status.HTTP_201_CREATED)
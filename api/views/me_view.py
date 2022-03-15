from rest_framework.views import APIView
from ..serializers import usuario_serializer
from rest_framework.response import Response
from rest_framework import status as status_http
from rest_framework import permissions


class Me (APIView):
    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request, format=None):
        serlializer_usuario = usuario_serializer.UsuarioSerializer(
            request.user, context={"request": request})
        return Response(serlializer_usuario.data, status=status_http.HTTP_200_OK)

from .serializers import RegisterSerializer
from rest_framework import generics


class RegisterUser(generics.CreateAPIView):
    serializer_class = RegisterSerializer

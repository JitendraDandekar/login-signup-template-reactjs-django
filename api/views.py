from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from rest_framework.authtoken.models import Token

from .serializers import LoginSerializer, UserSerializer


# Create your views here.
class RegistrationViewSet(viewsets.ViewSet):

    @staticmethod
    def create(request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            User.objects.create_user(**serializer.data)
            return Response(data={"message": "User Created!"}, status=status.HTTP_201_CREATED)
        return Response(data={"message": "User Already Exists!"}, status=status.HTTP_400_BAD_REQUEST)


class LoginViewSet(viewsets.ViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]

    @staticmethod
    def create(request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(request, **serializer.validated_data)
            if user is not None:
                login(request, user)
                token, created = Token.objects.get_or_create(user=user)
                return Response(data={"token": token.key}, status=status.HTTP_200_OK)
            else:
                return Response({"message": "Invalid Credential!"}, status=status.HTTP_404_NOT_FOUND)

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import RegisterSerializer, UserSerializer, LoginSerializer


# Create your views here.

@api_view(['POST'])
def register_view(request):
    serializer = RegisterSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        username = serializer.data.get('username')
        password = serializer.data.get('password')
        user = User.objects.create_user(username=username, password=password)
        user.save()
        return Response(data={'message': 'ok'})
    else:
        return Response("Error! something went wrong")


@api_view(['POST'])
def auth_view(request):
    serializer = LoginSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        user = authenticate(username=serializer.validated_data.get('username'),
                            password=serializer.validated_data.get('password'))
        if not user:
            return Response("Authentications failed")
        return Response(UserSerializer(user).data)

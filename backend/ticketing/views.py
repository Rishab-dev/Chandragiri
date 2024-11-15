from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth.models import User, Group
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework import status, viewsets
from .models import *
from .serializers import *

class LoginView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            # token, _ = Token.objects.get_or_create(user=user)
            return Response(status = status.HTTP_200_OK)
        return Response(status=status.HTTP_401_UNAUTHORIZED)
    
class LogoutView(APIView):
    def post(self, request):
        username = request.data.get("username")
        token = request.data.get("token")
        user = User.objects.get(username=username)
        user_token = Token.objects.get(user=user)
        if user_token.key == token:
            user_token.delete()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_401_UNAUTHORIZED)

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [AllowAny]

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_class = [AllowAny]
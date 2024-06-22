from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import UserRegistrationSerializer
from django.contrib.auth.models import User

class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer

class VerifyOTPView(generics.GenericAPIView):
    def post(self, request, *args, **kwargs):
        otp = request.data.get('otp')
        username = request.data.get('username')
        user = User.objects.get(username=username)
        if user.profile.otp == otp:
            user.is_active = True
            user.profile.otp = ''
            user.save()
            user.profile.save()
            return Response({'message': 'Email verified successfully'}, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid OTP'}, status=status.HTTP_400_BAD_REQUEST)

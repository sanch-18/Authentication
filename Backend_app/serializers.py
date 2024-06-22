from django.contrib.auth.models import User
from rest_framework import serializers
from django.core.mail import send_mail
import random

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        user.is_active = False  # Deactivate account until it is verified
        user.save()
        self.send_otp(user)
        return user

    def send_otp(self, user):
        otp = random.randint(100000, 999999)
        user.profile.otp = otp
        user.profile.save()
        send_mail(
            'OTP Verification',
            f'Your OTP is {otp}',
            'from@example.com',
            [user.email],
            fail_silently=False,
        )

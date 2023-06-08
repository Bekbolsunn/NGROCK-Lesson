from django.contrib.auth.models import User
from rest_framework import serializers


class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=128)
    password = serializers.CharField(min_length=8)

    def validate(self, attrs):
        if User.objects.filter(username=attrs['username']).count() > 0:
            raise serializers.ValidationError({"username": "Username is already taken"})
        return attrs


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True, allow_blank=False)
    password = serializers.CharField(style={'input_type': 'password'}, min_length=8, required=True)

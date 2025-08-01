from rest_framework import serializers

class LoginInstaSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
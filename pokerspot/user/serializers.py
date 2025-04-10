from .models import CustomUser
from rest_framework import serializers

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    email = serializers.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password', 'receive_newsletter', 'terms')

    def validate_email(self, value):
        if CustomUser.objects.filter(email=value).exists():
            raise serializers.ValidationError("A user with that email already exists.")
        return value
    
    def validate_terms(self, value):
        if not value:
            raise serializers.ValidationError("To register you must accept terms and conditions.")
        return value

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            receive_newsletter=validated_data['receive_newsletter'],
            terms=validated_data['terms'],
        )
        return user
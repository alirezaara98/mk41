from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'full_name', 'is_staff', 'is_active')


class UserSerializer2(serializers.Serializer):
    email = serializers.EmailField(required=True)
    full_name = serializers.CharField(max_length=150)
    is_staff = serializers.BooleanField(default=False)
    is_active = serializers.BooleanField(default=False)

    def validate(self, attrs):
        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    def update(self, instance, validated_data):
        instance.update(**validated_data)
        instance.save()

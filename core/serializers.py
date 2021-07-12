from rest_framework import serializers
from django.contrib.auth.models import User
from core.models import Post


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
        ]


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'password',
        )

    def create(self, validated_data):
        password = validated_data.pop('password')

        user = User.objects.create(**validated_data)

        user.set_password(password)
        user.save()

        return user


class PostSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = Post
        fields = [
            'id',
            'description',
            'image',
            'create_date',
            'update_date',
            'created_by'
        ]
        read_only_fields = [
            'id',
            'create_date',
            'update_date',
            'created_by',
        ]

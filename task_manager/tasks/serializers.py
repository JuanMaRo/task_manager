from django.contrib.auth.models import Group, User
from rest_framework import serializers
from .models import Task, Category, Status

class UserSerializer(serializers.ModelSerializer):
    # Make sure that the password is not sent in the API response.
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        # Create a new user with a hashed password
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name']

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ['id', 'name']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class TaskSerializer(serializers.ModelSerializer):
    # Use a read-only field to display the username of the assignee.
    assignee_username = serializers.ReadOnlyField(source='assignee.username')
    status = serializers.SlugRelatedField(slug_field='name', queryset=Status.objects.all())
    category = serializers.SlugRelatedField(slug_field='name', queryset=Category.objects.all(), allow_null=True)

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'assignee', 'assignee_username', 'category', 'status']
        read_only_fields = ['assignee']

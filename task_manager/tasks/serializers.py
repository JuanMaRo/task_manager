from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Task, Category, Status

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ['id', 'name']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class TaskSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='task-detail')
    assignee_username = serializers.ReadOnlyField(source='assignee.username')
    status = serializers.SlugRelatedField(slug_field='name', queryset=Status.objects.all())
    category = serializers.SlugRelatedField(slug_field='name', queryset=Category.objects.all(), allow_null=True)

    class Meta:
        model = Task
        fields = ['id', 'url', 'title', 'description', 'assignee', 'assignee_username', 'category', 'status']
        read_only_fields = ['assignee']

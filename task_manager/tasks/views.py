from django.contrib.auth.models import User
from rest_framework import viewsets, permissions, mixins
from .models import Task, Category, Status
from .serializers import UserSerializer, TaskSerializer, CategorySerializer, StatusSerializer
from .permissions import IsOwnerOrReadOnly

class UserViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    API endpoint that allows users to be registered.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

class TaskViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows tasks to be viewed, created, edited or deleted.
    """
    queryset = Task.objects.all()

    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    filterset_fields = ['category', 'status']

    def perform_create(self, serializer):
        serializer.save(assignee=self.request.user)

class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows categories to be viewed or edited by any authenticated user.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]

class StatusViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    permission_classes = [permissions.IsAuthenticated]

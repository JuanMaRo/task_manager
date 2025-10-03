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
    permission_classes = [permissions.AllowAny] # Allow anyone to register

class TaskViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows tasks to be viewed, created, edited or deleted.
    """
    # Only show tasks that belong to the current user
    # Allow all authenticated users to see all tasks.
    # Permissions will handle who can edit/delete.
    queryset = Task.objects.all()

    # Force the use of the full template rendering context for the browsable API
    template_name = 'rest_framework/api.html'

    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    filterset_fields = ['category', 'status']

    def perform_create(self, serializer):
        # Automatically assign the logged-in user as the assignee
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

from todo.models import TodoModel
from rest_framework import viewsets, permissions
from .serializers import TodoSerializer


class TodoViewSet(viewsets.ModelViewSet):
    queryset = TodoModel.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = TodoSerializer

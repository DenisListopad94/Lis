from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication, SessionAuthentication,TokenAuthentication
from rest_framework import mixins
from rest_framework.authtoken.models import Token


from api.tasks_api.serializers.tasks_serializer import TaskSerializer
from task_tracker.models import Task


class TaskList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
from .models import Task
from .serializers import TaskSerializer
from rest_framework.generics import ListCreateAPIView


# Create your views here.

class Taskslists(ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

from .models import Task
from .serializers import TaskSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

# Create your views here.

class Taskslists(ListCreateAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

# class DetailsOfTasks(RetrieveUpdateDestroyAPIView):
#     serializer_class = TaskSerializer
#     queryset = Task.objects.all()


# class Taskslists2(APIView):
#     def get(self, request):
#         tasks = Task.objects.all()
#         serializer = TaskSerializer(tasks, many=True)
#         return Response(serializer.data)


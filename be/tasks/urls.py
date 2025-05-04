from django.urls import path
from .views import(
    Taskslists,
)

urlpatterns = [
    path('tasks/', Taskslists.as_view(), name='task-list'),
]

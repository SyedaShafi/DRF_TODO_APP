from django.urls import path
from . import views



# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', views.allAPIView, name='api-view'),
    path('task-list/', views.taskList, name='task-list'),
    path('task-detail/<str:pk>/', views.taskDetail, name='task-detail'),
    path('add-task/', views.addTask, name='add-task'),
    path('update-task/<str:pk>/', views.updateTask, name='update-task'),
    path('delete-task/<str:pk>/', views.deleteTask, name='delete-task'),
]
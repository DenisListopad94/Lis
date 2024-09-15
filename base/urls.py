from django.urls import path
from . import views


# urlpatterns = [
#     path("main/", views.main, name="main"),
#     path("main/user_tasks/", views.user_tasks, name="user_tasks"),
# ]

urlpatterns = [
    path('main/', views.main, name='main'),
    path('base/main/tasks/', views.task, name='task'),
    path('base/main/tasks/users/', views.user, name='user'),
]
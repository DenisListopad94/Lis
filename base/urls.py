from django.urls import path
from . import views


# urlpatterns = [
#     path("main/", views.main, name="main"),
#     path("main/user_tasks/", views.user_tasks, name="user_tasks"),
# ]

urlpatterns = [
    path('main/', views.main, name='main'),
]
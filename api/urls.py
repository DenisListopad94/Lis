from django.urls import path, include

urlpatterns = [
    path('users/', include('api.users_api.urls')),
    path('comments/', include('api.comments_api.urls')),
    path('tasks/', include('api.tasks_api.urls')),
]
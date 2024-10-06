from django.urls import path
from .views import views
from base.views import (
    MainPageView, LoginTemplateView
)


# urlpatterns = [
#     path("main/", views.main, name="main"),
#     path("main/user_tasks/", views.user_tasks, name="user_tasks"),
# ]

# urlpatterns = [rabochee
#     path('main/', views.main, name='main'),
#     path('base/main/tasks/', views.task, name='task'),
#     path('base/main/tasks/users/', views.user, name='user'),
# ]


urlpatterns = [
    path('', MainPageView.as_view()),
    path('login/', LoginTemplateView.as_view()),
    path('base/main/tasks/users/', views.users, name='users'),
]
from django.urls import path
from .views import show_all_tasks, create_task_form
from .view.comment_view import show_all_comments, create_comment_form

urlpatterns = [
    path('', show_all_tasks, name='all_tasks'),
    path('create', create_task_form),
    path('comments', show_all_comments, name='all_comments'),
    path('comments/create_comment', create_comment_form)
]
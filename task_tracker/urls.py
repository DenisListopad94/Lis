from django.urls import path
'''show_all_tasks'''
from .views import create_task_form, TaskDetailView
'''show_all_comments'''
from .view.comment_view import create_comment_form, CommentsTemplateView

urlpatterns = [
    # path('', show_all_tasks, name='all_tasks'),
    path('<int:pk>', TaskDetailView.as_view(), name='all_tasks'),
    path('create', create_task_form),
    # path('comments', show_all_comments, name='all_comments'),
    path('comments', CommentsTemplateView.as_view(), name='all_comments'),
    path('comments/create_comment', create_comment_form)
]
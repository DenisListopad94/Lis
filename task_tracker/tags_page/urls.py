from django.urls import path
from task_tracker.tags_page.views import TagsTemplateView


urlpatterns = [
    path('', TagsTemplateView.as_view(), name='all_tags')
]
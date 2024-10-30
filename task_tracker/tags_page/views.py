from task_tracker.models import Tag
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class TagsTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'tags.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag_tasks'] = Tag.objects.all()
        return context
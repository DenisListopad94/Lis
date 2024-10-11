from django.contrib import admin
from task_tracker.models import Attachment, Comment, Project, Tag, Task
from django.utils.safestring import mark_safe

class CommentInline(admin.TabularInline):
    model = Comment


class TaskInline(admin.TabularInline):
    model = Task


class AttachmentInline(admin.TabularInline):
    model = Attachment


class TagMembershipInline(admin.TabularInline):
    model = Tag.tasks.through


@admin.display(description='фото')
def get_html_photo(object):
    if object.photo:
        return mark_safe(f'<img src={object.photo.url} width=50>')


@admin.register(Attachment)
class AttachmentAdmin(admin.ModelAdmin):
    list_display = ['file_name', 'file', 'image', 'user', 'task']
    search_fields = ['file_name']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content', 'task', 'user', get_html_photo, 'specs']
    list_display_links = ['title', 'task']
    ordering = ['task', 'user']
    search_fields = ['content', 'id']
    list_per_page = 10
    list_filter = ['user', 'task']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description']
    list_display_links = ['name']
    search_fields = ['description']
    list_filter = ['name']
    inlines = [
        TaskInline
    ]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    inlines = [
        TagMembershipInline
    ]


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'status', 'priority', 'height_level', 'project', 'user']
    list_display_links = ['title', 'user']
    search_fields = ['title', 'description']
    list_filter = ['status', 'priority', 'height_level']
    list_per_page = 10
    actions = ['create_task_completed']
    @admin.action(description='Task completed')
    def create_task_completed(modeladmin, request, queryset):
        queryset.update(status='cl')

    inlines = [
        CommentInline,
        AttachmentInline,
        TagMembershipInline
    ]
from django.contrib import admin
from task_tracker.models import Attachment, Comment, Project, Tag, Task

@admin.register(Attachment)
class AttachmentAdmin(admin.ModelAdmin):
    ...


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    ...


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    ...


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    ...


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    ...
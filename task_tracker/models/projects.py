from django.db import models


class Projects(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
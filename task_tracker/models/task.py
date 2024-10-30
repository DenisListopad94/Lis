from django.db import models
from custom_user.models import User
from base.models import BaseModel

STATUS_CHOICES=[
    ('op', 'Open'),
    ('cl', 'Close'),
    ('pr', 'Process'),
]

PRIORITY_CHOICES=[
    ('h', 'High'),
    ('m', 'Medium'),
    ('l', 'Low'),
]

class Task(BaseModel, models.Model):
    title = models.CharField(
        max_length=64,
        verbose_name = 'название'
    )
    description = models.CharField(
        max_length=256,
        verbose_name = 'описание'
    )
    status = models.CharField(
        choices=STATUS_CHOICES,
        max_length=2,
        null=True,
        blank=True,
        verbose_name = 'статус'
    )
    priority = models.CharField(
        choices=PRIORITY_CHOICES,
        max_length=2,
        null=True,
        blank=True,
        verbose_name = 'приоритет'
    )
    height_level = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name = 'уровень'
    )
    project = models.ForeignKey(
        to='Project',
        on_delete=models.CASCADE,
        related_name='tasks',
        null=True,
        blank=True,
        verbose_name = 'проект'
    )
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='tasks',
        null=True,
        blank=True,
        verbose_name = 'пользователь'

    )

    def __str__(self):
        return self.title


    class Meta:
        db_table = 'task'
        verbose_name = 'задача'
        verbose_name_plural = 'задача'

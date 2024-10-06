from django.db import models
from base.models import BaseModel


class Tag(BaseModel, models.Model):
    name = models.CharField(
        max_length=64,
        verbose_name = 'имя'
    )
    tasks = models.ManyToManyField(
        to='Task',
        related_name='tags',
        verbose_name = 'задачи'
    )


    def __str__(self):
        return self.name


    class Meta:
        db_table = 'tag'
        verbose_name = 'тэг'
        verbose_name_plural = 'тэг'

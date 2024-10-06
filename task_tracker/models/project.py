from django.db import models
from base.models import BaseModel


class Project(BaseModel, models.Model):
    name = models.CharField(
        max_length=64,
        verbose_name = 'имя'
    )
    description = models.CharField(
        max_length=256,
        verbose_name = 'описание'
    )


    def __str__(self):
        return self.name


    class Meta:
        db_table = 'project'
        verbose_name = 'проект'
        verbose_name_plural = 'проект'

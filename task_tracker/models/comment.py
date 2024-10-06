from django.db import models
from custom_user.models import User
from base.models import BaseModel



class Comment(BaseModel, models.Model):
    title = models.CharField(
        max_length=64,
        verbose_name = 'название'
    )
    content = models.CharField(
        max_length=256,
        verbose_name = 'контент'
    )
    task = models.ForeignKey(
        to='Task',
        on_delete=models.CASCADE,
        related_name='comments',
        null=True,
        blank=True,
        verbose_name='задача'
    )
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='comments',
        null=True,
        blank=True,
        verbose_name='пользователь'
    )


    def __str__(self):
        return self.title


    class Meta:
        db_table = 'comment'
        verbose_name = 'комментарий'
        verbose_name_plural = 'комментарий'

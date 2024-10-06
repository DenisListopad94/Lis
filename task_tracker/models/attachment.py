from django.db import models
from custom_user.models import User
from base.models import BaseModel


class Attachment(BaseModel, models.Model):
    file_name = models.CharField(
        max_length=64,
        null=True,
        verbose_name = 'имя файла'
    )
    file = models.FileField(
        null=True,
        verbose_name = 'фаил'
    )
    image = models.ImageField(
        null=True,
        verbose_name = 'изображение'
    )
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='attachments',
        null=True,
        verbose_name = 'пользователь'
    )
    task = models.ForeignKey(
        to='Task',
        on_delete=models.CASCADE,
        related_name='attachments',
        null=True,
        verbose_name = 'задача'
    )


    def __str__(self):
        return self.file_name


    class Meta:
        db_table = 'attachment'
        verbose_name = 'вложения'
        verbose_name_plural = 'вложения'
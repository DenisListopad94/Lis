# Generated by Django 5.1.1 on 2024-10-08 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_tracker', '0010_alter_attachment_file_alter_attachment_file_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='photo',
            field=models.ImageField(null=True, upload_to='comments'),
        ),
        migrations.AddField(
            model_name='comment',
            name='specs',
            field=models.FileField(null=True, upload_to='Downloads'),
        ),
    ]

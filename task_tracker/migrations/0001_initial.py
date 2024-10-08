# Generated by Django 5.1.1 on 2024-09-15 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('description', models.CharField(max_length=256)),
                ('status', models.CharField(choices=[('op', 'Open'), ('cl', 'Close'), ('pe', 'Process')], max_length=2, null=True)),
                ('priority', models.CharField(choices=[('h', 'High'), ('m', 'Medium'), ('l', 'Low')], max_length=2, null=True)),
                ('height_level', models.PositiveIntegerField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]

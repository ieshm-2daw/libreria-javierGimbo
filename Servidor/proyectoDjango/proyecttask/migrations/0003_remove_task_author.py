# Generated by Django 3.2.23 on 2023-11-08 09:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proyecttask', '0002_task_published_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='author',
        ),
    ]
# Generated by Django 2.2.24 on 2021-11-09 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_remove_task_progress'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='task_type',
            field=models.CharField(default='train', max_length=1000),
        ),
    ]
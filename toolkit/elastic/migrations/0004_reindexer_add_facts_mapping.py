# Generated by Django 2.2.17 on 2020-12-15 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elastic', '0003_index'),
    ]

    operations = [
        migrations.AddField(
            model_name='reindexer',
            name='add_facts_mapping',
            field=models.BooleanField(default=False),
        ),
    ]
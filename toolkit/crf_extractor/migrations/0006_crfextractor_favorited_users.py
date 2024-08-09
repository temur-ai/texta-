# Generated by Django 2.2.28 on 2022-06-28 13:01

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('crf_extractor', '0005_change_feature_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='crfextractor',
            name='favorited_users',
            field=models.ManyToManyField(related_name='crf_extractor_crfextractor_favorited_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
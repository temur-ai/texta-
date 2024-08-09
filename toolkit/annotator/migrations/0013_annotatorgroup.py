# Generated by Django 2.2.28 on 2022-05-12 09:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('annotator', '0012_auto_20220512_1150'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnnotatorGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('children', models.ManyToManyField(default=None, related_name='annotator_group_children', to='annotator.Annotator')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='annotator.Annotator')),
            ],
        ),
    ]
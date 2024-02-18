# Generated by Django 5.0.2 on 2024-02-18 10:54

import class_based_views_advanced.web.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_remove_todo_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='slug',
            field=models.SlugField(default=class_based_views_advanced.web.models.generate_slug, editable=False),
        ),
    ]

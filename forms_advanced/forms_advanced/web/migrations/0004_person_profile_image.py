# Generated by Django 3.2.23 on 2024-02-07 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_person_created_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='web/profile_images'),
        ),
    ]

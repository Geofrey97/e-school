# Generated by Django 3.2.6 on 2021-09-09 08:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_rename_description_video_caption'),
    ]

    operations = [
        migrations.RenameField(
            model_name='video',
            old_name='course',
            new_name='course_name',
        ),
    ]

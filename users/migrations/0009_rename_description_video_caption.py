# Generated by Django 3.2.6 on 2021-09-08 07:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20210908_1016'),
    ]

    operations = [
        migrations.RenameField(
            model_name='video',
            old_name='description',
            new_name='caption',
        ),
    ]

# Generated by Django 3.2.6 on 2021-10-07 08:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Questions', '0004_alter_answers_options'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Answers',
            new_name='Answer',
        ),
    ]

# Generated by Django 3.2.6 on 2021-10-03 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Quizes', '0002_alter_quiz_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quiz',
            old_name='no_of_questions',
            new_name='time',
        ),
        migrations.AddField(
            model_name='quiz',
            name='number_of_questions',
            field=models.IntegerField(default=10),
            preserve_default=False,
        ),
    ]

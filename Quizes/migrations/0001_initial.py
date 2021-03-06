# Generated by Django 3.2.6 on 2021-10-03 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('topic', models.CharField(max_length=120)),
                ('no_of_questions', models.IntegerField(help_text='Duration of quiz in minutes')),
                ('requied_score_to_pass', models.IntegerField(help_text='required score in %')),
            ],
            options={
                'verbose_name_plural': 'Qizes',
            },
        ),
    ]

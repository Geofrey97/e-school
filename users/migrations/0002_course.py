# Generated by Django 3.2.6 on 2021-09-07 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=100)),
                ('coarse_description', models.TextField()),
                ('coarse_image', models.ImageField(upload_to='course')),
            ],
        ),
    ]

# Generated by Django 3.2.6 on 2021-09-07 08:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_course_coarse_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='course_module',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_module_name', models.CharField(max_length=200)),
                ('course_description', models.TextField()),
                ('video_url', models.URLField(max_length=300)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.course')),
            ],
        ),
    ]

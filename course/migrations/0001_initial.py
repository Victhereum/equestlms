# Generated by Django 3.2.16 on 2022-10-16 19:30

import auto_prefetch
import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visible', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(help_text='Title of the course', max_length=125)),
                ('slug', models.SlugField(blank=True, max_length=125, null=True)),
                ('overview', ckeditor.fields.RichTextField()),
                ('cover_image', models.ImageField(upload_to='./courses_cover_images/')),
                ('price', models.PositiveIntegerField(default=0)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('new', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'prefetch_manager',
            },
            managers=[
                ('objects', django.db.models.manager.Manager()),
                ('prefetch_manager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='ClassRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visible', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('course', auto_prefetch.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='course_users', to='course.course')),
            ],
            managers=[
                ('objects', django.db.models.manager.Manager()),
                ('prefetch_manager', django.db.models.manager.Manager()),
            ],
        ),
    ]

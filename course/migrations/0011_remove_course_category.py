# Generated by Django 3.2.16 on 2022-10-19 07:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0010_alter_course_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='category',
        ),
    ]
# Generated by Django 3.2.16 on 2022-10-16 03:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_alter_task_tutor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='tutor',
            new_name='course',
        ),
    ]
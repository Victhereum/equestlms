# Generated by Django 3.2.16 on 2022-10-18 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_remove_student_birthday'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='enrolled_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]

# Generated by Django 3.2.16 on 2022-10-18 22:06

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20221018_2133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=django_resized.forms.ResizedImageField(crop=None, force_format=None, keep_meta=True, quality=0, size=[850, 300], upload_to='blog_img/'),
        ),
    ]

# Generated by Django 2.2.3 on 2020-04-04 10:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tradebooks', '0027_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='book',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='info',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='price',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='user',
        ),
    ]
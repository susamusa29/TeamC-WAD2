# Generated by Django 2.2.3 on 2020-04-07 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tradebooks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('title', models.CharField(max_length=50)),
                ('message', models.TextField()),
            ],
        ),
    ]

# Generated by Django 2.2.3 on 2020-04-02 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tradebooks', '0025_auto_20200403_0351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='bookID',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]

# Generated by Django 2.2.3 on 2020-04-02 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tradebooks', '0022_listing_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='picture',
            field=models.ImageField(blank=True, upload_to='book_images'),
        ),
    ]
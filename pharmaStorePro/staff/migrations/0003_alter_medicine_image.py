# Generated by Django 4.2.4 on 2023-08-24 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0002_medicine_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicine',
            name='image',
            field=models.ImageField(upload_to='images'),
        ),
    ]

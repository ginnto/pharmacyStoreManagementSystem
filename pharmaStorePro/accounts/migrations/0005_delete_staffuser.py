# Generated by Django 4.2.4 on 2023-09-23 20:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_staffuser_password'),
    ]

    operations = [
        migrations.DeleteModel(
            name='StaffUser',
        ),
    ]

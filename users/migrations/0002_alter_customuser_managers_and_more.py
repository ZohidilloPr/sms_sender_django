# Generated by Django 4.1.7 on 2023-02-24 03:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='customuser',
            managers=[
            ],
        ),
        migrations.RenameField(
            model_name='customuser',
            old_name='phone_num',
            new_name='phone',
        ),
    ]

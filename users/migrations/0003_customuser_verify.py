# Generated by Django 4.1.7 on 2023-02-24 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_customuser_managers_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='verify',
            field=models.BooleanField(default=False),
        ),
    ]

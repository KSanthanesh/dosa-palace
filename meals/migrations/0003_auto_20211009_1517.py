# Generated by Django 3.2.7 on 2021-10-09 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0002_reserve_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserve',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='reserve',
            name='time',
            field=models.TimeField(null=True),
        ),
    ]

# Generated by Django 4.1.3 on 2023-04-06 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorme', '0002_tutorprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutorprofile',
            name='hourly_rate',
            field=models.FloatField(default=0),
        ),
    ]

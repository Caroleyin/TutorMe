# Generated by Django 4.1.3 on 2023-04-12 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorme', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appuser',
            name='hourly_rate',
            field=models.FloatField(default=0),
        ),
    ]

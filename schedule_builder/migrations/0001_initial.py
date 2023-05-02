# Generated by Django 4.1.7 on 2023-04-29 16:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tutorme', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Requests',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_title', models.CharField(blank=True, max_length=255, null=True)),
                ('start_time', models.DateTimeField(blank=True, null=True)),
                ('end_time', models.DateTimeField(blank=True, null=True)),
                ('student_id', models.CharField(blank=True, max_length=255, null=True)),
                ('tutor_id', models.CharField(blank=True, max_length=255, null=True)),
                ('accepted', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('start', models.DateTimeField(blank=True, null=True)),
                ('end', models.DateTimeField(blank=True, null=True)),
                ('schedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule_builder.schedule')),
            ],
        ),
    ]

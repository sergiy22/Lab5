# Generated by Django 2.2.6 on 2019-11-22 08:10

from django.db import migrations, models
import uuid

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AtmoSensor',
            fields=[
                ('id',models.UUIDField(default=uuid.uuid4, help_text='this is unique ID LUL', primary_key=True, serialize=False)),
                ('lon', models.FloatField()),
                ('lat', models.FloatField()),
                ('date', models.DateField(auto_now=True)),
                ('time', models.TimeField(auto_now=True)),
                ('temperature', models.FloatField()),
                ('name', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CO2Sensor',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='this is unique ID ZULUL', primary_key=True, serialize=False)),
                ('lon', models.FloatField()),
                ('lat', models.FloatField()),
                ('date', models.DateField(auto_now=True)),
                ('time', models.TimeField(auto_now=True)),
                ('pressure', models.FloatField()),
                ('name', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
        ),
    ]

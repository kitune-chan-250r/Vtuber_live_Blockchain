# Generated by Django 3.1.5 on 2021-01-13 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('liver', models.CharField(max_length=999, primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=100)),
                ('startdatetime', models.CharField(max_length=100)),
                ('stream_url', models.CharField(max_length=100)),
                ('onair', models.BooleanField()),
                ('audience', models.IntegerField()),
            ],
        ),
    ]

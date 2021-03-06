# Generated by Django 3.1.5 on 2021-01-13 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blockchain', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.IntegerField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('transactions', models.TextField()),
                ('previous_hash', models.TextField()),
            ],
        ),
    ]

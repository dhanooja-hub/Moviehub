# Generated by Django 5.0.3 on 2024-05-28 07:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_album'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tracks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('duration', models.CharField(max_length=200)),
                ('track_number', models.PositiveIntegerField(default=1)),
                ('singers', models.CharField(max_length=200)),
                ('genre', models.CharField(max_length=200)),
                ('album_object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.album')),
            ],
        ),
    ]

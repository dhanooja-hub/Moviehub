# Generated by Django 5.0.3 on 2024-05-28 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_actor_delete_employee'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('language', models.CharField(max_length=200)),
                ('director', models.CharField(max_length=200)),
                ('year', models.CharField(max_length=200)),
            ],
        ),
    ]

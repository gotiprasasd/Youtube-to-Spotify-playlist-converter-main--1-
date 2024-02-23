# Generated by Django 4.1.7 on 2023-03-03 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CacheEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=255, unique=True)),
                ('value', models.TextField()),
            ],
            options={
                'db_table': 'my_cache_table',
            },
        ),
    ]

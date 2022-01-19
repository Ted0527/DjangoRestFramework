# Generated by Django 3.2.7 on 2022-01-19 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watchlist_app', '0006_point_pointinfo_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'movies',
            },
        ),
    ]

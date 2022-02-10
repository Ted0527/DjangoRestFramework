# Generated by Django 3.2.7 on 2022-02-10 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('thumbnail_image', models.URLField()),
                ('price', models.IntegerField(default=0)),
                ('list_price', models.IntegerField(default=0)),
                ('out_of_stock', models.BooleanField(default=True)),
                ('tag', models.CharField(blank=True, max_length=10)),
            ],
        ),
    ]
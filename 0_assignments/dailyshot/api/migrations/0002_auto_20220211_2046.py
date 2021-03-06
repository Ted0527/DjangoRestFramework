# Generated by Django 3.2.7 on 2022-02-11 20:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ManyToManyField(to='api.Product')),
                ('tag', models.ManyToManyField(to='api.Tag')),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='api.producttag'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tags', to='api.producttag'),
        ),
    ]

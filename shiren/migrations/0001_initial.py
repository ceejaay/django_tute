# Generated by Django 4.1.1 on 2022-11-22 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=256)),
                ('item_type', models.CharField(max_length=256)),
                ('buy_price', models.CharField(max_length=256)),
                ('sell_price', models.CharField(max_length=256)),
            ],
        ),
    ]

# Generated by Django 4.0.1 on 2022-11-24 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0010_auction_creator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='time_sent',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
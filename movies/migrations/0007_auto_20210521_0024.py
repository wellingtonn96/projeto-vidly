# Generated by Django 2.2.23 on 2021-05-21 00:24

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0006_auto_20210521_0023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='date_created',
            field=models.DateField(default=datetime.datetime(2021, 5, 21, 0, 24, 10, 497085, tzinfo=utc)),
        ),
    ]
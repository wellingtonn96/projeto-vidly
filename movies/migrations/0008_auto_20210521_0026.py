# Generated by Django 2.2.23 on 2021-05-21 00:26

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0007_auto_20210521_0024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='date_created',
            field=models.DateField(default=datetime.datetime(2021, 5, 21, 0, 26, 3, 118537, tzinfo=utc)),
        ),
    ]

# Generated by Django 2.1.3 on 2018-12-12 03:40

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('clinical', '0002_auto_20181212_0339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='date_of_first_visit',
            field=models.DateField(default=datetime.datetime(2018, 12, 12, 3, 40, 24, 632019, tzinfo=utc)),
        ),
    ]

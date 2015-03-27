# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('labinv', '0005_auto_20150324_2331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tube',
            name='date',
            field=models.DateField(default=datetime.date(2015, 3, 25)),
            preserve_default=True,
        ),
    ]

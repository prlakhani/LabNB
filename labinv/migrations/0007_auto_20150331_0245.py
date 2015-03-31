# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('labinv', '0006_auto_20150325_2022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grna',
            name='prodSize',
            field=models.IntegerField(blank=True, null=True, verbose_name='PCR product size for these primers', default=300),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tube',
            name='date',
            field=models.DateField(default=datetime.date(2015, 3, 31)),
            preserve_default=True,
        ),
    ]

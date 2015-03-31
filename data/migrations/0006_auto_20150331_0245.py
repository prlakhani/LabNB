# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0005_auto_20150325_2022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experiment',
            name='date',
            field=models.DateField(verbose_name='Date; if in doubt, end date', default=datetime.date(2015, 3, 31)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='filedata',
            name='date',
            field=models.DateField(default=datetime.date(2015, 3, 31)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='inxsurvivalexp',
            name='inx',
            field=models.OneToOneField(to='data.uInjection'),
            preserve_default=True,
        ),
    ]

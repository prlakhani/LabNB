# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0007_auto_20150331_0410'),
    ]

    operations = [
        migrations.AddField(
            model_name='gel',
            name='final',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='miscfile',
            name='final',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='experiment',
            name='date',
            field=models.DateField(default=datetime.date(2015, 4, 5), verbose_name='Date; if in doubt, end date'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='filedata',
            name='date',
            field=models.DateField(default=datetime.date(2015, 4, 5)),
            preserve_default=True,
        ),
    ]

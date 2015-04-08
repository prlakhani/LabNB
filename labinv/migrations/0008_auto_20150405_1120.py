# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('labinv', '0007_auto_20150331_0245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tube',
            name='date',
            field=models.DateField(default=datetime.date(2015, 4, 5)),
            preserve_default=True,
        ),
    ]

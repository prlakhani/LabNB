# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0004_auto_20150324_1920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experiment',
            name='date',
            field=models.DateField(default=datetime.date(2015, 3, 25), verbose_name='Date; if in doubt, end date'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='filedata',
            name='date',
            field=models.DateField(default=datetime.date(2015, 3, 25)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='uinjection',
            name='cas9',
            field=models.ForeignKey(to='labinv.cas9', related_name='inxcas9'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='uinjection',
            name='gRNA',
            field=models.ForeignKey(to='labinv.gRNA', related_name='inxgRNA'),
            preserve_default=True,
        ),
    ]

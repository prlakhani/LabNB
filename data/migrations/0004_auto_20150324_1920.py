# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0003_auto_20150324_1839'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='experiment',
            name='shortName',
        ),
        migrations.AddField(
            model_name='miscexp',
            name='shortName',
            field=models.CharField(max_length=50, default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='survivalexp',
            name='shortName',
            field=models.CharField(max_length=50, default=''),
            preserve_default=False,
        ),
    ]
